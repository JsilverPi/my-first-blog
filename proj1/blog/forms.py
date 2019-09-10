from  django import forms
from  .models import Post
from  .models  import Post_M,Comment

class  PostForm(forms.ModelForm):
  class Meta:
    model = Post_M
    fields=('title','abstract','text','file_name')

class  CommentForm(forms.ModelForm):

  class Meta:
    model=Comment
    fields=('author','text')

