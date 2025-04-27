from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("todo:tag-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created_at"]

    def __str__(self) -> str:
        return f"{self.content[:50]}..."

    def get_absolute_url(self) -> str:
        return reverse("todo:task-detail", kwargs={"pk": self.pk})
