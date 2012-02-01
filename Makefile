install:
	cp org.kaofelix.SystemConfigChange.plist ~/Library/LaunchAgents/
	cp detect-ssid-and-change-location.py ~/bin
	chmod +x ~/bin/detect-ssid-and-change-location.py
	launchctl load ~/Library/LaunchAgents/org.kaofelix.SystemConfigChange.plist
uninstall:	
	launchctl unload ~/Library/LaunchAgents/org.kaofelix.SystemConfigChange.plist
	rm ~/Library/LaunchAgents/org.kaofelix.SystemConfigChange.plist
	rm ~/bin/detect-ssid-and-change-location.py

reinstall: uninstall install
