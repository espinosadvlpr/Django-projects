import email
import re
from unicodedata import name
from django.shortcuts import render

from survey_form.models import Survey


def index_form(request):
    if request.method == "POST":
        user_name = request.POST["user-name"]
        user_email = request.POST["user-email"]
        user_age = request.POST["user-age"]
        user_role = request.POST["role"]
        user_comments = request.POST["textarea"]

        Survey.objects.create(
            name=user_name,
            email=user_email,
            age=user_age,
            role=user_role,
            comments=user_comments,
        )

    return render(request, "index.html")
