from django.db import models
from django.contrib.auth.models import AbstractUser


class Agency :
  user_type = models.CharField(max_length= 12, default = "NORMAL" )
  state = models.CharField(max_length= 32, null=True)
  office_address = models.CharField(max_length= 300, null= True)
  website_url = models.URLField(null=True)
  cac_number = models.CharField(max_length= 24, null= True)
  phone = models.CharField(max_length= 11, null=True)

  def __str__(self):
      return "{}".format(self.email)