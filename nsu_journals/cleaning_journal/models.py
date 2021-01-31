from django.db import models


class Mark(models.Model):
    room = models.IntegerField()
    mark = models.IntegerField()
    small_room_mark = models.IntegerField()
    big_room_mark = models.IntegerField()
    common_room_mark = models.IntegerField()
    date = models.DateField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return "Mark: " + str(self.mark) + " Date: " + str(self.date) + " Room: " + str(self.room)
