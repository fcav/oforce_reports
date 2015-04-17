import os
import shutil


template_dir = '../templates'
output_dir = '../output'

reports = ['adwords', 'apps', 'other']

for report in reports:
    src = os.path.join(template_dir, report)