install:
	cp org.kaofelix.SystemConfigChange.plist ~/Library/LaunchAgents/
	cp detect-and-trigger.py ~/bin
	chmod +x ~/bin/detect-and-trigger.py
	launchctl load ~/Library/LaunchAgents/org.kaofelix.SystemConfigChange.plist
uninstall:	
	launchctl unload ~/Library/LaunchAgents/org.kaofelix.SystemConfigChange.plist
	rm ~/Library/LaunchAgents/org.kaofelix.SystemConfigChange.plist
	rm ~/bin/detect-and-trigger.py
