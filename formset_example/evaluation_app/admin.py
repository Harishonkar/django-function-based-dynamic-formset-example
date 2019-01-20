from django.contrib import admin
from .models import Course,OptionType,Question,Options,Answer
# Register your models here.
admin.site.register(Course)
admin.site.register(OptionType)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(Answer)
