from django.shortcuts import render, redirect


def profile(requests):
    if requests.session["authorized"]:
        user = requests.session["User"]
        return render(requests, "profile/profile.html", {"email": user})
    return redirect("/authorization/login")
