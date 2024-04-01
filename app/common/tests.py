from django.test import TestCase

from common.models import BaseModel


class TestModels(TestCase):
    def test_has_attrs(self):
        attrs = [
            "uuid",
            "created_at",
            "updated_at",
        ]
        for attr in attrs:
            assert hasattr(BaseModel, attr)
