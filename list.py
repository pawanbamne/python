thislist = ["apple", "banana", "cherry", "mango", "greaps"]
for x in thislist:
	print(x)

thislist = ["apple", "banana", "cherry", "mango", "greaps"]
if "apple" in thislist:
	print("apple in list")

thislist = ["apple", "banana", "cherry", "mango", "greaps"]
if "sugercan" in thislist:
	print("yes")
else:
	print("no")

thislist = ["apple", "banana", "cherry", "mango", "greaps"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry", "mango", "greaps"]
thislist.insert(4, "pineaple")
print(thislist)

thislist = ["apple", "banana", "cherry", "mango", "greaps"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry", "mango", "greaps"]
del thislist[2]
print(thislist)

thislist = list(("apple", "mango", "greaps"))
print(thislist)