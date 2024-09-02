from django.db import models


class RadioactiveMaterial(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    constant = models.FloatField(help_text="em µSv.m2/h.GBq", db_index=True)

