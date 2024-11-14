from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('Log Report')
		tv = Treeview(self._root)
		tv.pack()
		tv.heading('#0', text='Number')
		tv.configure(column=('#Name', '#Done', '#Comment'))
		tv.heading('#Name', text='Task')
		tv.heading('#Done', text='Done')
		tv.heading('#Comment', text='Comment')
		cursor = self._dbconnect.ListRequest()
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#Done',row['Done'])
			tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])
			
