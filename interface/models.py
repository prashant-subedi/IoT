from django.db import models

# Create your models here.
class Device(models.Model):
    device_id=models.IntegerField(primary_key=True)
    device_status=models.BooleanField(default=False)
    device_name=models.CharField(choices=[
        ('LT','Light'),
        ('FN','Fan')
    ],max_length=20)
    room_number=models.IntegerField(default=0)


    def __str__(self):
        return self.device_name