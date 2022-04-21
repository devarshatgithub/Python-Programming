# Configure Setting.py file before writing send_mail code, with your personal information to send mail.
# More in addition you will need to alllow less secure app in gmail authentication for smooth flow of the program.

from django.core.mail import send_mail

send_mail( 
    'The Subject goes here',        # SUBJECT OF THE MAIL
    'The Body context goes here',   # BODY OF THE MAIL
    '20ce014@charusat.edu.in',      # FROM @email
    ['20ce014@charusat.edu.in'],    # TO @email
    fail_silently=True, 
)