from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Like
from django.core.mail import send_mail
from .forms import SharedPostForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.db.models import Count
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})


def blog_details(request,pk): 
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post=post.id)
    like = Like.objects.all()
    context = {
        "post":post,
        "comments":comments,
        "like":like
    }
    return render(request,'blogs/details.html',context)

def blog_send_mail(request):
    if request.method == "POST":
        name = request.POST["name"]
        email_field = request.POST["email_field"]
        to_field = request.POST["to_field"]
        comments = request.POST["comments"]

        subject = 'Hello from Django'
        message = 'This is a test email sent using Django.'
        from_email = email_field
        recipient_list = [to_field]
        print(name,from_email)
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse(request,'blogs/details.html')
    else:
        return render(request,'blogs/shared_mail.html')

def sharedMail(request):
    if request.method == "POST":
        name = request.POST["name"]
        email_field = request.POST["email_field"]
        to_field = request.POST["to_field"]
        comments = request.POST["comments"]
        subject = 'Hello from Django'
        message = comments
        from_email = email_field
        recipient_list = [to_field]
        print(name,email_field)
        send_mail(subject, message, from_email, recipient_list)
        return redirect('blogs/details.html')
    else:    
        return render(request, 'blogs/shared_mail.html')

@login_required
def blog_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST,instance=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            name = form.cleaned_data['name']
            text = form.cleaned_data['text'] 
            comment = Comment.objects.create(post=post,author=request.user,text=text,name=name)
            comment.save()
            print(comment)
            return redirect('blogs-details',pk=post.pk)
    else:
        form = CommentForm(instance=request.user)

    return render(request, 'blogs/blog_comments.html', {'post': post, 'form': form})


@login_required
def BlogPostLike(request, pk):
    # post = get_object_or_404(Post, id=pk)
    comment = Comment.objects.filter(id=pk).first()
    post_id = comment.post.id
    post = Post.objects.filter(id=post_id).first()
    like = Like.objects.filter(comment=comment.id,author=request.user).first()
    if like == None:
        Like.objects.create(comment=comment,author=request.user,likes = 1)

        
    else:
        like.delete()
    return redirect('blogs-details',pk=post.id)