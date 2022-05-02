import re



# digits = re.findall('[0-9]+', phrase)
# print(digits)

# nondigits=re.findall('[a-zA-Z]', phrase)
# print(nondigits)

# whitespaces = re.findall('[\s]', phrase)
# print(whitespaces)

# non_whitespaces=re.findall('[\S]', phrase)
# print(non_whitespaces)

# alphanumeric=re.findall('[\w]', phrase)
# print(alphanumeric)

# patterns= ['\W+']
# for p in patterns:
#     match= re.findall(p, phrase)
#     print("NonAlphaNumeric",match)

# hashtag=re.findall('[#]',phrase)
# print(hashtag)

# # (works for alpha numeric numbers)numbers = re.findall('[\d]', phrase)
# # print("Numbers are: ",numbers)


phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'
def multi_re_find(patterns,phrase):
   for pattern in patterns:
        print("searching the phrase using re check:%r"%pattern)
        print(re.findall(pattern,phrase))
        print('\n')

test_patterns=[r'\d+',#digits
               r'\D+',#non-digits
              r'\s+',#white space"
              r'\S+',#non white spae
              r'\w+',#alphanumeric
               r'\W',#non alphanumeric
               ]
multi_re_find(test_patterns,phrase)