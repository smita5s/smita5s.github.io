list = ["smita", "jhili", "sill"]
enter_input = input("Enter the name you know: ")

if enter_input in list:
    print( " You are in there! {}".format(enter_input))
else:
	print("You are nice guy! {}".format(enter_input))
print ('h')
print (5%2)

def who():
	people = input("enter: ")
	peoplelist = people.split(",").strip()
	return peoplelist
def ask():
	person =  input("enter: ")
	if person in who():
		print ("you know {}".format(person))
ask()
