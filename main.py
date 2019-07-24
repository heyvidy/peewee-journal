from app import *

while True:
	print("\n\n", "-"*20)
	print("Choose an option.\n 1.Create Entries\n 2.Check Entry\n\
		3.Create New Account.")
	choice = input("--> ")

	if choice == "1":
		user = login()
		if user:
			content = input("Write below\n------------------------\n")
			make_entry(user, content)
		else: 
			continue

	elif choice == "2":
		user = login()

		if user:
			get_all_entries(user)
			entry_id = input("Choose an entry by ID --> ")
			get_entry_by_id(entry_id)
		else:
			continue

	elif choice == "3":
		register()
		
	else:
		exit()
