from unittest import TestCase
from src.service_layer.application_service import *
from tests.fake_repository import FakeRepository
from src.service_layer.exceptions import *


class TestPorts(TestCase):
    def setUp(self) -> None:
        self.repository = FakeRepository()
        self.long_url = 'https://www.tier.app/en'

    def test_create_shorten_url_valid(self):
        url_dict = create_shorten_url(self.long_url, self.repository)
        self.assertIsInstance(url_dict, dict)

    def test_create_shorten_url_invalid_double(self):
        with self.assertRaises(UrlAlreadyExists):
            url_dict = create_shorten_url(self.long_url, self.repository)
            url_dict = create_shorten_url(self.long_url, self.repository)
            self.assertIsInstance(url_dict, dict)

    def test_create_shorten_url_invalid_too_short(self):
        with self.assertRaises(UrlTooShort):
            url_dict = create_shorten_url('www', self.repository)
            self.assertIsInstance(url_dict, dict)

    def test_create_shorten_url_invalid_domain(self):
        with self.assertRaises(InvalidDomain):
            url_dict = create_shorten_url('www.google.com', self.repository)
            self.assertIsInstance(url_dict, dict)

    def test_find_url_valid(self):
        url_dict = create_shorten_url(self.long_url, self.repository)
        res_url_dict = find_url(self.long_url, self.repository)
        self.assertDictEqual(url_dict, res_url_dict)

    def test_find_url_invalid(self):
        with self.assertRaises(UrlDoesNotExist):
            res_url_dict = find_url(self.long_url, self.repository)

    def test_visits(self):
        url_dict = create_shorten_url(self.long_url, self.repository)
        visit(self.long_url, self.repository)
        self.assertEqual(list(self.repository.all())[0].visits, 1)
        visit(self.long_url, self.repository)
        self.assertEqual(list(self.repository.all())[0].visits, 2)

    def test_delete_url(self):
        url_dict = create_shorten_url(self.long_url, self.repository)
        res_url_dict = find_url(self.long_url, self.repository)
        self.assertIsNotNone(res_url_dict)
        delete(url_dict['long_url'], self.repository)
        with self.assertRaises(UrlDoesNotExist):
            res_url_dict = find_url(self.long_url, self.repository)
            self.assertDictEqual(url_dict, res_url_dict)

    def tearDown(self) -> None:
        self.repository = None
        self.long_url = None

