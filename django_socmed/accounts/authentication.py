from django.contrib.auth import get_user_model

from django_socmed.accounts.models import Profile

# from django_socmed.users.models import User

User = get_user_model()


class EmailAuthBackend:
    """
    Authenticate using an email address.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def create_profile(backend, user, *args, **kwargs):
        """
        Create user profile for social authentication
        """
        Profile.objects.get_or_create(user=user)
