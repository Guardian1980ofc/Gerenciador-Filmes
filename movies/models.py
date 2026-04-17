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

class Movie(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    release_date = models.DateField("Release Date")
    score = models.IntegerField(choices=SCORE_CHOICES, default=3)

    def __str__(self):
        return self.name