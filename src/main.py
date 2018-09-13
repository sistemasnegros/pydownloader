# -*- coding: utf-8 -*-

import logging


# load file config .cfg
from lib_sysblack.lib_config import load_config
from lib_sysblack.lib_csv import parser_cvs


from constans import NAME_FILE_LOG_PATH, NAME_FILE_CONFIG_PATH, NAME_FILE_CSV_PATH


from generic import GenericConfig
from downloader import Downloader
from report import Report


class Main(GenericConfig):
    """docstring for Main"""

    def __init__(self):
        super(Main, self).__init__(load_config, NAME_FILE_CONFIG_PATH, NAME_FILE_LOG_PATH, NAME_FILE_CSV_PATH)

        self.loading_args()
        self.log_configuration()

        # General variable
        self.config = self.loading_file_config()
        self.errors = []
        self.fields_csv = self.config.get("GENERAL", "fields_csv").split(",")

        list_links = parser_cvs(self.args.csv, self.fields_csv)

        http = Downloader()

        report = Report()

        for data in list_links:

            download = http.download(data["link"])

            report.add_elements(download)

        report.print_report()

        logging.info("Script Completado.")


if __name__ == '__main__':
    Main()
