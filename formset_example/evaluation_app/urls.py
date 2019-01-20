

from django.urls import path
from . import views
urlpatterns=[
path('add_question/',views.add_question,name='add question'),
path('success/',views.success,name='success'),
path('update_question/<int:id>',views.update_question,name='update_question'),

#path('add_question_def/',views.CreateQuestionAnswer,name='add question def'),

]
