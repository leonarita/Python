from datetime import datetime

dmy_str1 = 'Thursday, June 18, 2020'
dmy_str2 = '18/6/20'
dmy_str3 = '18-06-2020'

print(datetime.strptime(dmy_str1, '%A, %B %d, %Y'))
print(datetime.strptime(dmy_str2, '%d/%m/%y'))
print(datetime.strptime(dmy_str3, '%d-%m-%Y'))

