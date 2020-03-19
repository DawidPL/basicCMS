from django.test import LiveServerTestCase
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_check_homepage_basic_information(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn ('Twoja strona', self.browser.title)

        header_exist = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('Nagłówek strony', header_exist)

        meta_data = self.browser.find_elements_by_tag_name('meta')
        self.assertTrue(any(m.get_attribute('content') == 'meta title' for m in meta_data))
        self.assertTrue(any(m.get_attribute('content') == 'meta description' for m in meta_data))

        

https://readthedocs.org/projects/django-dynamic-fixture/
https://github.com/getsentry/pytest-responses

https://pytest-django-testing.readthedocs.io/pl/latest/page/django/