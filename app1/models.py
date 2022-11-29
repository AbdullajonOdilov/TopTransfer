from django.db import models

class Club(models.Model):
    c_name= models.CharField(max_length=100)
    logo = models.FileField()
    country = models.CharField(max_length=100)
    def __str__(self):return self.c_name

class Player(models.Model):
    p_name = models.CharField(max_length=200)
    clubi = models.ForeignKey(Club,on_delete=models.CASCADE)
    p_age = models.PositiveSmallIntegerField()
    t_money = models.PositiveSmallIntegerField()
    def __str__(self):return self.p_name

class Transfer(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    old = models.ForeignKey(Club,on_delete=models.CASCADE,related_name='sales')
    new = models.ForeignKey(Club,on_delete=models.CASCADE,related_name='transfers')
    money_tft = models.PositiveIntegerField()
    money = models.PositiveIntegerField()

    season = models.CharField(max_length=100)
    def __str__(self):return f'{self.player}, {self.old} -> {self.new} '


