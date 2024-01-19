

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    try:
         name=request.session['Name']
         request.session.modified=True
         return render(request,'app/home.html',{'data':name})
    except:
        return render(request,'app/home.html')
        

def about(request):
    try:
        
        name=request.session['Name']
        request.session.modified=True
        return render(request,'app/about.html',{'data':name})
    except:
        return render(request,'app/about.html')
        


def contact(request):
    try:
        name=request.session['Name']
        request.session.modified=True
        return render(request,'app/contact.html',{'data':name})
    except:
        return render(request,'app/contact.html')
        
    
def service(request):
    try:
        name=request.session['Name']
        request.session.modified=True
        return render(request,'app/service.html',{'data':name})
    except:
        return render(request,'app/service.html')
        


def register(request):
    try:            
        return render(request,'app/register.html')    
    except:
        return render(request,'app/register.html')
        



def savedata(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    city=request.POST['city']
    password=request.POST['password'] 
    request.session['Name']=name
    request.session['Email']=email
    request.session['Contact']=contact
    request.session['City']=city
    request.session['Password']=password
    return render(request,'app/login.html')

def login(request):
    return render(request,'app/login.html')

def logindata(request):
    EmailId=request.POST['email']
    Password=request.POST['password']
    print(EmailId)
    print(Password)
    try :
        email_id=request.session['Email']
        pwd=request.session['Password']
    
        if EmailId==email_id and Password==pwd:
            name=request.session['Name']
            request.session.modified=True    
            return render(request,'app/home.html',{'data':name})    
        else:
            return render(request,'app/home.html') 
    except :
            msg='!!! your session expired... !!'
            return render(request,'app/home.html',{'data1':msg}) 
    
def logout(request):
    del request.session['Name']
    del request.session['Email']
    del request.session['Contact']
    del request.session['City']
    del request.session['Password']
    request.session.flush()
    return render(request,'app/home.html')
    
    
    
    
    
    
    