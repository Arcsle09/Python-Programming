#Problem Statememt:
#Ask the user for the time now (in hours), and ask for the number of hours to wait. 
#Your program should output what the time will be on the clock when the alarm goes off.

time = int(input("What time it is now?"))

alarm_time = int(input("After how many hours you want the alarm to go off?"))

go_off_time = (alarm_time % 24) + time 

if go_off_time >= 24:
  go_off_time = 0 + (go_off_time - 24)

print("The alarm will go off at",go_off_time)
