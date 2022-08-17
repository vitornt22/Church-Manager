from django.test import TestCase
from django.urls import resolve, reverse


class AccountUrlTest(TestCase):
    def test_account_login_url_is_correct(self):
        login_url = reverse('account:login')
        self.assertEquals(login_url, '/')

    def test_account_index_url_is_correct(self):
        index_url = reverse('account:index')
        self.assertEquals(index_url, '/Estatisticas')

    def test_account_profile_url_is_correct(self):
        index_url = reverse('account:profile')
        self.assertEquals(index_url, '/Igreja')

    def test_account_logout_url_is_correct(self):
        index_url = reverse('account:logout')
        self.assertEquals(index_url, '/logout')
