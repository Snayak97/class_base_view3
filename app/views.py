from typing import Any, Dict
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import *
from app.models import *
from app.forms import *



class temp(TemplateView):
    template_name='temp.html'
    def get_context_data(self, **kwargs):
        CEDO=super().get_context_data(**kwargs)
        CEDO['name']='SOUMYA'
        return CEDO

# insert from using templateviews 
class form_insert(TemplateView):
    template_name='form_insert.html'
    def get_context_data(self, **kwargs):
        CEDO=super().get_context_data(**kwargs)
        SFO=StudentForm
        CEDO['SFO']=SFO
        return CEDO
        
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('from inserted')

#insert views using fromviews
class StudenFormViews(FormView):
    template_name='StudenFormViews.html'
    form_class=StudentForm
    def form_valid(self, form):
        form.save()
        return HttpResponse('StudenFormViews inserted')
    