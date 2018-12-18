import re

a=input("Enter email ID : ")

match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', a)

if match == None:
    print('Email validation failure ..')
else:
    print('Email is in required format.')
