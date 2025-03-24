from arcforge.core.model import *

@Model.Table("tb_cliente")
class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=100)
    email = CharField(max_length=100,unique=True)
    password = CharField(max_length=100)