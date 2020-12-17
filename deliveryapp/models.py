from django.db import models

# Create your models here.

class Bussiness(models.Model):
    Bussiness_type_choices = [
    ('gs':'Gass'),
    ('wt':'Water'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True, blank=True)
    contact = models.CharField(unique=True, null=False)
    image = models.ImageField(default='profilepics/default.jpg', upload_to='profilepics')
    business_type = models.CharField(max_length=2, choices=Buiness_type_choices,default=gass)

    def __str__(self):
        return f'{self.user.username}


    def save(self,  *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)