from django.db import models

class Girls(models.Model):
    user_name = models.CharField(max_length=50)
    onlyfans_url = models.URLField(max_length=500)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name} and {self.onlyfans_url}'