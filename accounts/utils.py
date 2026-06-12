# views.py
from django.core.mail import send_mail

def send_test_email(email):
    send_mail(
    subject = "DAVRON MARKET",
    message = "ROYXATDAN MUVAFAQIYATLI OTDINGIZ TABRIKLAYMIZ KALLANGIZGA KALLAM ",
    from_email="davronbekabdurazzaqov98@gmail.com",
    recipient_list = [email],
    fail_silently= False,

    )
    return True

def send_email_login(email):
    send_mail(
    subject = "DAVRON MARKET",
    message = "Akkuntingizga Kirdingiz ! Agar bu siz bolmasangiz iltimos parolni yangilab oling",
    from_email="davronbekabdurazzaqov98@gmail.com",
    recipient_list = [email],
    fail_silently= False,

    )
    return True

