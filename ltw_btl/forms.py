from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class addBookForm (ModelForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)
    class Meta:
        model  = Book
        fields = '__all__'
        labels = {
            'name' : 'Tiêu đề',
            'author' : 'Tác giả',
            'description' : 'Mô tả',
            'category' : 'Thể loại',
            'release_date' : 'Ngày xuất bản',
            'number_of_pages' : 'Số trang',
            'image' : 'Upload ảnh',
        }
        
    # Ham khoi tao
    def __init__(self, *args, **kwargs):
        super (addBookForm, self).__init__(*args, **kwargs)
        
        self.fields['image'].widget.attrs["onchange"]="readURL(this);"
        

class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name' : 'Tên',
            'last_name' : 'Họ',
            'username' : 'Tên đăng nhập',
            'email' : 'Email',
            'password1' : 'Mật khẩu',
            'password2' : 'Nhập lại mật khẩu',
        }
        
class profileUserForm (ModelForm):
    class Meta:
        model  = User
        fields = ['last_name', 'first_name', 'email']
        labels = {
            'last_name' : 'Họ',
            'first_name' : 'Tên',
            'email' : 'Email',
        }
        
    def __init__(self, *args, **kwargs):
        super (profileUserForm, self).__init__(*args, **kwargs)
        # self.fields['username'].disabled = True
        

class sendMailForm (ModelForm):
    class Meta:
        model  = User
        fields = ['email']
        labels = {
            'email' : 'Email',
        }
        
    def __init__(self, *args, **kwargs):
        super (sendMailForm, self).__init__(*args, **kwargs)
        # self.fields['username'].disabled = True
        
        
        
class confirmCodeMailForm (forms.Form):
    
    key = forms.CharField(max_length=6)
    # class Meta:
    #     model  = User
    #     fields = ['email']
    #     labels = {
    #         'email' : 'Email',
    #     }
        
    def __init__(self, *args, **kwargs):
        super (confirmCodeMailForm, self).__init__(*args, **kwargs)
        # self.fields['username'].disabled = True