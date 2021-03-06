from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField();
  create_date=models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True,null=True)

  def publish(self):
     self.published_date=timezone.now()
     self.save()

  def __str__(self):
     return  self.title



# Create your models here.
class Post_M(models.Model):
  author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  abstract=models.TextField();
  text = models.TextField();
  create_date=models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True,null=True)
  file_name=models.CharField(max_length=30);

  def publish(self):
     self.published_date=timezone.now()
     self.save()

  def __str__(self):
     return  self.title

#
class Comment(models.Model):
    post = models.ForeignKey('blog.Post_M',on_delete=models.CASCADE,related_name='comments')
    author=models.CharField(max_length=50)
    text=models.CharField(max_length=500)
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
      self.approved_comment = True
      self.save()

    def __str__(self):
      return  self.text

