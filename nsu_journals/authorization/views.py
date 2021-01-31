from django.shortcuts import render, redirect
from .models import Student
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


user_info = [None, None, None]


def send_message_with_code(email, code):
    bot_email = "nsu.journals@gmail.com"
    bot_email_password = "MoEfNbFWN8|T"

    msg = MIMEMultipart()
    msg['From'] = bot_email
    msg['To'] = email
    msg['Subject'] = "NSU JOURNALS"
    msg.attach(MIMEText(code, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], bot_email_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def confirm_email(requests, code):
    if user_info == [None, None, None]:
        return redirect("/authorization/registration")

    if code == user_info[2]:
        new_student = Student(email=user_info[0], password=user_info[1], group="-", is_super_user=False)
        new_student.save()
        return render(requests, "authorization/confirm_email.html", {"message": "Вы успешно зарегистрировались!"})
    return redirect("/authorization/registration")


def login(requests):
    global user_info
    requests.session["authorized"] = False
    message = ""
    if requests.method == "POST":
        email = requests.POST["email"]
        password = requests.POST["password"]
        if len(Student.objects.filter(email=email)) == 0 or Student.objects.filter(email=email)[0].password != password:
            message = "НЕВЕРНАЯ ПОЧТА ИЛИ ПАРОЛЬ!"
        else:
            requests.session["authorized"] = True
            requests.session["User"] = Student.objects.filter(email=email)[0].email
            user_info = [email, password, None]
            return redirect("/profile/")
    return render(requests, "authorization/login.html", {"message": message})


def registration(requests):
    global user_info
    message = ""
    if requests.method == "POST":
        email = requests.POST["email"]
        password = requests.POST["password"]
        if len(Student.objects.filter(email=email)) != 0:
            message = "ПОЧТА УЖЕ ИСПОЛЬЗУЕТСЯ!"
        elif "nsu" not in email.split("@")[-1].lower():
            message = "ВВЕДИТЕ ПОЧТУ НГУ!"
        else:
            code = os.urandom(20).hex()
            user_info = [email, password, code]
            send_message_with_code(email, code)
            message = "Подтвердите почту!"
    return render(requests, "authorization/regin.html", {"message": message})
