from django.db import models


# Create your models here.
class lecture_update(models.Model):
    course_name = models.CharField(verbose_name="Course name", max_length=25)
    course_code = models.CharField(verbose_name="course code", max_length=10)
    venue = models.CharField(verbose_name="venue", max_length=50)
    time_start = models.DateTimeField(verbose_name="lecture starting time",)
    time_end = models.DateTimeField(verbose_name="lecture finish time",)
    course_topic = models.CharField(verbose_name="course topic", max_length=50)
    lecture_requirement= models.CharField(verbose_name="lecture requirement", max_length=100)
    attendance = models.BooleanField(("will attendance be taken"), default= True)
    group_id = models.ForeignKey("accounts.group", on_delete=models.CASCADE)
    author = models.CharField( max_length=50, blank= True, null= True)


    REQUIRED_FIELDS = ['course_name', 'course_code', 'time_start', 'time_end']


    def __str__(self):
        return self.course_name


class pending_assignment(models.Model):
    course_name= models.CharField(("course name"), max_length=50)
    assignment_question = models.CharField(("assignment question"), max_length=5000)
    related_file_for_assignment = models.FileField(upload_to='media', max_length=30, blank=True, null=True)
    submitted_to_who = models.CharField(("to be submitted to whom"), max_length=50)
    where_to_submit = models.CharField(("where  to submit"), max_length=50)
    assignment_marks = models.CharField(("marks the assignment will take"), max_length=50)
    assignment_dueDate = models.DateTimeField(verbose_name="assignment due date", auto_now=False, auto_now_add=False)
    group_id = models.ForeignKey("accounts.group", verbose_name=("group id"), on_delete=models.CASCADE)
    author = models.CharField( max_length=50, blank= True, null= True)

    REQUIRED_FIELDS = ['course_name', 'assignment_dueDate', 'where_to_submit', 'submitted_to_who']

    def __str__(self):
        return self.course_name
    





class upcoming_test(models.Model):
    course_name = models.CharField(verbose_name="course name", max_length=50)
    date_announced = models.DateTimeField(verbose_name="date announced", auto_now=False, auto_now_add=False)
    test_time = models.DateTimeField(verbose_name="test time", auto_now=False, auto_now_add=False)
    venue= models.CharField(verbose_name="venue", max_length=50)
    area_of_concentration = models.CharField(verbose_name="area of concentration", max_length=50)
    test_marks = models.CharField(verbose_name= "test marks", max_length=50)
    group_id = models.ForeignKey("accounts.group", verbose_name=("group id"), on_delete=models.CASCADE)
    author = models.CharField( max_length=50, blank= True, null= True)

    REQUIRED_FIELDS = ['course_name', 'test_time', 'venue']


    def __str__(self):
        return self.course_name
    
class important_information(models.Model):
    title= models.CharField(verbose_name= "title", max_length=50)
    body = models.CharField(verbose_name= "body", max_length=5000)
    group_id = models.ForeignKey("accounts.group", on_delete=models.CASCADE)
    date_posted = models.DateTimeField( auto_now=True,)
    author = models.CharField( max_length=50, blank= True, null= True)
    def __str__(self):
        return self.title
    