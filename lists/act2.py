# All about Dictionary 
from pprint import pprint
student = {
    'name' : 'Aineesh',
    'grade' : '9th',
    'school_name' : 'Codingal',
    'address' : {
        'pin' : 120120,
        'city' : "Pune",
        'country' : "INDIA"
    }
}

print(student['name'])
print(student['address']['city'])

# Adding new key, value
student['favColor'] = 'Blue'
# pprint(student,sort_dicts=False)

# update
student['favColor'] = 'Green'
# pprint(student,sort_dicts=False)

# pop()
student.pop("favColor")
pprint(student, sort_dicts=False)

# Combine two different list into a dictionary
_ids = ['1001', '1002', '1003', '1004']
names = ["John", "David", "Tim", "Walter"]

"""
   10001 : John
   1002 : David
   1003 : Tim
   1004 : Walter
"""

emp_records = dict(zip(_ids, names))
pprint(emp_records)