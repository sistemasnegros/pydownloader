# -*- coding: utf-8 -*-


class Report(object):
    """docstring for ClassName"""

    def __init__(self):
        self.report = []

    def add_elements(self, elements):
        self.report.append(elements)

    def sort_elements(self):
        self.report = sorted(self.report, key=lambda download: download.is_success)

    def print_report(self):
        self.sort_elements()
        for download in self.report:

            if not download.error and download.is_success:
                formato = "ALLOW - Code: %s - %s" % (download.code, download.url)
            elif not download.error and not download.is_success:
                formato = "DENY - Code: %s - %s" % (download.code, download.url)
            elif download.error:
                formato = "ERROR - %s - %s" % (download.url, download.error)

            print formato
