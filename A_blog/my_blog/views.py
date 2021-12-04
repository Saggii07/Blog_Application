

from django.views.generic import ListView, DetailView,DeleteView,CreateView,UpdateView
from .models import Post
from django.urls import reverse_lazy
from rest_framework import generics,serializers
from .serializers import PostSerializer
# Create your views here.

class HomeView(ListView):
    model=Post
    template_name='home.html'

class DetailView(DetailView):
    model=Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'post_add.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class UpdateView(UpdateView):
    model=Post
    template_name = 'post_update.html'
    fields = '__all__'

class DeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



###*#*#*#*#*################*#*#*#*#*#*#############*#*##8##8#8##########

"""
here logic of create an api trough content we can create blog content with API 

"""

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListDetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer





