from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from speakers.models import Speaker
from .forms import ContactSpeakerForm
from .models import ContactSpeaker
# Create your views here.
def IndexView(request):
    speakers = Speaker.objects.all()
    form = ContactSpeakerForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        send_mail('Test de mensaje','Hola no respondas a este mensaje','jsitqconf@itq.edu.ec',['gio666nb@gmail.com'])
        return redirect(reverse('index'))


    return render(request,'index.html',{'speakers':speakers,'form':form})