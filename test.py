import os
from datetime import date


list1 = ['hasan', 'kaizar', 'hunaid']
list2 = [0, 0, 0, 0]
dict1 = dict(zip(list1, list2))

dict1['hasan'] = dict1['hasan'] + 1
for key in dict1.keys():
    print(key)