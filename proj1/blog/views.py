from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models  import Post
from .models  import Post_M,Comment
from  django.utils  import timezone
from  .forms import PostForm
from  django.shortcuts import redirect
from .forms import CommentForm
from  django.db.models import F

# Create your views here.

def post_list_c(request):

   posts_a=Post_M.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   posts=Post_M.objects.order_by(F('published_date').desc(nulls_last=True)).all()[:1]
   return  render(request,'blog/post_list_c.html',{'posts': posts , 'posts_a':posts_a})


def post_blog(request):
   return  render(request,'blog/post_blog.html')

@login_required
def post_members(request):
   return  render(request,'blog/post_members.html')

def post_list(request):
#
#
   posts_a=Post_M.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#  post_last=Post_M.objects.order_by('published_date').last()
   posts=Post_M.objects.order_by(F('published_date').desc(nulls_last=True)).all()[:1]
#  return  render(request,'blog/post_list.html',{'posts': posts, 'post_last':post_last})
   return  render(request,'blog/post_list.html',{'posts': posts , 'posts_a':posts_a})
def post_detail(request,pk):
  post=get_object_or_404(Post_M,pk=pk)
  return  render(request,'blog/post_detail.html',{'post': post})

@login_required
def post_new(request):
  if request.method == "POST":
       form=PostForm(request.POST)
       if form.is_valid():
          post = form.save(commit=False)
          post.author=request.user
# 09052019
#          post.published_date=timezone.now()
          post.save()
          return  redirect('post_detail',pk=post.pk)

  else:
          form=PostForm()

 
  return  render(request,'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request,pk):
  post=get_object_or_404(Post_M,pk=pk)
  if request.method=="POST":
     form = PostForm(request.POST,instance=post)
     if form.is_valid():
         post=form.save(commit=False)
         post.author=request.user
# 09052019
#         post.published_date=timezone.now()
         post.save()
         return  redirect('post_detail', pk=post.pk)
  else:
         form=PostForm(instance=post)


  return render(request,'blog/post_edit.html',{'form': form})


@login_required
def post_draft_list(request):
#attention not created_date, create_date)
    posts=Post_M.objects.filter(published_date__isnull=True).order_by('create_date')
    return render(request,'blog/post_draft_list.html',{'posts':posts})

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post_M,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)

 
@login_required
def  post_remove(request,pk):
    post=get_object_or_404(Post_M,pk=pk)
    post.delete()
    return  redirect('post_list')

def add_comment_to_post(request,pk):
    post=get_object_or_404(Post_M,pk=pk)
    if request.method=="POST":
       form=CommentForm(request.POST)
       if  form.is_valid():
          comment=form.save(commit=False)
          comment.post=post
          comment.save()
          return  redirect('post_detail',pk=post.pk)
    else:
       form=CommentForm()

    return  render(request, 'blog/add_comment_to_post.html',{ 'form':form})

@login_required
def comment_approve(request,pk):
     comment=get_object_or_404(Comment,pk=pk)
     comment.approve()
     return  redirect('post_detail',pk=comment.post.pk)

@login_required
def  comment_remove(request,pk):
  comment=get_object_or_404(Comment,pk=pk)
  comment.delete()
  return  redirect('post_detail',pk=comment.post.pk)

def  about(request):
  return  render(request,'blog/about.html')

