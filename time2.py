str_time = int(input("What time is it now?")) # added the int in order for them to input a variable
str_wait_time = int(input("What is the number of hours to wait?")) #added the int in order to add a variable
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = (time + wai_time) # added () and we also fixed the text error as well
print(time_when_alarm_go_off)
