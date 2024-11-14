#!/usr/bin/python3
import sqlite3
from typing import Literal

class DBConnect:
	def __init__(self):
		self._db = sqlite3.connect('information.db')
		self._db.row_factory = sqlite3.Row
		self._db.execute('create table if not exists Comp(ID integer primary key autoincrement, Name varchar(255), Done varchar(255), Comment text)')
		self._db.commit()
	def Add(self, name, Done, comment) -> Literal['Your Report has been submitted.']:
		self._db.execute('insert into Comp (Name, Done, Comment) values (?,?,?)',(name,Done,comment))
		self._db.commit()
		return 'Your Report has been submitted.'
	def ListRequest(self):
		cursor = self._db.execute('select * from Comp')
		return cursor
