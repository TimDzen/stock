from rest_framework import serializers
from rest_framework import validators
from api.models import ApiUser, Stock, Product, Business


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ]
    )
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ]
    )
    password = serializers.CharField(min_length=6,
                                     max_length=20,
                                     write_only=True)
    user_type = serializers.ChoiceField(choices=ApiUser.user_type_choices)

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Business
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
