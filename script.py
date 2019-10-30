import re
import os
import sys

threshold  = 1000000

TOTAL = 0
RESPONSE_SUM = 0

SLOWER_THAN_1000_MS = 0
SLOWER_THAN_500_MS = 0
SLOWER_THAN_100_MS = 0

###
def get_next_log_lines(file_buffer):
	
	follow = sys.argv[1]
	
	global TOTAL
	global RESPONSE_SUM
	global SLOWER_THAN_1000_MS
	global SLOWER_THAN_500_MS
	global SLOWER_THAN_100_MS
	global FILE_LENGTH
	global threshold
	
	while 1:
		
		if TOTAL == FILE_LENGTH and follow != "follow":
			break;
		
		next_line = file_buffer.readline()
		
		if next_line: 
			TOTAL = TOTAL + 1
			
			match_result = re.match('.*\s(\d+)$', next_line)
			
			if match_result:
				microsecs = float(match_result.group(1))
				millisecs = microsecs/1000
				
				if millisecs < 100:
					SLOWER_THAN_100_MS = SLOWER_THAN_100_MS + 1
				elif millisecs < 500:
					SLOWER_THAN_500_MS = SLOWER_THAN_500_MS + 1
				elif millisecs < 1000:
					SLOWER_THAN_1000_MS = SLOWER_THAN_1000_MS + 1
				
				RESPONSE_SUM = RESPONSE_SUM + millisecs
				
				if microsecs > threshold:
					print microsecs
	
###

#file_buffer = open("./access.log")
file_buffer = open("/var/log/apache2/access.log")

FILE_LENGTH = len(file_buffer.readlines())
file_buffer.seek(0)

current_line = 0

get_next_log_lines(file_buffer)

file_buffer.close()

print "Slower than 100ms: " + str(SLOWER_THAN_100_MS)
print "Slower than 500ms: " + str(SLOWER_THAN_500_MS)
print "Slower than 1s: " + str(SLOWER_THAN_1000_MS)
print "Average (ms) = " + str(RESPONSE_SUM / TOTAL)
