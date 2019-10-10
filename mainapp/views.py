from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from .models import Sign, ContractUs
from .forms import ContractUsForm
from django.contrib import auth
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
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/mainapp/')

    username = request.POST.get('loginid','')
    password = request.POST.get('loginpsw','')

    user = auth.authenticate(username=username , password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('index.html')