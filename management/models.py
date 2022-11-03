from django.db import models

class StatusManagement(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class CategoryManagement(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class ColorManagement(models.Model):
    color_name = models.CharField(max_length=200, verbose_name='Цвет')

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class BrandManagement(models.Model):
    brand_name = models.CharField(max_length=200, verbose_name='Бренд')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Имя')
    product_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    product_description = models.CharField(max_length=200, verbose_name='Описание', blank=True)
    product_img = models.ImageField(upload_to='product_img/')
    product_status = models.ForeignKey(StatusManagement, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    product_category = models.ForeignKey(CategoryManagement, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')
    product_color = models.ForeignKey(ColorManagement, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Цвет')
    product_brand = models.ForeignKey(BrandManagement, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Бренд')
    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# class CommentCrm(models.Model):
#     comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
#     comment_text = models.TextField(verbose_name='Текст комментария')
#     comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

#     def __str__(self):
#         return self.comment_text

#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
