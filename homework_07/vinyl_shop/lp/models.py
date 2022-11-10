from django.db import models

class RecordLabel(models.Model):
    name = models.CharField(max_length=30)

class Lp(models.Model):
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=40)
    year = models.IntegerField()
    condition = models.CharField(max_length=2)
    record_label = models.ForeignKey(RecordLabel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.album

class LpGenre(models.Model):
    lp = models.ForeignKey(Lp, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)

