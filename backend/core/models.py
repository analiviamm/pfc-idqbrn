from django.db import models


class RadioactiveMaterial(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    constant = models.FloatField(help_text="em µSv.m2/h.GBq", db_index=True)


class Result(models.Model):
    date = models.DateField()
    radiation_level = models.FloatField(help_text="em µSv/h", db_index=True)
    altitude = models.FloatField(help_text="em m", db_index=True)
    min_radius = models.FloatField(help_text="em m", db_index=True, default=0)
    access_restrict = models.FloatField(help_text="em m", db_index=True, default=0)
    tireoide_monitoring = models.FloatField(help_text="em m", db_index=True, default=0)
    aliment_restrict = models.FloatField(help_text="em m", db_index=True, default=0)
    people_reallocation = models.FloatField(help_text="em m", db_index=True, default=0)
    immediate_evacuation = models.FloatField(help_text="em m", db_index=True, default=0)
    first_minute_contact = models.FloatField(help_text="em m", db_index=True, default=0)
    second_minute_contact = models.FloatField(help_text="em m", db_index=True, default=0)
