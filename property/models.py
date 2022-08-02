from django.db import models

# Create your views here.
property_type = {
    ('s', 'sale'),
    ('r', 'rate')
}


class Property(models.Model):
    name = models.CharField(max_length=50, verbose_name=' عنوان ')
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garage_number = models.PositiveIntegerField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='property/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name=' عنوان ')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
