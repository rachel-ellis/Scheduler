import test.py
# not sure how inputs are being handled in test.py

from datetime import datetime

def main():
  
  # based on https://www.programiz.com/python-programming/datetime/current-time
	currentTime = datetime.now().strftime('%H:%M')
  
	# for simplicity (for now), only consider full hours
	currentHour = int(currentTime.split(":")[0])
	currentMin = int(currentTime.split(":")[1])

  # round to nearest hour
	if currentMin >= 30:
		currentHour += 1
  currentMin = 0

  
if__name__== " main ":
  main()
