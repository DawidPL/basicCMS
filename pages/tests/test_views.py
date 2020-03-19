from django.test import RequestFactory
from django.urls import reverse
from pages.views import SubpageView

from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestViews:

    def test_if_generated_page_has_proper_slug(self):
        mixer.blend('pages.Subpage', slug='test')
        path = reverse('generated_page', kwargs={'slug': 'test'})
        request = RequestFactory().get(path)
        view = SubpageView()

        response = view.get(request, slug='test')

        assert response.status_code == 200
