from datetime import timedelta
from django.utils import timezone
from django.db import migrations

def create_sample_product_data(apps, schema_editor):
    Product = apps.get_model('store', 'Product')
    Product(
        id=1, name='Product 1', description='Description prod 1', price=1.00,
        photo='products/prod1.jpg',
    ).save()
    Product(
        id=2, name='Product 2', description='Description prod 2', price=2.00,
        photo='products/prod2.jpg',
    ).save()
    Product(
        id=3, name='Product 3', price=3.00,
        description='Description prod 3',
        sale_start=timezone.now(),
        sale_end=timezone.now() + timedelta(days=10),
        photo='products/prod3.jpg',
    ).save()
    Product(
        id=4, name='Product 4', price=3.00,
        description='Description prod 4',
        sale_start=timezone.now(),
        sale_end=timezone.now() + timedelta(days=10),
        photo='products/prod4.jpg',
    ).save()

class Migration(migrations.Migration):
    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_product_data),
    ]
