from django.conf import settings
from django.db import models
class Comment(models.Model):
    'Generated Model'
    blog = models.ForeignKey("users.User",on_delete=models.PROTECT,related_name="comment_blog",)
    author = models.ForeignKey("users.User",on_delete=models.PROTECT,related_name="comment_author",)
    pub_date = models.DateField()
    mod_date = models.DateTimeField(auto_now=True,)
    message = models.TextField()
