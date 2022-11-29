from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.author} - {self.title}"


    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    