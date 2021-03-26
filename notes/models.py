from django.db import models

# Create your models here.
class Notes(models.Model):
    name   = models.CharField(max_length=50, blank=False, default= '')
    item01 = models.CharField(max_length=50, blank=False, default='')
    item02 = models.CharField(max_length=50, blank=True, default='')
    item03 = models.CharField(max_length=50, blank=True, default='')
    item04 = models.CharField(max_length=50, blank=True, default='')
    item05 = models.CharField(max_length=50, blank=True, default='')
    item06 = models.CharField(max_length=50, blank=True, default='')
    item07 = models.CharField(max_length=50, blank=True, default='')
    item08 = models.CharField(max_length=50, blank=True, default='')
    item09 = models.CharField(max_length=50, blank=True, default='')
    item10 = models.CharField(max_length=50, blank=True, default='')



    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', )

