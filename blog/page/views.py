from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import BlogPost, Authors, Comment
from .forms import BlogPostForm,CommentForm

def home(request):
    return HttpResponse("Welcome to the blog.")

def page1(request):
    latest_post=BlogPost.objects.all()
    return render(request,'page1.html',{'latest_post':latest_post})

def view_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'view_post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('latest_post')
    else:
        form = BlogPostForm()  
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('latest_post')
    else:
        form = BlogPostForm(instance=post)
    return render (request, 'edit_post.html',{'form':form})


def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('latest_post'))

def comment_post(request,post_id):
    post=get_object_or_404(BlogPost,id=post_id)
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect ('view_post',post_id=post.id)
    else:
        form=CommentForm()
    return render (request,'add_comment.html', {'form':form,'post':post})



