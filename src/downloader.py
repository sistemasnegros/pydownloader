# -*- coding: utf-8 -*-

import urllib2

import ssl

from simple_object import SimpleObject


class Downloader(object):
    """docstring for Downloader"""

    def __init__(self):
        super(Downloader, self).__init__()

        self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    def download(self, url):
        download = SimpleObject()
        """method attemt download file and return if is success"""

        req = urllib2.Request(url)

        download.error = None
        download.response = None
        download.is_success = None
        download.code = 0
        download.url = url

        try:
            download.response = urllib2.urlopen(req, context=self.context)
            download.is_success = download.response.getcode() == 200
            download.code = download.response.getcode()

        except urllib2.HTTPError, error:
            #download.error = error
            if error.code == 403:
                download.is_success = False
                download.code = 403

        except Exception as error:
            download.error = error

        return download
