from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Pogar, Sevsk
from .forms import PostForm, PogarForm, SevskForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def pogar_list(request):
    pogars = Pogar.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/pogar/pogar_list.html', {'pogars': pogars})
def pogar_detail(request, pk):
    pogar = get_object_or_404(Pogar, pk=pk)
    return render(request, 'blog/pogar/pogar_detail.html', {'pogar': pogar})

def sevsk_list(request):
    sevsks = Sevsk.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/sevsk/sevsk_list.html', {'sevsks': sevsks})
def sevsk_detail(request, pk):
    sevsk = get_object_or_404(Sevsk, pk=pk)
    return render(request, 'blog/sevsk/sevsk_detail.html', {'sevsk': sevsk})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
