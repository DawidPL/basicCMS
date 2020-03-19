from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.models import User

from pages.models import (SiteSettings,
                          Homepage,
                          Subpage,
                          ContactPage,
                          BlogPost,
                          Box,
                          Carousel,
                          Multilanguage,
                          SocialMedia,
                          Project)


class ModelsRepository:
    project = None
    __instance = None

    def __init__(self):
        active_projects = Project.objects.filter(is_active=True)
        # TODO: Tutaj najpierw powinniśmy sprawdzić, czy nie istnieje jakiś projekt i aktywowac pierwszy z brzegu, a tylko jeśli nie ma żadnego tworzyć nowy, domyślny projekt
        if len(active_projects) > 0:
            self.project = active_projects[0]
        else:
             self.create_default_project_with_first_superuser_as_author()

    def create_default_project_with_first_superuser_as_author(self):
        users = User.objects.filter(is_superuser=True)
        if len(users) == 0:
            raise Exception('Najpierw wywołaj komendę "py manage.py createsuperuser"')
        else:
            self.project = Project.objects.create(title='default_project_1',
                                                  author='Dawid',
                                                  comment='Ten projekt został utworzony automatycznie.',
                                                  is_active=True)

    '''
    https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    '''

    def __new__(cls):
        if ModelsRepository.__instance is None:
            ModelsRepository.__instance = object.__new__(cls)
        return ModelsRepository.__instance

    def get_project(self):
        return self.project

    def get_project_name(self):
        return self.project.title

    def set_project(self, project: Project) -> 'ModelsRepository':
        self.project = project
        project.is_active = True
        project.save()
        other_projects = Project.objects.filter(author=project.author).exclude(id=project.id)
        for project in other_projects:
            project.is_active = False
            project.save()
        return self
        
    def deactivate_all_projects_but_one_with_given_id(self, project_id):
        projects_to_deactivate = Project.objects.exclude(id=project_id)
        project_to_activate = Project.objects.get(id=project_id)
        if project_to_activate:
            project_to_activate.is_active = True
            project_to_activate.save()
        for project in projects_to_deactivate:
            project.is_active = False
            project.save()

    def get_homepage(self):
        try:
            return Homepage.objects.get(project_id=self.project.id)
        except Homepage.DoesNotExist:
            return None

    def get_custom_subpages(self):
        return Subpage.object.filter(project_id=self.project.id)
    
    def get_active_subpages(self):
        return Subpage.objects.exclude(is_active=False).filter(project_id=self.project.id)

    def get_all_subpages(self):
        return Subpage.objects.filter(project_id=self.project.id)

    def get_active_blog_posts(self):
        return BlogPost.objects.exclude(is_active=False).filter(project_id=self.project.id)

    def get_all_blog_posts(self):
        return BlogPost.objects.order_by('created').filter(project_id=self.project.id)

    def get_site_setting(self):
        try:
            return SiteSettings.objects.get(project_id=self.project.id)
        except SiteSettings.DoesNotExist:
            return None

    def get_active_slides(self):
        return Carousel.objects.exclude(is_active=False).filter(project_id=self.project.id)

    def get_all_slides(self):
        return Carousel.objects.filter(project_id=self.project.id)

    def get_contact_page(self):
        try:
            return ContactPage.objects.get(project_id=self.project.id)
        except ContactPage.DoesNotExist:
            return None

    def get_active_multilanguage(self):
        return Multilanguage.objects.exclude(multilanguage_marker=False).filter(project_id=self.project.id)

    def get_all_multilanguage(self):
        return Multilanguage.objects.filter(project_id=self.project.id)

    def get_social_media(self):
        try:
            return SocialMedia.objects.get(project_id=self.project.id)
        except SocialMedia.DoesNotExist:
            return None
