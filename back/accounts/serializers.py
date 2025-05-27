from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False,)
    gender = serializers.ChoiceField(choices=[("M", "남자"), ("F", "여자")], required=False,)
    annual_reading_amount = serializers.IntegerField(required=False,)
    weekly_avg_reading_time = serializers.IntegerField(required=False,)
    profile_img_url = serializers.ImageField(required=False,)
    is_critic = serializers.ChoiceField(choices=[("N", "아님"), ("Y", "평론가")], required=False,)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["age"] = self.validated_data.get("age", 0)
        data["gender"] = self.validated_data.get("gender", "")
        data["annual_reading_amount"] = self.validated_data.get("annual_reading_amount", 0)
        data["weekly_avg_reading_time"] = self.validated_data.get("weekly_avg_reading_time", 0)
        data["profile_img_url"] = self.validated_data.get("profile_img_url", "default_img.png")
        data["is_critic"] = self.validated_data.get("is_critic", "N")
        return data

    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get("age", 0)
        user.gender = self.validated_data.get("gender", "")
        user.annual_reading_amount = self.validated_data.get("annual_reading_amount", 0)
        user.weekly_avg_reading_time = self.validated_data.get("weekly_avg_reading_time", 0)
        user.profile_img_url = self.validated_data.get("profile_img_url", user.profile_img_url)
        user.is_critic = self.validated_data.get("is_critic", "N")
        user.save()
        return user
