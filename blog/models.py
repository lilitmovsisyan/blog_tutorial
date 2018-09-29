from django.db import models
from django.utils import timezone

"""Our model for a blog post is:
Properties: title, text, author, date_created, date_published
Actions(i.e. methods): Publish
So we put these into a class to create such an object model.

Define the properties (what type is it? does it have a relation to another property or object?) e.g.:

models.CharField – this is how you define text with a limited number of characters.
models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
models.DateTimeField – this is a date and time.
models.ForeignKey – this is a link to another model.

ForeignKey is like a unique identifier I think?"""

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title    

