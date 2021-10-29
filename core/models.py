from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Places(models.Model):
    owner = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    number_of_tables = models.IntegerField(default=1)

    def __str__(self):
        return "{}/{}".format(self.owner.username, self.name)


class Category(models.Model):
  owner = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE, related_name="categories")
  name = models.CharField(max_length=255)

  def __str__(self):
      return "{}/{}".format(self.owner, self.name)

class MenuItem(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  price = models.IntegerField(default=0)
  image = models.CharField(max_length=255)
  show_price = models.BooleanField(default=False)
  is_available = models.BooleanField(default=True)
  code = models.IntegerField(default=0)
  stars = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
     )

  def __str__(self):
    return "{}/{}".format(self.category, self.name)