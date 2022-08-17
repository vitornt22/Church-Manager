from account import views
from django.test import TestCase
from django.urls import resolve, reverse


class AccountViewsTest(TestCase):

    def test_account_index_views_function_is_correct(self):
        view = resolve(reverse('account:index'))
        self.assertIs(view.func, views.index)

    def test_account_profile_views_function_is_correct(self):
        view = resolve(reverse('account:profile'))
        self.assertIs(view.func, views.profile)

    def test_account_logout_views_function_is_correct(self):
        view = resolve(reverse('account:logout'))
        self.assertIs(view.func, views.logout_view)

    def test_account_login_views_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.login_view)

    def test_account_login_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)

    def test_account_login_view_load_corrects_templates(self):
        response = self.client.get(reverse('account:login'))
        self.assertTemplateUsed(response, 'index.html')
