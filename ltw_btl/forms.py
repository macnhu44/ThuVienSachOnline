from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
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
    
    key = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nhập mã xác thực...'}), 
                          max_length=6, 
                          required=True)
        
        
    def __init__(self, *args, **kwargs):
        super (confirmCodeMailForm, self).__init__(*args, **kwargs)
        # self.fields['username'].disabled = True
        

class ResetPasswordForm (SetPasswordForm):
        
    def __init__(self, *args, **kwargs):
        super (ResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "Nhập mật khẩu mới:"
        self.fields['new_password2'].label = "Nhập lại mật khẩu:"
        
        
