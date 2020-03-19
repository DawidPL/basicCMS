import unittest
import pytest
from django.db.models import QuerySet
from pages.repository.models_repository import ModelsRepository
from pages.models import Project, Homepage, Subpage, BlogPost, SiteSettings


@pytest.mark.django_db
class ModelsRepositoryTest(unittest.TestCase):

    def test_repository_return_none_when_no_model_instance_is_found_in_database(self):
        repository = ModelsRepository()

        def query_set_asserts(query_set):
            self.assertIsInstance(query_set, QuerySet)
            self.assertTrue(len(query_set) == 0)

        query_set_asserts(repository.get_all_blog_posts())
        query_set_asserts(repository.get_active_blog_posts())
        query_set_asserts(repository.get_all_subpages())
        query_set_asserts(repository.get_active_subpages())
        query_set_asserts(repository.get_all_multilanguage())
        query_set_asserts(repository.get_active_multilanguage())
        query_set_asserts(repository.get_all_slides())
        query_set_asserts(repository.get_active_slides())
        self.assertIsNone(repository.get_homepage())
        self.assertIsNone(repository.get_site_setting())
        self.assertIsNone(repository.get_contact_page())
        self.assertIsNone(repository.get_social_media())

    def test_init_creates_default_project_when_no_projects_are_available(self):
        repository = ModelsRepository()
        project_id = repository.get_project().id
        project = Project.objects.get(id=project_id)

        self.assertEquals('default', project.author)
        self.assertEquals('default_project_1', project.title)

    def test_set_project(self):
        repository = ModelsRepository()
        new_project = Project.objects.create()
        initial_project = repository.get_project()

        repository.set_project(new_project)
        actual = repository.get_project()

        self.assertEqual(new_project, actual)
        self.assertNotEqual(initial_project, actual)

    def test_get_project(self):
        self.populate_database()
        project_id = self.repository.get_project().id
        project = Project.objects.get(id=project_id)

        self.assertEqual('fixture_title', project.title)
        self.assertEqual('fixture_author', project.author)

    def test_get_homepage(self):
        self.populate_database()
        homepage = self.repository.get_homepage()

        self.assertEquals(self.repository.get_project().id, homepage.project.id)
        self.assertEquals(1, homepage.template)
        self.assertEquals('Some content for homepage!', homepage.content)

    def test_get_active_subpages(self):
        self.populate_database()

        active_subpages = self.repository.get_active_subpages()
        self.assertEquals(1, len(active_subpages))
        actual = active_subpages[0]

        self.assertEquals(self.repository.get_project().id, actual.project.id)
        self.assertEquals('active_subpage', actual.title)
        self.assertTrue(actual.is_active)

    def test_get_all_subpages(self):
        self.populate_database()

        subpages = self.repository.get_all_subpages()
        self.assertEquals(2, len(subpages))
        inactive_subpage = subpages[0]
        active_subpage = subpages[1]

        self.assertEquals(self.repository.get_project().id, active_subpage.project.id)
        self.assertEquals(self.repository.get_project().id, inactive_subpage.project.id)
        self.assertEquals('active_subpage', active_subpage.title)
        self.assertTrue(active_subpage.is_active)
        self.assertEquals('inactive_subpage', inactive_subpage.title)
        self.assertFalse(inactive_subpage.is_active)

    def test_get_active_blog_posts(self):
        self.populate_database()

        active_blogposts = self.repository.get_active_blog_posts()
        self.assertEquals(1, len(active_blogposts))
        actual = active_blogposts[0]

        self.assertEquals(self.repository.get_project().id, actual.project.id)
        self.assertTrue(actual.is_active)
        self.assertEquals('active_blogpost', actual.title)

    def test_get_all_blog_posts(self):
        self.populate_database()

        blog_posts = self.repository.get_all_blog_posts()
        self.assertEquals(2, len(blog_posts))
        active_blog_post = blog_posts[0]
        inactive_blog_post = blog_posts[1]

        self.assertEquals(self.repository.get_project().id, active_blog_post.project.id)
        self.assertEquals(self.repository.get_project().id, inactive_blog_post.project.id)
        self.assertEquals('active_blogpost', active_blog_post.title)
        self.assertTrue(active_blog_post.is_active)
        self.assertEquals('inactive_blogpost', inactive_blog_post.title)
        self.assertFalse(inactive_blog_post.is_active)

    def test_get_site_setting(self):
        self.populate_database()

        actual = self.repository.get_site_setting()

        self.assertEquals(self.repository.get_project().id, actual.project.id)
        self.assertTrue(actual.is_blog_active)
        self.assertEquals('fixture.com', actual.site_url)

    def test_changing_project(self):
        self.populate_database()
        first_project = self.repository.get_project()
        second_project = Project.objects.get(id=2)

        project_one_subpages = self.repository.get_all_subpages()
        self.repository.set_project(second_project)
        project_two_subpages = self.repository.get_all_subpages()

        self.assertNotEqual(project_one_subpages, project_two_subpages)
        self.assertTrue(len(project_one_subpages) == 2)
        self.assertTrue(len(project_two_subpages) == 1)
        self.assertTrue(project_one_subpages[0].project == first_project)
        self.assertTrue(project_two_subpages[0].project == second_project)

    def populate_database(self):
        project = Project.objects.create(title='fixture_title', author='fixture_author', is_active=True)
        second_project = Project.objects.create(title='second_project_fixture_title',
                                                author='second_project_fixture_author', is_active=False)
        Homepage.objects.create(project=project, template=1, content='Some content for homepage!')
        Subpage.objects.create(is_active=False, title='inactive_subpage', project=project,
                               slug='fixture-subpage-inactive')
        Subpage.objects.create(is_active=True, title='active_subpage', project=project, slug='fixture-subpage-active')
        Subpage.objects.create(is_active=True, title='active_subpage_second_project', project=second_project,
                               slug='fixture-subpage-active-second-project')
        BlogPost.objects.create(is_active=True, title='active_blogpost', project=project,
                                slug='fixture-blogpost-active')
        BlogPost.objects.create(is_active=False, title='inactive_blogpost', project=project,
                                slug='fixture-blogpost-inactive')
        SiteSettings.objects.create(project=project, site_url='fixture.com', is_blog_active=True, template=1)
        self.repository = ModelsRepository()


if __name__ == '__main__':
    unittest.main()
