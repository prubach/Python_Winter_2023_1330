email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawel@pl'
email4 = 'pawel@'
email5 = 'pawel@.pl'

email_list = [email1, email2, email3, email4, email5]
#TODO create a function that will test if the email is valid
def validate_email(email):
    #....
    return True


#print(validate_email(email1))
for em in email_list:
    print('{}: {}'.format(em, validate_email(em)))