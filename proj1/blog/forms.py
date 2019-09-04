from  django import forms
from  .models import Post
from  .models  import Post_M

class  PostForm(forms.ModelForm):
  class Meta:
    model = Post_M
    fields=('title','abstract','text','file_name')

