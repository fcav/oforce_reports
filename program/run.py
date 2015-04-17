import xlrd

class Report():
    def __init__(self):
        self.path = None
        self.skip_rows = 5 
        
    def set_path(self):
        self.path = '/home/flaminiacavallo/workspace2/getting_biddable_back_on_track/report.xlsx'
        #input('Please paste the path to your report.')
        
    def import_into_dict(self):
        list_rows = []
        workbook = xlrd.open_workbook(self.path )
        sheet = workbook.sheet_by_index(0)
        headers = sheet.row_values(self.skip_rows)
        for rownum in range(self.skip_rows + 1, sheet.nrows):
            row_vals = sheet.row_values(rownum)
            #excel often returns blank rows - skip them
            if any(map(lambda x: x != '', row_vals)):
                row = dict(zip(headers, sheet.row_values(rownum)))
                if row['Account'] != 'Total':
                    list_rows.append(row)
        return list_rows
    
    def process_report(self, mappings):
        pass
    
    
    
class Excel_report():
    
    def __init__(self, template):
        self.template = template
        self.report_path = None
        
        
    def copy_template_to_excel(self):
        self.report_path = 'path'
    
    def get_mappings(self):
        pass
    
    def pupulate_report(self, mappings):
        r = Report()
        r.set_path()
        m = self.get_mappings()
        r.process_report(m)
    
    def email_user(self):
        pass
        
    

if __name__ == '__main__':
    r = Report()
    r.set_path()
    list_rows = r.import_into_dict()
    print('done')
    