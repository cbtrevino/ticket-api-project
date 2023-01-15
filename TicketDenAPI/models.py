from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    talent = models.CharField(max_length=255)
    state = models.CharField(max_length=27)
    city = models.CharField(max_length=17)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.talent + ' | ' + str(self.category) + ' | ' + str(self.start_date) + ' - ' + str(self.end_date)