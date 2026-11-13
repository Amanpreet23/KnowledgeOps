from tortoise import migrations
from tortoise.migrations import operations as ops
from database.models import Roles
from tortoise import fields

class Migration(migrations.Migration):
    dependencies = [('models', '0001_initial')]

    initial = False

    operations = [
        ops.AlterField(
            model_name='Role',
            name='role_name',
            field=fields.CharEnumField(description='ADMIN: admin\nUSER: user', enum_type=Roles, max_length=255),
        ),
    ]
