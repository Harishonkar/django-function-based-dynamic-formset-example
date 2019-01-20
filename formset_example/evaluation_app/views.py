from django.shortcuts import render,HttpResponse
from .models import Question,Options,OptionType
#from .forms import OptionsFormSet
from .forms import OptionsForm,QuestionForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.forms import inlineformset_factory
from django.forms.models import modelformset_factory
from django.forms.models import formset_factory


def add_question(request):
    extra_forms = 2
    form=QuestionForm(request.POST or None)
    OptionFormSet = formset_factory(OptionsForm)
    if request.method == 'POST':
        question=form.save(commit=False)
        question.save()
        print("Question......",question)


        formset = OptionFormSet(request.POST)
        print("formset......",formset)
        for fo in formset:
            opt=fo.cleaned_data.get('option')
            opt_type=fo.cleaned_data.get('option_type')
            print("opt_type.....",opt_type)
            get_opt_type=OptionType.objects.get(id=int(opt_type))
            Options.objects.create(options=opt,question=question,option_type=get_opt_type)

        return HttpResponse("gfbfhghgch")




    return render(request,'question_form.html',{'form':form,'formset':OptionFormSet})




def update_question(request,id):
    extra_forms = 2

    get_question=Question.objects.get(id=id)
    form=QuestionForm(request.POST or None,instance=get_question)
    formset_options=Options.objects.filter(question=get_question)
    print(formset_options)
    link_data = [{'option': l.options, 'option_type': l.option_type.get_options()}
                    for l in formset_options]
    print("link_data.....",link_data)
    OptionFormSet = formset_factory(OptionsForm)
    if request.method == 'POST':
        question=form.save(commit=False)
        question.save()
        print("Question......",question)


        formset = OptionFormSet(request.POST)
        print("formset......",formset)
        #print("method......",formset.method)
        for fo in formset:
            opt=fo.cleaned_data.get('option')
            opt_type=fo.cleaned_data.get('option_type')

            get_opt_type=OptionType.objects.get(id=opt_type)
            print("get_opt type.....",get_opt_type)
            #print("get_opt_type.......",get_opt_type.get_options())
            get_options=Options.objects.filter(option_type=get_opt_type,options=opt)
            print("get option...obj..",get_options)
            if not get_options:
                Options.objects.create(options=opt,question=question,option_type=get_opt_type)

        return HttpResponse("gfbfhghgch")


    context={
    'form':form,
    'formset':OptionFormSet(initial=link_data)
    }

    return render(request,'question_form.html',context)








'''def CreateQuestionAnswer(request):
    #author = Author.objects.get(pk=author_id)

    OptionsFormSet = inlineformset_factory(Question, Options, fields=('options',),extra=1)
    if request.method == "POST":
        question=request.POST.get('question_name')
        get_question=Question.objects.get(id=question)
        get_question.save()
        formset = OptionsFormSet(request.POST, instance=get_question)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponse("<p>dfgfhfhgdfsaaddsfdgfhg...........</p>")
    else:
        formset = OptionsFormSet(instance=get_question)
        form= OptionsForm()
        print(form)
    return render(request, 'manage_books.html', {'form':form,'options': formset})'''




# Create your views here.
class CreateQuestionAnswer(CreateView):
    model=Question
    fields='__all__'
    success_url=reverse_lazy('success')
    template_name='question_form.html'

    def get_context_data(self, **kwargs):
        data = super(CreateQuestionAnswer, self).get_context_data(**kwargs)
        if self.request.POST:
            data['options'] = OptionsFormSet(self.request.POST)
            data1 = OptionsFormSet(self.request.POST,instance=self.object)
            print("data1..................",data1)
        else:
            data['options'] = OptionsFormSet(instance=self.object)
        return data


    def form_valid(self, form):
        context = self.get_context_data()
        options = context['options']
        print("options--------",type(options))
        print("option instance ----",options.instance)
        #with transaction.atomic():
        question=form.save()

        if options.is_valid():
        #options=formset.save(commit=False)
            for idx,option in enumerate(options):
                a="options_set-{}-options".format(idx)
                option.cleaned_data[a]
                option.instance=question
                print("options.........",option.options)
                option.save()
        return super(CreateQuestionAnswer, self).form_valid(form)

def success(request):
    return HttpResponse("<h1>fhghgjggdfsdg</h1>")
