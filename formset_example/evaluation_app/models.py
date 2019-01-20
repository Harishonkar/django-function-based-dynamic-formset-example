from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class OptionType(models.Model):
    option_type=models.CharField(max_length=100)

    def __str__(self):
        return self.option_type


    def get_options(self):
        return (self.id,self.option_type)


class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    question_name=models.CharField(max_length=100)
    parent_course=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,  related_name='child_question')

    extra_text_fields=models.CharField(max_length=100)


    def __str__(self):
        return self.question_name


class Options(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    option_type=models.ForeignKey(OptionType,on_delete=models.CASCADE)
    options=models.CharField(max_length=100)

    def __str__(self):
        return self.options

class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    user_answer=models.CharField(max_length=100)
    created_date_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_answer
