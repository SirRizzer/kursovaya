from django.test import TestCase

from kursovaya.api import GetMaximumMark


class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class StatisticTest(TestCase):
    def test_get_min_mark(self):
        content = [
            ['subject', 'mark1', 'mark2'],
            ['sub1', '61', '78'],
            ['sub2', '90', '92']
        ]
        min_mark_cmd = GetMinimumMark()
        min_mark = min_mark_cmd.execute(content)
        self.assertEqual(min_mark, 'sub1, 61.0, sub2, 90.0')

    def test_get_max_mark(self):
        content = [
            ['subject', 'mark1', 'mark2'],
            ['sub1', '61', '78'],
            ['sub2', '90', '92']
        ]
        max_mark_cmd = GetMaximumMark()
        max_mark = max_mark_cmd.execute(content)
        self.assertEqual(max_mark, 'sub1, 78.0, sub2, 92.0')
