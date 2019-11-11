from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
from speakers.models import Speaker
from .forms import CreatePostForm
# Create your views here.
class Blogs(ListView):
    model = Blog
    template_name = 'blogs/blog.html'

class Post(DetailView):
    queryset = Blog.objects.all()

    template_name='blogs/blog_detail.html'

    def get_object(self):
        post = super().get_object()
        return post

class CreatePost(CreateView):
    model = Blog
    form_class = CreatePostForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        speaker = Speaker.objects.get(user_id=self.request.user.id)
        obj.speaker = speaker
        return super().form_valid(form)

class UpdatePost(UpdateView):
    model = Blog
    form_class = CreatePostForm
    template_name_suffix = '_update_form'


class DeletePost(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')
