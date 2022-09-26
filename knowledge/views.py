from django.shortcuts import render

from knowledge.models import KnowlegeBase
from django.db.models import Q

# Create your views here.


def start(request):
    if request.method == "POST":
        search = request.POST["search"]
        posts = KnowlegeBase.objects.filter(
            Q(title__contains=search) | Q(text__contains=search)
        )
    else:
        search = ""
        posts = KnowlegeBase.objects.all()
    data = {"posts": posts, "search": search}
    return render(request, "index.html", data)


def add(request):
    return render(request, "add.html")


def agb(request):
    return render(request, "agb.html")


def legal_notice(request):
    return render(request, "legal-notice.html")
