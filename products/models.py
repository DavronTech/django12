from django.db import models

# Create your models here.

class Products(models.Model):
    CHOICES = (
        ('white', 'WHITE'),
        ('blue', ' BLUE'),
        ('black', 'BLACK'),
        ('red', 'RED'),
        ('green', 'GREEN'),
        ('yellow', 'YELLOW'),
        ('purple', 'PURPLE'),
        ('orange', 'ORANGE'),
        ('pink', 'PINK'),
        ('gray', 'GRAY'),
        ('brown', 'BROWN'),
    )
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100, choices=CHOICES)
    image = models.ImageField(upload_to='watch/', default = '/default_watch.jpg', blank = True)

    def str(self):
        return self.name