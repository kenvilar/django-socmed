from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render


@login_required
def user_list(req):
    users = User.objects.filter(is_active=True)
    return render(req, "account/user/list.html", {"section": "people", "users": users})


@login_required
def user_detail(req, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(req, "account/user/detail.html", {"section": "people", "user": user})
