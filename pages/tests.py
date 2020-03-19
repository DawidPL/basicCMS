from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import index
from .models import SiteSettings

class HomePageTest(TestCase):


    def test_uses_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_display_all_site_settings_objects(self):
        SiteSettings.objects.create(meta_title='meta title', meta_description=' meta_description',
                                    meta_title_blog='meta title blog')

        response = self.client.get('/')
        response_blog = self.client.get('/blog')

        self.assertIn('meta title', response.content.decode()) 
        self.assertIn('meta_description', response.content.decode())
        self.assertIn('meta title blog', response_blog.content.decode())

class SiteSettingsTest(TestCase):

    def test_saving_object(self):
        obj_first = SiteSettings()
        obj_first.save()
        obj_second = SiteSettings()
        obj_second.save()

        saved_objects = SiteSettings.objects.all()
        self.assertEqual(saved_objects.count(), 2)

    def test_retriving_object(self):
        obj = SiteSettings()
        obj.site_url = 'localhost:8000'
        obj.meta_title = 'meta title'
        obj.meta_description = 'meta description'
        obj.meta_title_blog = 'meta title blog'
        obj.meta_description_blog = 'meta description blog'
        obj.logo_text = 'Logo'
        obj.save()

        saved_object = SiteSettings.objects.first()
        obj_saved = saved_object

        self.assertEqual(obj_saved.site_url, 'localhost:8000')
        self.assertEqual(obj_saved.meta_title, 'meta title')
        self.assertEqual(obj_saved.meta_description, 'meta description')
        self.assertEqual(obj_saved.meta_title_blog, 'meta title blog')
        self.assertEqual(obj_saved.meta_description_blog, 'meta description blog')
        self.assertEqual(obj_saved.logo_text, 'Logo')

