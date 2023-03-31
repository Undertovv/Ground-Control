#!/usr/bin/python3

from daemon import DaemonContext as daemonise
with daemonise(): #daemonise me daddy
	from main.py import * 
