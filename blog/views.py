from django.shortcuts import render

# Create your views here.

# blog/views.py
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.shortcuts import get_object_or_404
class BlogListView(ListView):
    model = Post
    template_name = "home2.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):  #
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class ListAndCreate(CreateView):
    model = Post
    template_name = "list_and_create.html"
    fields = ["title", "author", "body"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        print(context["objects"])
        return context

def function_based_list_and_create(request):
    context = {}
    print(request)
    context["objects"] = Post.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "function_based_create_and_list.html", context)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

def BlogListDeleteView(request):
    context={}
    context["post_list"] = Post.objects.all()

    if request.method=="POST":
        #print("#@", request.POST.getlist("checkbox_delete"))
        to_delete_list =  request.POST.getlist("checkbox_delete")
        to_delete_objects = Post.objects.filter(pk__in=to_delete_list)
        to_delete_objects.delete()
        #print(to_delete_objects)
    return render(request, "home2_delete.html", context)


