from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)   
    author =models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Authors(models.Model):
    name=models.CharField(max_length=50)
    started=models.DateTimeField(auto_now_add=True)    

class Comment(models.Model):
    post=models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author =models.CharField(max_length=50)
    text=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text