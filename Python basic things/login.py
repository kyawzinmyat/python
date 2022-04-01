password = input("Pleaser enter the password u want to set")
print("password set successfully")


i = 0
while i<7:
	user_pass = input("Please enter password")
	if user_pass == password:
		print("log in successfully")
		break
	else:
		print("wrong password")
		i+=1
	