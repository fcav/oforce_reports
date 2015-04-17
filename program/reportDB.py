import sqlite3

class reportDB():
	def __init__(self):
		conn = sqlite3.connect("../reports.db")
		self.c = conn.cursor()
		self.initTables()

	def initTables(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS inputData
                     (Account text, Date text, Device text, 
                     	Campaign text, Clicks int, Impressions int, 
                     	Cost real, Conversions int)''')

		self.c.execute('''CREATE TABLE IF NOT EXISTS mapping
                     (Account text, Campaign text, CountryCode text, 
                     	Subregion text, Region text, Brand text, 
                     	Tier text, Product text, Network text )''')


