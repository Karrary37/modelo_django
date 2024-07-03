from django.test import TestCase
from core.tasks import celery_teste


class CeleryTestCase(TestCase):

    def test_celery_teste(self):
        test_id = 123
        result = celery_teste(test_id)
        self.assertEqual(result, test_id)
