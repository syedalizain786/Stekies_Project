import re
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    f_name=models.CharField(max_length=200 ,blank=False, null=False)
    l_name=models.CharField(max_length=200 ,blank=False, null=False)
    email=models.EmailField(max_length=200, unique=True, blank=False, null=False)
    phone=models.CharField(max_length=20 , blank=True)
    city = models.CharField(max_length=200, blank=False, null=False)
    max_price = models.CharField(max_length=100, blank=False, null=False)
    area = models.CharField(max_length=100, blank=False, null=False)
    no_of_rooms = models.CharField(max_length=10, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)


    class Meta:
        db_table = 'user'

    def clean(self):
        if not self.f_name:
            raise ValidationError({'f_name': 'First name is required.'})
        if not self.l_name:
            raise ValidationError({'l_name': 'Last name is required.'})
        if not self.email:
            raise ValidationError({'email': 'Email is required.'})
        if not self.city:
            raise ValidationError({'city': 'City filter is required.'})
        if not self.max_price:
            raise ValidationError({'max_price': 'Maximum price filter is required.'})
        if not self.area:
            raise ValidationError({'area': 'Area filter is required.'})
        if not self.no_of_rooms:
            raise ValidationError({'no_of_rooms': 'Bedrooms filter is required.'})
        if not self.password:
            raise ValidationError({'password': 'Password is required.'})
        #     pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&])[A-Za-z\d#@$!%*?&]{8,}$')
        #     if not pattern.match(self.password):
        #         raise ValidationError({
        #             'password': "Password must be at least 8 characters long, contain at least one uppercase letter, "
        #                         "one lowercase letter, one number, and one special character including the # symbol."
        #         })
        # super().clean()

    # def save(self, *args, **kwargs):
    #         self.full_clean()
    #         self.password = make_password(self.password)
    #         super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
    @property
    def is_authenticated(self):
        return True