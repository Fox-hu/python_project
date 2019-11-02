import re

# phoneNumRe = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
# mo = phoneNumRe.search('my number is 415-555-4242')
# print('phone number found:' + mo.group())

phoneNumRe = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phoneNumRe.search('my number is 415-555-4242')
print("mo group 1 "+mo.group(1))
print("mo group 2 "+mo.group(2))
print("mo group 0 "+mo.group(0))
