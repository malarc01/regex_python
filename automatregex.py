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
# print(search2.group(), 'line 85')
# search2 == None

# Greedy and Non-greedy Matching
# Python’s regular expressions are greedy by default

greedy_regex = re.compile(r'(Ha){3,5}')
mat = greedy_regex.search('HaHaHaHaHa')
mat.group()
print(mat.group(), 'line94')

not_greedy = re.compile(r'(Ha){3,5}?')
mat2 = not_greedy.search('HaHaHaHaHa')
mat2.group()
print(mat2.group(), 'line99')


# The findall() Method

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
search_string = phone_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
search_string.group()
print('line 107', search_string.group())
print(phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# with groups
fone_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups ()
fone_regex.findall('Cell:415-555-9999')
print('line 113', fone_regex.findall('Cell:415-555-9999'))

# Character Classes
# + =>
# match 1 or more digital then space then word 1 or more
xmas_regex = re.compile(r'\d+\s\w+')
xmas_regex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print('line 120', xmas_regex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))


# Making Your Own Character Classes
vowel_regex = re.compile(r'[aeiouAEIOU]')
vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
print('line 128', vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

consonant_regex_search = re.compile(r'[^aeiouAEIOU]')
consonant_regex_search.findall('RoboCop eats baby food. BABY FOOD.')
print('line 132', consonant_regex_search.findall(
    'RoboCop eats baby food. BABY FOOD.'))


# The Caret and Dollar Sign Characters
hello_search = re.compile(r'^Hello')
hello_search.search('Hello,world!')
print('line139', hello_search.search('Hello,world!'))
print('line 140', hello_search.search('He said hello.') == None)

# testing r'\d$'
ends_with_number = re.compile(r'\d$')
ends_with_number.search('Your number is 42')
print('line 145', ends_with_number.search('Your number is 42 '))
print('line 146', ends_with_number.search('Your number is 42'))
print(ends_with_number.search('Your number is forty two.') == None)

# tesing r'^\d+$' matches string that both begin + end with one or more numbers
whole_string_is_number = re.compile(r'^\d+$')
whole_string_is_number.search('1234567890')
print('line 152', whole_string_is_number.search('1234567890'))
print('line 153', whole_string_is_number.search('12345xyz67890'))
print('line 154', whole_string_is_number.search('12  34567890'))
# “Carrots cost dollars”

# The Wildcard Character
regex = re.compile(r'.at')
regex.findall('The cat in the hat sat on the flat mat')
print('line 160', regex.findall('The cat in the hat sat on the flat mat'))


# Matching Everything with Dot-Star
# * => match 0 or more 0 or 1 or 2 or 3 etc.
name = re.compile(r'First Name:(.*)Last Name:(.*)')
result = name.search('First Name: Al Last Name: Sweigart')
print('line 167', result.group())
print('should print Al Sweigart ', result.group(0))
print('should print Al', result.group(1))
print('should print Sweigart', result.group(2))

# .* uses greedy mode means start with most text as possible
# .*? is for non greedy mode.

no_greed = re.compile(r'<.*?>')
nogreed_search = no_greed.search('<To serve man> for dinner.>')
print(nogreed_search.group())

greed_regex = re.compile(r'<.*>')
obj = greed_regex.search('<To serve man> for dinner.>')
print('probably returns whole setenece?', obj.group())


# Matching Newlines with the Dot Character
# .* The dot-star will match everything except a newline
no_newline_regex = re.compile('.*')
print('line 187', no_newline_regex.search(
    'Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.

new_line_regex = re.compile('.*', re.DOTALL)
print('line 192', new_line_regex.search(
    'Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# Case-Insensitive Matching
reg1 = re.compile('RoboCop')
reg2 = re.compile('ROBOCOP')
reg3 = re.compile('robOcop')
reg4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.IGNORECASE)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())


print(robocop.search('ROBOCOP protects the innocent.').group())


print(robocop.search(
    'Al, why does your programming book talk about robocop so much?').group())


# Substituting Strings with the sub() Method
# + => 1 or more
# sub(arg1,arg2) arg1 = is string to replace any matches
# arg2 => string for regular expression
name_regex = re.compile(r'Agent \w+')
name_regex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(name_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# using the matched text itself as part of the substitution
agent_name_regex = re.compile(r'Agent (\w)\w*')
agent_name_regex.sub(
    r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

print(agent_name_regex.sub(r'\1****',
                           'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
print('line 229 group(1)', agent_name_regex.search(
    'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.').group(1))
print('line 230 group(0)', agent_name_regex.search(
    'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.').group(0))


# Managing Complex Regexes
verbose_regex = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

verbose_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL)

some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# Project: Phone Number and Email Address Extractor
