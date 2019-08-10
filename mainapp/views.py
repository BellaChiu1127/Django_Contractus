from django.shortcuts import render
from django.http import HttpResponse
from .models import Sign, ContractUs
from .forms import ContractUsForm
# Create your views here.
def mainapp_index(request):
    mainapp_list = Sign.objects.all()
    context = {'mainapp_list' : mainapp_list}
    return render(request,'index.html',context)
def contract_us(request):
    form = ContractUsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContractUsForm()

    context = {
        'form' : form
    }
    return render(request, "index.html",context)