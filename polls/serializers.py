from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class userSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(
            validators=[UniqueValidator(queryset=User.objects.all())],
            allow_blank=True
        )

    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())],
            max_length=32
        )

    # phone = serializers.IntegerField(
    #     required=True,
    #     min_value=1111111111,
    #     max_value=9999999999
    # )

    password = serializers.CharField(
        required=True,
        min_length=10,
        write_only=True
     )

    password2 = serializers.CharField(
        required=True,
        write_only=True
    )

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'password2', 'first_name', 'last_name']

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({"Password": "Entered Password Doesn't match"})

        user = User(
            # email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user
