import sqlite3
import itertools
import datetime as dt

class reportDB():
	def __init__(self):
		conn = sqlite3.connect("../reports.db",timeout=1)
		conn.row_factory=sqlite3.Row
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


	def fetchReport(self):
		resultsDict = []
		CurrentWeek = dt.datetime.now().isocalendar()[1]
		for row in self.c.execute('''SELECT * FROM inputData JOIN mapping USING (Account,Campaign) '''):
			rowDict = dict(itertools.izip(row.keys(),row))
			try:
				date = dt.datetime.strptime(rowDict['Date'],"%d/%m/%Y")
			except ValueError:
				continue

			rowDict['Quarter'] = 1+(date.month-1)/3
			rowDict['Month'] = date.month
			rowDict['Week'] = date.isocalendar()[1]
			rowDict['CurrentWeek'] = CurrentWeek

			resultsDict.append(rowDict)

		return resultsDict
			
