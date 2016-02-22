from django.core.mail import send_mail

def sendMailImageProccesed(email):
    print str(email)
    send_mail('Design publication', 'Greetings, Your design has been published.',
               'mariocloud2016@gmail.com' ,[str(email)])