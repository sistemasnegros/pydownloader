# -*- coding: utf-8 -*-

import unittest

from downloader import Downloader


class TestsBasicos(unittest.TestCase):

    def test_download_ssl(self):
        downloader = Downloader()
        download = downloader.download("https://google.com.co")
        self.assertIsInstance(download.is_success, bool)

    def test_download(self):
        downloader = Downloader()
        download = downloader.download("http://google.com.co")
        self.assertIsInstance(download.is_success, bool)

    def test_download_not_exist(self):
        downloader = Downloader()
        download = downloader.download("http://xxxxxxsssxxxxdd.com.co")
        self.assertIsNone(download.response)
