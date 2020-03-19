from django.urls import reverse, resolve
import pytest


class TestUrls:

    '''
    All fixtures are in conftest.py

    '''

    @pytest.mark.parametrize('name', ['index', 'contact', 'blog'])
    def test_if_url_path_is_correct(self, name):
        path = reverse(name)
        assert resolve(path).view_name == name

    def test_if_url_single_blog_path_with_slug_is_correct(self, slug_list):
        path = reverse('single_blog', kwargs=slug_list)
        assert resolve(path).view_name == 'single_blog'

    def test_if_url_subpage_path_is_correct(self, slug_list):
        path = reverse('generated_page', kwargs=slug_list)
        assert resolve(path).view_name == 'generated_page'
