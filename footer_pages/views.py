from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from .forms import CreatePageForm

class PageDetailView(DetailView):

    queryset = Page.objects.all()

    # template_name='speakers/about-speaker.html'

    def get_object(self):
        page = super().get_object()
        return page

class PageUpdateView(UpdateView):
    model = Page
    form_class = CreatePageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('index')

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('index')
