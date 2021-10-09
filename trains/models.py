from django.db import models
<<<<<<< HEAD
from django.db.models.deletion import CASCADE
from django.urls import reverse


class train(models.Model):
    TRAIN_STATUS = [
        ('Revenue', (
            ('PS', 'Passenger Service'),
            ('ER', 'Early Return'),
            ('CM', 'CSO Manning'),
            ('RSS', 'RS Spare'),
            ('OPS', 'OPS Spare'),
        )),
        ('Non Revenue', (
            ('ASA', 'Auto Shunt Allow'),
            ('MSO', 'Manual Shunt Only'),
            ('DOWN', 'Down(Not To Move)'),
        )),
    ]

    tid = models.CharField(primary_key=True, max_length=20)
    location = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=30, choices=TRAIN_STATUS, default='PS')
    remarks = models.TextField(blank=True)

    class Meta:
        ordering = ["tid"]

    def __str__(self):
        return self.tid

    def get_absolute_url(self):
        return reverse('trains-list')
=======

# Create your models here.
>>>>>>> 3bd82cf312519771f4dce2d198a701070b0e52a6
