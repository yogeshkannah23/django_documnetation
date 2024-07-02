from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.first_name + self.last_name}"

class Musician(models.Model):
    def caps(value):
        if not value.isupper():
            raise ValidationError(f"The first_name needs to be in upper case")
        return 

    first_name = models.CharField(max_length=50,help_text="Enter caps",unique=True,validators=[caps])
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name + self.last_name}"




class Album(models.Model):
    Year_in_school = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior",
    "GR": "Graduate",
    }
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    year = models.CharField(max_length = 2,choices=Year_in_school,default="FR")

    def __str__(self) -> str:
        return self.name

class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    PlaceType = models.TextChoices("PlaceType","First Second Third")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType, max_length=10)
    position = models.CharField(blank=True, choices=PlaceType, max_length=30)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Runneres"


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

