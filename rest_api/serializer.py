from rest_framework import serializers
from uploading.models import Post
from accounts.models import Account

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'user', 'description', 'post_link']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=100)
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_active']

        def create(self, validated_data):
            return Account.objects.create_user(**validated_data)