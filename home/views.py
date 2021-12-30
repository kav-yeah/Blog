from django.urls import reverse_lazy
from django.views.generic import DetailView,ListView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='home.html'
    context_object_name ='Posts'
class NewPostView(CreateView):
    model=Post
    template_name = 'post_new.html'
    fields = '__all__'

class PostdetailView(DetailView):
    model=Post
    template_name = 'post_details.html'

class PostEditView(UpdateView):
    model =Post
    template_name ="postedit.html"
    fields =["title","content"]

class PostDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url = reverse_lazy('home')

# -------------------------------------------------User Authentication ---------------------------------------------

