#!/usr/bin/python
import subprocess
from functools import partial

SSID_GET="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I | grep ' SSID:' | cut -d ':' -f 2 | tr -d ' '"
WORK_SSIDS=["twdata", "twdata_test"]

shell = partial(subprocess.call, shell=True)
shell_out = partial(subprocess.check_output, shell=True)

def change_location(new_location):
    shell("growlnotify -n LocationChange "
          "-m 'Location changed to {}' "
          "New Network Location".format(new_location))
    shell("scselect {}".format(new_location))

def main():
    current_ssid = shell_out(SSID_GET).strip()
    if current_ssid in WORK_SSIDS:
        change_location("ThoughtWorks")
    else:
        change_location("Default")

if __name__ == "__main__":
    main()
