# This is our main script
from models import User, JournalEntry
from datetime import datetime

def make_entry(user, content):
	entry = JournalEntry.create(content=content, author=user, 
								timestamp=datetime.now())

	if entry == 1:
		print("Entry Saved Successfully!\n")

def get_all_entries(user):
	entries = JournalEntry.select().where(JournalEntry.author == user)

	print("-"*20)
	for entry in entries:
		print(entry.id, entry.timestamp, entry.content[:20], "...")
	print("-"*20)


def get_entry_by_id(id):
	entry = JournalEntry.select().where(JournalEntry.id == id).get()
	print("-"*20)
	print(entry.content)
	print("-"*20)


def login():
	username = input("Enter Username --> ")
	password = input("Enter Password --> ")

	user = User.select().where(User.username == username)

	if not user.exists():
		print("Incorrect Credentials.\n")
		return 0

	if user.get().password == password:
		print("Logged in succesfully.\n")
		return user.get()
	else:
		print("Incorrect Password.\n")
		return 0

def register():
	username = input("Enter Username --> ")

	user = User.select().where(User.username == username)

	if user.exists():
		print("User exists.")
		username = input("Enter New Username --> ")

	fullname = input("Enter FullName --> ")
	password = input("Enter Password --> ")

	new_user = User.create(full_name = fullname, 
		username=username, password=password)

	print("User Created Successfully!")