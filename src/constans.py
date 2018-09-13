# -*- coding: utf-8 -*-
"""this file have all the constan"""

# allow relative path
from unipath import Path

### Only Const  ###

# Name aplication
NAMEAPP = "pydownloader"

# root folder
PROJECT_DIR = Path(__file__).ancestor(1)

# logs
NAME_FILE_LOG = "%s.log" % (NAMEAPP)
#NAME_FILE_LOG_PATH = PROJECT_DIR.child(NAME_FILE_LOG)
NAME_FILE_LOG_PATH = "./%s" % NAME_FILE_LOG

# config
NAME_FILE_CONFIG = "%s.cfg" % (NAMEAPP)
#NAME_FILE_CONFIG_PATH = PROJECT_DIR.child(NAME_FILE_CONFIG)
NAME_FILE_CONFIG_PATH = "./%s" % (NAME_FILE_CONFIG)

# csv
NAME_FILE_CSV = "%s.csv" % (NAMEAPP)
#NAME_FILE_CSV_PATH = PROJECT_DIR.child(NAME_FILE_CSV)
NAME_FILE_CSV_PATH = "./%s" % (NAME_FILE_CSV)
