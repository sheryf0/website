from django.db import models

# Create your models here.
class course(models.Model):
    course_name = models.CharField(verbose_name="course name", max_length=50)
    course_code = models.CharField(verbose_name="course code", max_length=10)
    group_id = models.ManyToManyField("accounts.group", verbose_name="group id")

    REQUIRED_FIELDS = ['course_name', 'course_code',]

    def __str__(self):
        return self.course_name
    

class handout(models.Model):
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=2000)
    year_used = models.DateTimeField( auto_now=False, auto_now_add=False)
    related_file = models.FileField( upload_to='handout', max_length=100)
    course = models.ForeignKey("materials.course", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class syllabus(models.Model):
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=2000)
    year_used = models.DateTimeField( auto_now=False, auto_now_add=False)
    related_file = models.FileField( upload_to='syllabus', max_length=100)
    course = models.ForeignKey("materials.course", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class book(models.Model):
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=2000)
    rating = models.IntegerField()
    related_file = models.FileField( max_length=100)
    course = models.ForeignKey("materials.course", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class past_question(models.Model):
    name = models.CharField( max_length=50)
    description = models.CharField( max_length=2000)
    year_used = models.DateTimeField( auto_now=False, auto_now_add=False)
    related_file = models.FileField(upload_to='past_questions', max_length=100)
    course = models.ForeignKey("materials.course", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    