from rest_framework import  serializers
from users.models import BlogUser

class UserDisplaySerializer(serializers.ModelSerializer):
  class Meta:
      model = BlogUser
      fields = ["username"]