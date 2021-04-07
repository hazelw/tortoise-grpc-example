from tortoise.models import Model
from tortoise import fields


class Snake(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    pattern = fields.CharField(max_length=255)
