
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import singup_form , login_form
from home.models import Post
# Create your views here.


class singup_view(View):
    form_class = singup_form
    template_class = 'account/singup.html'

    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request,*args,**kwargs)
        
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_class,{'form':form})
    
    def post(self,reqeust):
        form = self.form_class(reqeust.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(reqeust,'Account created successfully','success')
            return redirect('home:home')
        return render(reqeust,self.template_class,{'form':form})
    
class login_view(View):
    form_class = login_form
    template_class = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_class,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'Account login successfully','success')
                return redirect('home:home')
            else:
                messages.error(request,'Youre password or username is not exist!','warning')
            return render(request,self.template_class,{'form':form})


#Log-out button on Navbar 

class logout_view(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'You are logout successfully','success')
        return redirect('home:home')
    

class profile_view(LoginRequiredMixin,View):
    def get(self,reqeust,user_id):
        user = User.objects.get(id = user_id)
        posts = Post.objects.filter(user = user)
        return render(reqeust,'account/profile.html',{'user':user, 'posts':posts})
    