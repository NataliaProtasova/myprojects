from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializers.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)

    # price = serializers.FloatField(min_value=1.00, max_value=100000)
    price = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )
    sale_start = serializers.DateTimeField(
        required=False,
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    sale_end = serializers.DateTimeField(
        required=False,
        input_formats=['%I:%M %p %d %B %Y'], format=None, allow_null=True,
        help_text='Accepted format is "12:01 PM 16 April 2019"',
        style={'input_type': 'text', 'placeholder': '12:01 AM 28 July 2019'},
    )
    photo = serializers.ImageField(default=None)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'sale_start', 'sale_end',
            'is_on_sale', 'current_price',
            'photo'
        )
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
