from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from pages.models import Project


class ProjectActionsTest(TestCase):

    def setUp(self):
        self.username = 'admin'
        self.password = 'admin'
        self.user = User.objects.create_superuser(self.username, 'test@test.com', self.password)

    def test_activate_action_activates_chosen_project(self):
        project_one = Project.objects.create()
        project_two = Project.objects.create()
        login_response = self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('admin:pages_project_changelist'),
                                    {'action': 'activate', '_selected_action': [project_one.id]}, follow=True)

        assert login_response == True
        assert response.status_code == 200

        project_one_after_action = Project.objects.filter(id=project_one.id)[0]
        project_two_after_action = Project.objects.filter(id=project_two.id)[0]

        assert project_one_after_action.is_active == True
        assert project_two_after_action.is_active == False

    def test_activate_action_activates_first_project_if_more_than_one_were_selected(self):
        project_one = Project.objects.create()
        project_two = Project.objects.create()
        project_three = Project.objects.create()
        login_response = self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('admin:pages_project_changelist'),
                                    {'action': 'activate', '_selected_action': [project_two.id, project_three.id]},
                                    follow=True)

        assert login_response == True
        assert response.status_code == 200

        project_one_after_action = Project.objects.filter(id=project_one.id)[0]
        project_two_after_action = Project.objects.filter(id=project_two.id)[0]
        project_three_after_action = Project.objects.filter(id=project_three.id)[0]

        assert project_one_after_action.is_active == False
        assert project_two_after_action.is_active == False
        assert project_three_after_action.is_active == True

    def tearDown(self) -> None:
        self.client.logout()
