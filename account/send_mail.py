from django.core.mail import send_mail

def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email = user.email
    send_mail('Hey activate your account', f'to activate your account you need to follow the link: {full_link}',
              'cbrowne9472@gmail.com',
              [to_email,],
              fail_silently=False)

def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Subject',
        f'Your code for reset password: {code}',
        'from@example.com',
        [to_email,],
        fail_silently=False
    )