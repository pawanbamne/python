thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
x = thisdict["model"]
print(x)

thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
thisdict["year"]= 2018
print(thisdict)


thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
for x in thisdict:
	print(x)


thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
for x in thisdict:
	print(thisdict[x])


thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
for x in thisdict.values():
	print(x)

print("\n")

thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
for x, y in thisdict.items():
	print(x, y)

print("\n")
thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
if "model" in thisdict:
	print("yes, model is exist")
print("\n")

thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
thisdict.pop("model")
print(thisdict)


thisdict = {
	"brand": "ford",
	"model": "mustang",
	"year": 1994
}
thisdict["color"]= "red"
print(thisdict)