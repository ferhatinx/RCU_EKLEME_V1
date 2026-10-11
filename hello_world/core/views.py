from django.shortcuts import render

def index(request):
    context = {
        "title": "RCU Ekleme",
        "is_update_page": False,
    }
    return render(request, "index.html", context)


def update(request):
    context = {
        "title": "RCU Değiştirme",
        "is_update_page": True,
    }
    return render(request, "index.html", context)
