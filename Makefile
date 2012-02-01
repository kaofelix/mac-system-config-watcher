PLIST = org.kaofelix.SystemConfigChange.plist
SCRIPT = detect-ssid-and-change-location.py
SCRIPT_PATH = ~/bin
LAUNCH_AGENTS_PATH = ~/Library/LaunchAgents

install:
	cp $(PLIST) $(LAUNCH_AGENTS_PATH)/
	mkdir -p $(SCRIPT_PATH)
	cp $(SCRIPT) $(SCRIPT_PATH)
	chmod +x $(SCRIPT_PATH)/$(SCRIPT)
	launchctl load $(LAUNCH_AGENTS_PATH)/$(PLIST)
uninstall:	
	launchctl unload $(LAUNCH_AGENTS_PATH)/$(PLIST)
	rm $(LAUNCH_AGENTS_PATH)/$(PLIST)
	rm $(SCRIPT_PATH)/$(SCRIPT)
	rmdir $(SCRIPT_PATH) || true

reinstall: uninstall install
