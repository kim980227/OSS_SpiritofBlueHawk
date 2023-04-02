from django.db import models

# Create your models here.
class Post(models.Model):
    item = models.CharField(max_length=50)
    itemIndex = models.IntegerField()
    spotX = models.FloatField()
    spotY = models.FloatField()
    budget = models.PositiveIntegerField()
    # spotX and spotY is for google api spot
    def __str__(self):
        return f'[{self.pk}]{self.item}'
    def get_absolute_url(self):
        return f'/mainapp/{self.pk}/'


class BulletinBoard(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    bulletin_board = models.ForeignKey(BulletinBoard, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} on {self.bulletin_board.title}'
