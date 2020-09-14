from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=200)
    picnic_table = models.IntegerField('Picnic Table #')
    exit_sign = models.CharField('Exit Sign', max_length=200, default='')
    def __str__(self):
        return self.name

class Level(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    min_level = models.IntegerField(null=True)
    routes = models.IntegerField()
    def __str__(self):
        return str(self.routes) + '@' + str(self.min_level)
