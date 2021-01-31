from django.shortcuts import render, redirect
from .models import Mark


def get_marks_from_room(requests, room):
    if "authorized" not in requests.session or not requests.session["authorized"]:
        return redirect("/authorization/login")
    marks = sorted([str(mark.date) + ": " + str(mark.mark) for mark in Mark.objects.filter(room=room)], reverse=True)
    return render(requests, "cleaning_journal/print_marks_from_room.html", {"marks": marks})


def get_room(requests):
    if "authorized" not in requests.session or not requests.session["authorized"]:
        return redirect("/authorization/login")
    if requests.method == "POST":
        room = requests.POST["room"]
        return redirect("/cleaning_journal/get_rooms_marks/" + room)
    return render(requests, "cleaning_journal/get_room.html")
