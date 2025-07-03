from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class AccessType(models.Model):

    name = models.CharField(max_length=50,verbose_name=_("Name"),help_text=_("Access type name"))

    class Meta:
        db_table = "access_type"
        verbose_name = _("Access Type")
        verbose_name_plural = _("Access types")
        ordering = ["id"]

    def __str__(self):
        return self.name
    

class UserManager(BaseUserManager):
    ...


class UserModel(AbstractBaseUser,PermissionsMixin):

    name = models.CharField(max_length=250,verbose_name=_("Name"),help_text=_("User Name"),unique=True)
    email = models.EmailField(max_length=250,unique=True,verbose_name=_("E-mail"),help_text=("User's e-mail"))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation date"),help_text=_("Create date of the user"))
    type_of_access = models.ForeignKey(AccessType,on_delete=models.PROTECT,related_name="users",verbose_name=_("Type of access"),help_text=_("Type of access"),null=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "User"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["id"]

{
    "name":"Raphael",
    "email":"raphael.laurintino@gmail.com",
    "type_of_access":1
}