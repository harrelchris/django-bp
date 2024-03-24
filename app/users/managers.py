from django.contrib.auth.models import UserManager as AuthUserManager


class UserManager(AuthUserManager):
    def get_queryset(self):
        return super().get_queryset()
