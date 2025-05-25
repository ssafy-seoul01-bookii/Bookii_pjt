from django.db import models
from django.contrib.auth.models import AbstractUser

PATH = {
    "Account": {
      "profile_img": "accounts/profile_imgs/",
    }
}

GENDER_TYPE_CHOICES = [
  ("M", "남자"),
  ("F", "여자"),
]

class User(AbstractUser):
  keyword = models.ManyToManyField(to="books.keyword", through="books.User_keyword", related_name="user_keywords")
  category = models.ManyToManyField(to="books.Category", through="books.Preferred_category", related_name="user_categories")
  age = models.PositiveIntegerField(blank=True,)
  gender = models.CharField(max_length=1, choices=GENDER_TYPE_CHOICES, blank=True,)
  annual_reading_amount = models.PositiveIntegerField(blank=True,)
  weekly_avg_reading_time = models.PositiveIntegerField(blank=True,)
  profile_img_url = models.ImageField(upload_to=PATH["Account"]["profile_img"], default=f"{PATH['Account']['profile_img']}/default_img.png",)
  # N or Y
  is_critic = models.CharField(max_length=1, default="N")
  following = models.ManyToManyField(to="self", through="accounts.Follow",)

class Follow(models.Model):
  following = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE, related_name="followers")
  follower = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE, related_name="followings")
