import sqlite3
import xlrd

class Mappings():
    def __init__(self, report_name):
        self.path = '../output/{0}.xlsx'.format(report_name)
        self.skip_rows = 0
        
    def import_into_dict(self):
        list_rows = []
        try:
            workbook = xlrd.open_workbook(self.path)
        except:
            print('The file cannot be opened: {0}'.format(self.path))
            return None
        sheet = workbook.sheet_by_index(3)
        headers = sheet.row_values(self.skip_rows)
        headers = [x.replace(' ', '_') for x in headers if x != '' and x != 'Please note: ']
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
        
        for r in list_rows:
            headers = r.keys()
            values = ['"{0}"'.format(str(r[key])) for key in headers]
            cur.execute("INSERT INTO mapping ({0}) SELECT {1} WHERE NOT EXISTS (SELECT 1 FROM mapping WHERE Campaign = '{2}');""".format(','.join(headers), ','.join(values), r['Campaign']))
            cur.execute("UPDATE mapping SET VALUES ({0}) WHERE {1});".format(','.join([h + '=' + r[h] for h in headers if h != 'Campaign']), 'Campaign=' + r['Campaign']))
            con.commit()
                
    
if __name__ == '__main__':
    reports_to_be_done = ['adwords', 'apps', 'other']
    for report in reports_to_be_done:
        m = Mappings(report)
        list_rows = m.import_into_dict()
        if list_rows:
            m.upload_report(list_rows)
    
