# Ryan runs a fruits delivery service.
# He has tie-ups with multiple resellers/distributors to help them deliver their fruits to their end users.
# There is a resellers' conference happening in the next week where multiple resellers will organize their own events on a pre-decided day.
# Each event can vary in time for which it is going on. Ryan sees this as a very good opportunity to add more business to his delivery service. 
# However, the problem is that the event timings can overlap. Due to this Ryan needs to decide how many maximum events he can attend. 
# Each event has a start time and the end time. If the start time of an event is same as the end time of another event then Ryan will 
# not be able to attend both the events (imagine some time taken to commute between the events).
# Input :Locked stub code in the editor reads the following input from stdin and passes event details for each E events as an array 
# argument to the function:The 1st line of input contains an integer E denoting the number events.
# Next E lines, one for each event contains three spaced integers denoting start time ST and end time ET.

# Output:You need to print an integer X, denoting maximum events Ryan can attend.
# Constraints :1<=E<=10000<=ST<ET<=24
# Sample Input:
# 3
# 5 7
# 2 4
# 5 6
# Sample output: 2

# 4
# 4 5
# 3 4
# 5 6
# 2 3
# Sample output: 2
# -
# 11
# 8 10
# 2 3
# 4 5
# 11 12
# 3 4
# 5 6
# 6 7
# 8 9
# 10 11
# 7 8
# 1 4
# Sample output: 5
# Note:Ryan first attends the event (2 4) that goes on from 2 to 4.
# Next, he has an option to attend events (5 7) or (5 6) both resulting in maximum events attended as 2.
# Hence the output is 2.


# def fin_overlapping_events(events_list):
# 	temp = []
# 	for i in events_list:
# 		temp.append(i.split(" "))

# 	print(temp)





# arr = ['4 5', '3 4', '5 6', '2 3']
# fin_overlapping_events(arr)
v
ar = [[4,5],[3,4],[5,6],[2,3]]
var.sort()
lol = [{'start': i[0], 'end': i[1]} for i in var]
print(var)
final = []
j = 1
for i in range(len(var) - 1):
	print(var[i][0], '-------', var[i+1][1])
	print('--------------------')
	if var[i][0] < var[i+1][1]:
		print('--->', var[i])
