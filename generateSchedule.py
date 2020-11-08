import input.py
# not sure how inputs are being handled in input.py

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

	
def calcPriorities(tasks, daysLeft, hoursNeeded):

	ratio = [i / j for i, j in zip(daysLeft, hoursNeeded)]
	sortedRatio = ratio.sorted(reverse=True)

	orderedTasks = []

	for i in range(len(ratio)):
		for j in range(len(sortedRatio)):
			if ratio[i] == sortedRatio[j]:
				orderedTasks.append(task[j])
	return orderedTasks


if__name__== " main ":
	main()
