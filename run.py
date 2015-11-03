### BEGIN LICENSE
# The MIT License (MIT)
#
# Copyright (C) 2015 Christopher Wells <cwellsny@nycap.rr.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END LICENSE
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
