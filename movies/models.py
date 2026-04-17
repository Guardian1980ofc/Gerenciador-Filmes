from django.db import models

SCORE_CHOICES = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Genre(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Actor(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    release_date = models.DateField("Release Date")
    score = models.IntegerField(choices=SCORE_CHOICES, default=3)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="movies",
        null=True,
        blank=True)
    
    director = models.ForeignKey(
        Director, 
        on_delete=models.PROTECT, 
        related_name="movies",
        null=True, 
        blank=True
    )

    actors = models.ManyToManyField(
        Actor, 
        related_name="movies", 
        blank=True
    )

    def __str__(self):
        return self.name
