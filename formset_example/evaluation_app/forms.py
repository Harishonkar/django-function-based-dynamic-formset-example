from django import forms
from .models import Question,Options,OptionType
from django.forms import formset_factory
class QuestionForm(forms.ModelForm):

    class Meta:
        model=Question
        fields="__all__"

option_choice=[]
def get_option_choices():
    for item in OptionType.objects.all().values_list():
        #print(item)
        choice=(item[0],item[1])
        print(choice)
        option_choice.append(choice)
    #print(option_choice)
    return option_choice

class OptionsForm(forms.Form):

    option=forms.CharField(max_length=100)
    option_type=forms.ChoiceField(choices=(get_option_choices()))
