from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

#trying to add a group model here that should theoretically have a parent child relationship with students
class group(models.Model):
    department = models.CharField(verbose_name="Department", max_length=50)
    level = models.CharField(verbose_name="level", max_length=50)
    group_id = models.CharField(
        verbose_name="Group Id", max_length=10, primary_key=True, unique=True)

    def __str__(self):
        return self.group_id


class studentManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, group_id,  password=None):
        if not email:
            raise ValueError("email is required ")
        if not first_name:
            raise ValueError('first name is required')
        if not last_name:
            raise ValueError("last name is required")
        if not phone:
            raise ValueError("phone number is required")
        if not group_id:
            raise ValueError("your group ID is required ")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            group_id=group_id,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, group_id, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            group_id=group_id,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class student(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email Address", max_length=254, unique=True)
    first_name = models.CharField(verbose_name="First Name", max_length=50)
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    is_courseRep = models.BooleanField(default=False)
    group_id = models.ForeignKey(
        group, on_delete=models.CASCADE, null=True, blank=True)

    date_joined = models.DateTimeField(
        verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'group_id', ]
    objects = studentManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
