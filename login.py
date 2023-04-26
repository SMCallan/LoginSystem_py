#Login system. 

#Open file. And prempt the login protocol. 
with open("login_system.txt", "r") as login_system_file:
	user_credentials = login_system_file.read().split("\n")

#Conversion to dictionary. 
username_login_password = {}
for i in user_credentials:
	name, password = i.split(";")
	username_login_password[name] = password
	
#The user is prompted to enter or create login details.
validating_login = False
while not validating_login:
	
	print("Login")
	users_account_name = input("USERNAME: ")
	users_account_password = input("PASSWORD: ")
	if users_account_name not in username_login_password.keys():
		print("Invalid login credential")
		continue
	elif username_login_password[users_account_name] != users_account_password:
		print("Invalid password credential")
		continue
	else:
		print("Logged in successfully")
		validating_login = True
