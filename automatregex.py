import re


# Matching Multiple Groups with the Pipe
heroRegex = re.compile(r'Batman|Tina Fey')
match_object1 = heroRegex.search('Batman and Tina Fey')
match_object1.group()
print(match_object1.group())

match_object2 = heroRegex.search('Tina Fey and Batman')
match_object2.group()
print(match_object2.group())

# searching for Bat(man|mobile|copter|bat)
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
match_obj = batRegex.search('Batmobile lost a wheel')
match_obj.group()
# print(match_obj.group())
print(match_obj.group(0))
print(match_obj.group(1))


# Optional Matching with the Question Mark
# ? means 0 or 1 instance
bat = re.compile(r'Bat(wo)?man')
m = bat.search('The Adventures of Batman')
m.group()
print(m.group())

m2 = bat.search('The Adventures of Batwoman')
m2.group()
print(m2.group())

# more example
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match1 = phoneRegex.search('My number is 415-555-4242')
match1.group()
print(match1.group())

match2 = phoneRegex.search('My number is 555-4242')
match2.group()
print(match2.group())


# Matching Zero or More with the Star
# * => match 0 or 1 or 2 or 3 etc... more

regex_term = re.compile(r'Bat(wo)*man')
match = regex_term.search('The Adventures of Batman')
match.group()
print(match.group())

matchdos = regex_term.search('The Adventures of Batwoman')
matchdos.group()
print(matchdos.group())

matchtres = regex_term.search('The Adventures of Batwowowowoman')
print(matchtres.group())


# Matching One or More with the Plus
# + => match 1 or more
compile_regex = re.compile(r'Bat(wo)+man')
matchy = compile_regex.search('The Adventures of Batwoman')
matchy.group()
print('line66', matchy.group())

matchy2 = compile_regex.search('The Adventures of Batwowowowoman')
matchy2.group()
print(matchy2.group(), 'line 70')

matchy3 = compile_regex.search('The Adventures of Batman')
print('line 73', matchy3)

matchy3 == None
print('line 74', matchy3)

# Matching Specific Repetitions with Braces
ha_regex = re.compile(r'(Ha){3}')
search = ha_regex.search('HaHaHa')
search.group()
print(search.group(), 'line 82')

search2 = ha_regex.search('Ha')
print(search2.group(), 'line 85')
search2 == None
