from django.db import models

class blogs(models.Model):
    Title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()
    Image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Title
    
    def pub_date_pr(self):
        return self.pub_date.strftime('%c')


