from django.db import models

class Seifa(models.Model):
    SA1 = models.CharField(max_length=50, primary_key=True)
    IRSD_Score = models.FloatField()
    IRSD_Decile = models.IntegerField()
    IRSAD_Score = models.FloatField()
    IRSAD_Decile = models.IntegerField()
    IER_Score = models.FloatField()
    IER_Decile = models.IntegerField()
    IEO_Score = models.FloatField()
    IEO_Decile = models.IntegerField()
    Usual_Resident_Population = models.IntegerField()

    class Meta:
        db_table = 'SA1_SEIFA'

    def __str__(self):
        return self.SA1