from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand

import os
import codecs
import pathlib
from bs4 import BeautifulSoup

from pages.models import Project
from pages.repository.models_repository import ModelsRepository
from pages.utils.datetime import datetime_provider


class Command(BaseCommand):
    help = 'Generate static website and change urls in each header to static version'
    date_provider = datetime_provider.DatetimeAsStringProvider()
    repository = ModelsRepository()
    path_to_write = ''

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int)

    def generate_static_website(self, *args, **options):
        original_active_project = None
        key = 'id'
        if key not in options:
            raise Exception('Jako argument wywołania komendy należy podać id projektu do eksportu.')
        else:
            project_to_export_id = options[key]
            project_to_export = Project.objects.get(id=project_to_export_id)
            currently_active_projects = Project.objects.filter(is_active=True)
            if project_to_export:
                self.repository.deactivate_all_projects_but_one_with_given_id(project_to_export.id)
                self.path_to_write = f'{settings.BASE_DIR}/{settings.DISTILL_DIR}\\{self.date_provider.now()}-{project_to_export.title}\\'
                pathlib.Path(self.path_to_write).mkdir(parents=True, exist_ok=True)
                call_command('distill-local', '--force', self.path_to_write)

                if len(currently_active_projects) > 0:
                    project_to_export.is_active = False
                    project_to_export.save()
                    for project in currently_active_projects:
                        project.is_active = True
                        project.save()


    def replace_urls(self):
        string_to_find_1 = '/blog/'
        string_to_find_2 = '/kontakt/'
        string_to_replace_1 = '/blog'
        string_to_replace_2 = '/kontakt'

        exclude_dirs = ['media', 'static']

        for (root_path, dirs, files) in os.walk(self.path_to_write):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                get_file = os.path.join(root_path, file)
                with codecs.open(get_file, "r+") as f:
                    soup = BeautifulSoup(f, "html.parser", from_encoding="utf-8")
                    blog_href = soup.find('a', attrs={'href': string_to_find_1})
                    contact_href = soup.find('a', attrs={'href': string_to_find_2})
                    try:
                        if blog_href:
                            blog_href.attrs['href'] = string_to_replace_1
                        if contact_href:
                            contact_href.attrs['href'] = string_to_replace_2
                        wanted_soup = soup
                    except Exception as e:
                        self.stdout.write(f'Urls has been changed already! {get_file}, error: {e}')
                    else:
                        try:
                            with open(get_file, "w") as f:
                                f.write(str(wanted_soup.prettify()))
                        except Exception as e:
                            self.stdout.write(f'Could not open and write to: {get_file}, error: {e}')

    def handle(self, *args, **options):
        try:
            self.generate_static_website(*args, **options)
            self.replace_urls()
            self.stdout.write(self.style.SUCCESS(f'********** Command has been execute without any error **********'))
        except Exception as e:
            self.stdout.write(e)
            self.stdout.write(self.style.NOTICE(f'********** Command  can not be execute! **********'))
