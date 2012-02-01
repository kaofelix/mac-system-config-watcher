#!/usr/bin/python
import subprocess

SSID_GET="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I | grep ' SSID:' | cut -d ':' -f 2 | tr -d ' '"
WORK_SSIDS=["twdata", "twdata_test"]


def change_location(new_location):
    subprocess.call("growlnotify -n LocationChange "
                    "-m 'Location changed to {}' "
                    "New Network Location".format(new_location),
                    shell=True)
    subprocess.call("scselect {}".format(new_location), shell=True)

def main():
    current_ssid = subprocess.check_output(SSID_GET, shell=True).strip()
    if current_ssid in WORK_SSIDS:
        change_location("ThoughtWorks")
    else:
        change_location("Default")

if __name__ == "__main__":
    main()
