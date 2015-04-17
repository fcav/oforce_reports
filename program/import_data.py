import sqlite3
import xlrd

class Report():
    def __init__(self, report_name):
        self.path = '../reports/{0}.xlsx'.format(report_name)
        self.skip_rows = 5
        
    def import_into_dict(self):
        list_rows = []
        try:
            workbook = xlrd.open_workbook(self.path )
        except:
            print('Cannot open file: {0}'.format(self.path))
            return None
        sheet = workbook.sheet_by_index(0)
        headers = sheet.row_values(self.skip_rows)
        headers = [x.replace(' ', '_') for x in headers]
        for rownum in range(self.skip_rows + 1, sheet.nrows):
            row_vals = sheet.row_values(rownum)
            #excel often returns blank rows - skip them
            if any(map(lambda x: x != '', row_vals)):
                row = dict(zip(headers, sheet.row_values(rownum)))
                if row['Account'] != 'Total':
                    list_rows.append(row)
        return list_rows
    
    def upload_report(self, list_rows):        
        con = sqlite3.connect("../reports.db")
        cur = con.cursor()
        cur.execute("TRUNCATE TABLE inputData;")
        
        for r in list_rows:
            headers = r.keys()
            values = ['"{0}"'.format(str(r[key])) for key in headers]
            cur.execute("INSERT INTO inputData ({0}) VALUES ({1});".format(','.join(headers), ','.join(values)))
            con.commit()
    
    def process_report(self, mappings):
        pass
    
    
    
if __name__ == '__main__':
    reports_to_be_done = ['adwords', 'apps', 'other']
    for report in reports_to_be_done:
        r = Report(report)
        list_rows = r.import_into_dict()
        if list_rows:
            r.upload_report(list_rows)
    