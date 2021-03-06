from django.db import models
from core import models as core_models
class Review(core_models.TimeStampedModel):

    """ Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    clearliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE) # 리뷰하는 사람
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE) # 리뷰하는 방

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):
        avg = (
            self.accuracy +
            self.communication +
            self.clearliness +
            self.location +
            self.check_in +
            self.value 
        ) / 6

        return round(avg, 2)
    
    rating_average.short_description = "Avg."