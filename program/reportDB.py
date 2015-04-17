import sqlite3

class reportDB():
	def __init__(self):
		conn = sqlite3.connect("../reports.db")
		self.c = conn.cursor()
		self.initTables()

	def initTables(self):
		self.c.execute('''CREATE TABLE IF NOT EXISTS inputData
                     (Account text, Day text, Device text, Campaign text, Clicks int, Impressions int, Cost real, Converted_clicks real);''')

		self.c.execute('''CREATE TABLE IF NOT EXISTS mapping
                     (Account text, Campaign text, Country text, Country_Code_For_Report text, 
                     	Subregion text, Region text, Brand text, 
                     	Tier text, Product text, Network text );''')


a = reportDB()
print('Script finished.')
