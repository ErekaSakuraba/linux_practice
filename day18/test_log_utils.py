import unittest
from day16.log_utils import create_ranking

class TestCreateRanking(unittest.TestCase):
    def test_create_ranking(self):
        error_count = {
            "Camera": 5,
            "Database": 5,
            "Network": 3
        }

        expected = [
            ("Camera", 5),
            ("Database", 5),
            ("Network", 3)
        ]

        self.assertEqual(create_ranking(error_count), expected)

    def test_create_ranking_single_item(self):
        error_count = {"Camera": 5}
        expected = [("Camera", 5)]
        self.assertEqual(create_ranking(error_count), expected)

    def test_create_ranking_same_count(self):
        error_count = {
            "Camera": 5,
            "Database": 5,
            "Network": 3
        }

        ranking = create_ranking(error_count)

        self.assertEqual(ranking[0][1], 5)
        self.assertEqual(ranking[1][1], 5)
        self.assertEqual(ranking[2][1], 3)

    def test_create_ranking_empty(self):
        error_count = {}
        expected = []
        self.assertEqual(create_ranking(error_count), expected)