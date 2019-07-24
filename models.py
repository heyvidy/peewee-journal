from peewee import *

db = SqliteDatabase('journal.db')

class User(Model):
	full_name = CharField()
	username = CharField()
	password = CharField()
	
	class Meta:
		database = db # This model uses the "journal.db" database.


class JournalEntry(Model):
	author = ForeignKeyField(User, backref='entries')
	content = TextField()
	timestamp = TimestampField()

	class Meta:
		database = db


if __name__ == "__main__":
	# Run only when models.py is executed
	# WONT run when models.py is imported
	print("I'm in!")
	db.connect()
	db.create_tables([User, JournalEntry])
