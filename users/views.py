from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect,reverse, render, get_object_or_404
from django.urls import reverse_lazy
from .forms import CreateUserForm,UpdateUserForm

class CreateUser(CreateView):
    model = User
    form_class = CreateUserForm

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.is_staff = True
        print(obj.id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('login')

class UpdateUser(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('index')