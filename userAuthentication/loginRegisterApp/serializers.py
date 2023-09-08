from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ('id', 'username', 'email','password')
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'password')

        extra_kwargs = {'password' : {"write_only": True}}

    # # Define a related_name for the groups field
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=_('groups'),
    #     blank=True,
    #     related_name='customuser_set',  # Change this to your preferred name
    #     related_query_name='user',
    # )

    # # Define a related_name for the user_permissions field
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=_('user permissions'),
    #     blank=True,
    #     related_name='customuser_set',  # Change this to your preferred name
    #     related_query_name='user',
    # )