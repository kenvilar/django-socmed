# from django_socmed.users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
