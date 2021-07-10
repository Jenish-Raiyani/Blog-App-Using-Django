from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author=models.CharField(max_length=14)
    content=models.TextField(default="")
    slug=models.CharField(max_length=130,default="")
    #head0 = models.CharField(max_length=500, default="")
   # chead0 = models.CharField(max_length=5000, default="")
   # head1 = models.CharField(max_length=500, default="")
   # chead1 = models.CharField(max_length=5000, default="")
    #head2 = models.CharField(max_length=500, default="")
    #chead2 = models.CharField(max_length=5000, default="")
    #pub_date = models.DateField()
    timeStamp=models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to='media', default="")
    


    def __str__(self):
        return self.title

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email