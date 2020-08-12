from django.db import models
from django.utils.crypto import get_random_string

def new_file_name(instance, filename):
    return 'images/{0}{1}'.format(get_random_string(length=10), filename)



STREAM = (
    ('B','BTECH'),
    ('M','MTECH')
)

CATEG = (
    ('Job','JOB'),
    ('Internship','INTERNSHIP')
)


class Article(models.Model):
    Title = models.CharField(max_length=100)
    category =models.CharField(choices=CATEG, max_length=128)
    Description = models.TextField()
    start_date =models.DateTimeField(null=True, blank=True)
    end_date =models.DateTimeField(null=True, blank=True)
    official_link =models.CharField(max_length=100)
    image = models.ImageField(upload_to=new_file_name,
                              blank=True,
                              null=True)
    created = models.DateTimeField(auto_now_add=True)
    stream =models.CharField(choices=STREAM, max_length=128)

    def __str__(self):
        return self.category + ' ' + str(self.created)
