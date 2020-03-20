from django.core.mail import send_mail
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .forms import ContactForm
from .models import BlogPost, Subpage
from .repository.models_repository import ModelsRepository


class ContentMixin(object):
    models_repository = None

    def __init__(self):
        self.models_repository = ModelsRepository()

    def get_context_data(self, requests, *args, **kwargs):
        homepage = self.models_repository.get_homepage()
        site_settings = self.models_repository.get_site_setting()
        subpage_sorted = self.models_repository.get_active_subpages()
        social_media = self.models_repository.get_social_media()
        multilanguage = self.models_repository.get_active_multilanguage()

        if homepage:
            carousel = homepage.carousel
            boxes = homepage.boxes
        else:
            carousel = boxes = None

        context = {
            'carousel': carousel,
            'multilanguage': multilanguage,
            'site_settings': site_settings,
            'homepage': homepage,
            'boxes': boxes,
            'subpage_sorted': subpage_sorted,
            'social_media': social_media,
            'recaptcha': settings.GOOGLE_RECAPTCHA
        }
        return context


class IndexView(ContentMixin, View):

    def get(self, request):
        context = self.get_context_data(request)

        return render(request, 'home.html', context)


class BlogView(ContentMixin, View):

    def get(self, request):
        context = self.get_context_data(request)
        blog = self.models_repository.get_active_blog_posts()

        context['blog'] = blog

        return render(request, 'blog.html', context)


class SinglePostView(ContentMixin, ContactForm, View):

    def get(self, request, slug):

        template_name = 'single_post.html'
        post = get_object_or_404(BlogPost, slug=slug)
        context = self.get_context_data(request)

        context['post'] = post

        if post.is_active:
            return render(request, template_name, context)
        else:
            return render(request, '404.html')


class ContactView(ContentMixin, View):
    template_name = 'contact.html'

    def get(self, request):
        form = ContactForm()
        contact = self.models_repository.get_contact_page()
        context = self.get_context_data(request)
        context['form'] = form
        context['contact'] = contact

        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_lastname = form.cleaned_data['lastname']
            form_email = form.cleaned_data['email']
            form_tel = form.cleaned_data['tel']
            form_message = form.cleaned_data['message']

            form_header = f'Otrzymałeś wiadomość od {form_name} {form_lastname}'
            formatted_message = (
                f'Treść wiadomości:\n {form_message} \n '
                f'\n Dane adresata:\n'
                f'\n Imię i Nazwysko {form_name} {form_lastname}\n'
                f'telefon: {form_tel} \n'
                f'email: {form_email}'
            )
            send_mail(form_header, formatted_message,
                      form_email, [settings.DEFAULT_EMAIL_ADRESS],
                      fail_silently=False)

            return render(request, self.template_name, {'form': form})
        form = ContactForm
        return render(request, self.template_name, {'form': form})


class SubpageView(ContentMixin, View):

    def get(self, request, slug):

        template_name = 'subpage.html'
        unique_subpage = get_object_or_404(Subpage, slug=slug)

        context = self.get_context_data(request)
        context['unique_subpage'] = unique_subpage

        if unique_subpage or unique_subpage.slug == 'admin':
            return render(request, template_name, context)
        else:
            return render(request, '404.html', context)
