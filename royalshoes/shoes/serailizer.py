from rest_framework import serializers
from .models import Registration, AddToCart, ShoeList, CompanyList, CompanyBanner


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=1000, required=False)
    mobile = serializers.CharField(max_length=10)
    email = serializers.EmailField(required=False)
    dob = serializers.DateField(required=False)
    password = serializers.CharField(max_length=50)

    class Meta:
        model = Registration
        fields = ("name", "mobile", "email", "dob", "password")

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Registration.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance


class AddToCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddToCart
        fields = ("shoe", "user", "items", "price", "status")

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.shoe = instance.shoe
    #     instance.user = instance.user
    #     instance.items = validated_data.get('items', instance.items)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return instance


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyList
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBanner
        fields = "__all__"


class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoeList
        fields = ["id", "name", "description", "price", "size", "shoe_image"]
        # fields = "__all__"
