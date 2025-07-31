from django.db import models
from django.contrib.auth.models import User

class Produk(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.DecimalField(max_digits=1000,decimal_places=2)
    deskripsi = models.TextField()
    stock = models.IntegerField()
    gambar = models.ImageField(upload_to='', null=True, blank=True)
    waktu_ditambahkan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Produk, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.harga * self.quantity
    
