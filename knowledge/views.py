from django.shortcuts import render

from knowledge.models import KnowlegeBase

# Create your views here.


def start(request):
    if request.method == "POST":
        print("trying to post")
    posts = KnowlegeBase.objects.all()
    data = {"posts": posts}
    return render(request, "index.html", data)


def add(request):
    return render(request, "add.html")


def agb(request):
    return render(request, "agb.html")


def legal_notice(request):
    return render(request, "legal-notice.html")
