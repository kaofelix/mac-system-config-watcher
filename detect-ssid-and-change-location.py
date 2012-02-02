#!/usr/bin/python
import sys
import subprocess
import re
from functools import partial

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.handlers.SysLogHandler())

SSID_GET=("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/"
          "airport -I | grep ' SSID:' | cut -d ':' -f 2 | tr -d ' '")
WORK_SSIDS=["twdata", "twdata_test"]

shell = partial(subprocess.call, shell=True)
shell_out = partial(subprocess.check_output, shell=True)

location_regexp = re.compile(" [*] [-A-Z0-9]+\t\((.+)\)")

def current_location():
    location_list = shell_out("scselect")
    return location_regexp.search(location_list).group(1)

def change_location(new_location):
    if new_location == current_location():
        logger.info("Current location is already {}".format(new_location))
        return
    
    if shell("scselect {}".format(new_location)) == 0:
        location_changed_msg = 'Location changed to {}'.format(new_location)
        logger.info(location_changed_msg)
        shell("growlnotify -n LocationChange "
              "-m '{}' "
              "New Network Location".format(location_changed_msg))
    else:
        logger.warning("Error changing network location to {}".format(new_location))

def main():
    current_ssid = shell_out(SSID_GET).strip()
    if current_ssid in WORK_SSIDS:
        change_location("ThoughtWorks")
    else:
        change_location("Default")

if __name__ == "__main__":
    main()
