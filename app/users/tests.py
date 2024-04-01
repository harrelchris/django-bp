from django.test import TestCase

from users.admin import UserAdmin
from users.models import User


class TestAdmin(TestCase):
    def setUp(self):
        self.user = User.objects.create()

    def test_display_valid(self):
        for attr in UserAdmin.list_display:
            assert hasattr(self.user, attr)

    def test_filter_valid(self):
        for attr in UserAdmin.list_filter:
            assert hasattr(self.user, attr)

    def tearDown(self):
        self.user.delete()


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create()

    def test_has_attrs(self):
        attrs = [
            "uuid",
            "created_at",
            "updated_at",
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "is_staff",
            "is_superuser",
        ]
        for attr in attrs:
            assert hasattr(self.user, attr)

    def test_is_active(self):
        assert self.user.is_active

    def test_not_staff(self):
        assert not self.user.is_staff

    def test_not_superuser(self):
        assert not self.user.is_superuser

    def tearDown(self):
        self.user.delete()
