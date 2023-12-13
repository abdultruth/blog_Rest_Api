from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.content)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='')
    blog = models.ForeignKey(Feed, on_delete=models.CASCADE)
    comment = models.ForeignKey(
                                'self', on_delete=models.CASCADE, 
                                null=True, blank=True, 
                                related_name='replies'
                            )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.body)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']



