from django.shortcuts import render


def home(requests):
    requests.session["authorized"] = False
    return render(requests, "homepage/home.html")
