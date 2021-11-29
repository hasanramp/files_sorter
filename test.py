import os
from datetime import date


dir_name = '/home/kevin/Downloads'
dir2 = 'AppImages'
filename = 'some.pdf'
path = os.path.join(dir_name, date.today().strftime('%d-%m-%Y'), filename)
print(path)
