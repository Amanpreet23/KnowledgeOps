from enum import Enum

from tortoise.models import Model
from tortoise import fields, models
from enum import Enum


class IngestStatus(str, Enum):
    PENDING = "pending"
    INDEXED = "indexed"
    FAILED = "failed"


class Sender(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Roles(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Role(Model):
    id = fields.UUIDField(pk=True)
    role_name = fields.CharEnumField(Roles, max_length=255)


class User(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    role = fields.ForeignKeyField("models.Role", related_name="users")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Tokens(Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="tokens",on_delete=fields.CASCADE)
    token_hash = fields.CharField(max_length=64, unique=True)
    expires_at = fields.DatetimeField()
    revoked_at = fields.DatetimeField(null=True)


class Conversation(Model):
    id = fields.UUIDField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="conversations",on_delete=fields.CASCADE)
    title = fields.CharField(max_length=200)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Message(Model):
    id = fields.UUIDField(pk=True)
    conversation = fields.ForeignKeyField("models.Conversation", related_name="messages",on_delete=fields.CASCADE)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


