"""A script which runs a server and gets the upload and dowload speeds."""
from subprocess import Popen, PIPE
import time

# Start the server
Popen("python3 -m http.server 8080", shell=True, stdin=PIPE, stdout=PIPE)

# Run the get internet speed command evey x minutes y times
READING_INTERVAL = 5
NUMBER_OF_READINGS = 120
i = 0
while i < NUMBER_OF_READINGS:
	Popen("python3 speedtest_cli.py --csv bandwidth_report.csv", \
		shell=True, stdin=PIPE, stdout=PIPE)
	print "Got time: " + str(READING_INTERVAL * (i + 1))
	time.sleep(READING_INTERVAL * 60)
	i = i + 1
