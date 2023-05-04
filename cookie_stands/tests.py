from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand

class CookieStandTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', email='test@gmail.com', password='pass')
        testuser1.save()

        test_cookie_stand = CookieStand.objects.create(
            id = 12345,
            location = 'Cookie Stand location',
            owner = testuser1,
            description = 'Cookie Stand description',
            hourly_sales = [80],
            minimum_customers_per_hour = 2,
            maximum_customers_per_hour = 10,
            average_cookies_per_sale = 3.5,
        )
        test_cookie_stand.save()

    def test_cookie_stand_content(self):
        cookie_stand = CookieStand.objects.get(id=12345)
        actual_location = str(cookie_stand.location)
        actual_description = str(cookie_stand.description)
        actual_min_cust = str(cookie_stand.minimum_customers_per_hour)

        self.assertEqual(actual_location, 'Cookie Stand location')
        self.assertEqual(actual_description, 'Cookie Stand description')
        self.assertEqual(actual_min_cust, '2')
