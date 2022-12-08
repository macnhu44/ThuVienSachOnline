from django.urls import path
from . import views

urlpatterns = [
    # Authenticate path
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logOut, name='logout'),
    
    # HomePage path
    path('', views.getGuestHome, name='guestPage'),
    path('userhome/', views.getUserHome, name='userHome'),
    
    # Product path
    path('addBook/', views.addBook, name='addBook'),
    path('viewBook/<str:pk>/', views.viewBook, name='viewBook'),
    path('editBook/<str:pk>/', views.editBook, name='editBook'),
    path('deleteBook/<str:pk>/', views.deleteBook, name='deleteBook'),
    path('statisticalBook/', views.statisticalBook, name='statisticalBook'),
    
    # User path
    path('profileUser/', views.profileUser, name='profileUser'),
    path('editUser/', views.editUser, name='editUser'),
    path('sendMail/', views.sendMail, name='sendMail'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('confirmCodeMail/', views.confirmCodeMail, name='confirmCodeMail'),
]
