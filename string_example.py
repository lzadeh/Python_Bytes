# message = 'This is a string variable. I\'m happy.'
# subString1 = message[10:16]
# subString2 = message[10:16:2]
# subString3 = message[-9:-1]
# print(subString1)
# print(subString2)
# print(subString3)

# Sample email content
email_content = '''
Congratulations! You've won a million dollars.
Click here to claim your money.
'''

# Spam keyword
spam_keyword = 'click'

# convert the content to lowercase
email_content_lower = email_content.lower()

print("Email content in lowercaser: " + email_content_lower)

if spam_keyword in email_content_lower:
    print("Spam keyword found in email content")


'''
# find the index of spam keyword
spam_index = email_content_lower.find(spam_keyword)

if spam_index > 0:
    print("Spam keyword found at index " + str(spam_index))
    print("This email is spam.")
'''


# calculate the number of words in email content
word_count = len(email_content_lower.split())

if word_count < 20:
    print("Word count: " + str(word_count))
    print("This email is spam.")