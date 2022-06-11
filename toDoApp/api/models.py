from django.db import models


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=250, null=False, blank=False)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def change_completed_state(self):
        self.completed = not self.completed
        self.save()

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["-created_date"]
