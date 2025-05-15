from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from .models import Blog, Comments, Reply
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-date')[:4]
    context ={
        'data' : blogs
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    page =1
    if request.GET:
        page = request.GET.get('page', 1)
    blogs = Blog.objects.order_by('-date')
    blog_paginator = Paginator(blogs, 1)
    blog_list = blog_paginator.get_page(page)
    context ={
        'data' : blog_list
    }
    return render(request,'blog.html', context)
def blogcontent(request, pk):
    content = Blog.objects.get(pk=pk)
    comments = Comments.objects.filter(bloparent=content.pk).order_by('-created_at')
    replies_dict = {}
    for comment in comments:
        comment.replies = Reply.objects.filter(commentParent=comment).order_by('created_at')
        # replies_dict[comment.id] = replies
    
    print(replies_dict)
    # Ensure content.date is a `date` object
    current_date = content.date

    # Get next blog by date (newer)
    next_post = Blog.objects.filter(date__gt=current_date).order_by('date').first()

    # Get previous blog by date (older)
    previous_post = Blog.objects.filter(date__lt=current_date).order_by('-date').first()
    context ={
        'data': content,
        'next_post': next_post,
        'previous_post': previous_post,
        'comment':comments,
        
    }
    return render(request, 'blogcontent.html', context)

def comment(request):
    if request.method =='POST':
        blog_id = request.POST.get('blog_id')
        name= request.POST.get('name')
        email = request.POST.get('email')
        message= request.POST.get('message')
        blog_id = Blog.objects.get(pk=blog_id)
        Comments.objects.create(name=name, bloparent=blog_id, email=email, message=message)
        messages.success(request, 'Comment added successfully!!!!')
    return redirect(f'blogcontent/{blog_id.pk}')

@login_required
def replies(request):
    if request.method == "POST":
        if not request.user.is_staff: 
            return HttpResponseForbidden("You are not authorized to reply.")
        
        cmntid = request.POST.get('commentid')
        reply = request.POST.get('message')

        comment_obj = Comments.objects.get(id=cmntid)

        # Save reply with default admin name (or use request.user.username if you prefer)
        Reply.objects.create(
            commentParent=comment_obj,
            replymsg=reply
        )
    return redirect('blogcontent', pk=comment_obj.bloparent.pk)
        
def contctmessage(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        send_mail(
            subject,
            full_message,
            email,  # from email
            ['fathimariswana024@example.com'],  # to email (your email)
        )

        messages.success(request, "Message sent successfully!")
        return redirect('contact')  # redirect to the contact page again

    return render(request, 'contact.html')


    