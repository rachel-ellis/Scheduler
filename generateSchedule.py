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

	orderedTasks = []

	# first prioritize things due today
	for i in range(len(daysLeft)):
		if daysLeft[i] == 1:
			orderedTasks.append(tasks[i])
			tasks.pop(i)
			daysLeft.pop(i)
			hoursNeeded.pop(i)

	ratio = [i / j for i, j in zip(hoursNeeded, daysLeft)]
	sortedRatio = sorted(ratio, reverse=True)
	
	for i in range(len(ratio)):
		for j in range(len(sortedRatio)):
			if ratio[i] == sortedRatio[j]:
				orderedTasks.append(task[j])
	return orderedTasks


if__name__== " main ":
	main()
