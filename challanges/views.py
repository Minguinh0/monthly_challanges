from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challanges = {
    "january": "Eat more vegetables",
    "february": "Run more",
    "march": "Walk 20 min everyday",
    "april": "Eat healthy",
    "may": "This is may",
    "june": "This is june",
    "july": "This is july",
    "august": "This is august",
    "september": "This is september",
    "october": "This is october",
    "november": "This is november",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challanges.keys())

    return render(request, "challanges/index.html", {
        "months": months
    })

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirect_month]) #challange/hanuary
    return HttpResponseRedirect(redirect_path)

def monthly_challage(request, month):

    try:
        challange_text = monthly_challanges[month]
        return render(request, "challanges/challange.html", {
            "text": challange_text,
            "month_name": month
        })
    except:
        raise Http404()