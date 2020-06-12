def my_function():
	print("hello from a function")
my_function()


def my_function(fname):
	print(fname + " Refsnes")

my_function("email")
my_function("tobias")
my_function("linus")



def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k -1)
		print(result)
	else:
		result = 0
	return result
print("\n\nRecurtion example result")
tri_recursion(6)

