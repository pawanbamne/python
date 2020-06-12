import datetime

x = datetime.datetime.now()

print(x)


import datetime
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

print("\n")
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%%"))
print(x.strftime("%X"))
print(x.strftime("%x"))
print(x.strftime("%c"))
print(x.strftime("%W"))
print(x.strftime("%U"))
print(x.strftime("%j"))
print(x.strftime("%Z"))
print(x.strftime("%z"))
print(x.strftime("%f"))
print(x.strftime("%S"))
print(x.strftime("%M"))
print(x.strftime("%p"))
print(x.strftime("%I"))
print(x.strftime("%H"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%m"))
print(x.strftime("%B"))