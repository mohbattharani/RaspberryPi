import os, time

temp = os.popen('vcgencmd measure_temp').readline()
print (type(temp))
print (float(temp.split('=')[-1].split("'")[0]))
