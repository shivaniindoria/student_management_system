from django.shortcuts import render

# Create your views here.
def LoginView(request):
    return render(request,'login.html')
def SignUpView(request):
    return render(request,'signup.html')
def ForgotPasswordView(request):
    return render(request,'forgot-password.html')
def PasswordResetView(request):
    return render(request,'password-reset.html')