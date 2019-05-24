from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):

        # resolve() function uses to find method which url is binded
        found = resolve('/')
        self.assertEqual(found.func, home_page)
