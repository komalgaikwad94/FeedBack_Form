from django.db import models

# Create your models here.

# Create your models here.
class ContactQuery(models.Model):
    full_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    query=models.TextField()
    submitted_at=models.DateTimeField(auto_now_add=True)

    #
    def __str__(self):
        return f'{self.full_name}:{self.query}'


class FeedbackForm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return f'{self.name}:{self.email}'