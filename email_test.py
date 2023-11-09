email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawel@pl'
email4 = 'pawel@'
email5 = 'pawel@.pl'
email6 = 'pawel.pl'

email_list = [email1, email2, email3, email4, email5, email6]
#TODO create a function that will test if the email is valid
def validate_email(email):
    at_pos = email.find('@')
    print(at_pos)
    print(email[-1])
    if email[0] in ['@', '.'] or email[-1] in ['@', '.']:
        return False

    if at_pos < 1 or at_pos > len(email) - 2:
        return False
    dot_pos = email.find('.')
    if dot_pos < 1:
        return False



    #....
    return True


#print(validate_email(email1))
for em in email_list:
    #print('{}: {}'.format(em, validate_email(em)))
    print(f'{em}: {validate_email(em)}')


my_text = '{}: {}'

res = my_text.format('Hello', 'World')
print(res)

a = 'Hello'
b = 'World'

my_text = f'{a}: {validate_email(email1)}'
print(my_text)

my_text = a + ': ' + str(b)
