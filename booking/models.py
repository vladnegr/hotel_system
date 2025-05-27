from django.db import models
from django.contrib.auth.models import User

class TypeRoom(models.Model):
    name = models.CharField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Тип кімнати:{self.name}'
    

    class Meta():
        verbose_name = 'Тип кімнати'
        verbose_name_plural = 'Тип кімнати'
    


class Room(models.Model):
    type_room = models.ForeignKey(TypeRoom, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Rooms', null=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    places = models.IntegerField(default=1)

    def __str__(self):
        return f'Кімната:{self.name}, ціна:{self.price}.'
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=18)

    def __str__(self):
        return f'Бронювання:{self.room}, дата заїзду{self.date_in}, дата виїзду{self.date_out}'