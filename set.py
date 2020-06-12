thisset = {"apple", "mango", "banana"}
for x in thisset:
	print(x)


thisset = {"apple", "mango", "banana"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "mango", "banana"}
thisset.update(["orange", "pineapple", "paypaya"])
print(thisset)

thisset = {"apple", "mango", "banana"}
thisset.discard("mango")
print(thisset)

thisset = {"apple", "mango", "banana"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "mango", "banana"}
thisset.clear()
print(thisset)



