from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserCreateFrom


def create_user(request):
    if request.method == "POST":
        form = UserCreateFrom(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, "user create successfully you can login now")
            return redirect("users/login")
        messages.error(request, "fix the errors")
    else:
        form = UserCreateFrom()
    return render(request, "users/register.html", {"form": form})

