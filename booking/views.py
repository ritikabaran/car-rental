from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from booking.models import *
from django.views.decorators.csrf import csrf_exempt #include this 
import random
def welcome(request):
    template=loader.get_template("welcome.html")
    res=template.render()
    return HttpResponse(res)

def signup(request):
    template=loader.get_template("signup.html")
    res=template.render()
    return HttpResponse(res)

@csrf_exempt # include  this
def store_user(request):
    if request.method=='POST':
        username=request.POST['username']
        if(len(User.objects.filter(username=username))):
            msg='username already taken ....try another username'
            context={
                'msg':msg
            }
            template=loader.get_template("signup.html")
            res=template.render(context,request)
            return HttpResponse(res)
        else:
            user=User()
            user.username=username
            user.password=request.POST['password']
            user.name=request.POST['name']
            user.save()
            template=loader.get_template("store_user.html")
            res=template.render()
            return HttpResponse(res)
    else:
        msg='invalid request......first signup'
        context={
            'msg':msg
        }
        template=loader.get_template("signup.html")
        res=template.render(context,request)
        return HttpResponse(res)
    
@csrf_exempt # include  this
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if(len(User.objects.filter(username=username))):
            user=User.objects.filter(username=username)
            if(len(user.filter(password=password))):
                request.session['username']=username # login success then ...
                user_data=User.objects.filter(username=username)
                profile_data=Profile.objects.filter(username=username)
                context={
                    'user_data':user_data,
                    'profile_data':profile_data
                }
                template=loader.get_template("homepage.html")
                res=template.render(context,request)
                return HttpResponse(res)
            else:
                msg='incorrect password.......login again'
                context={
                    'msg':msg
                }
                template=loader.get_template("login.html")
                res=template.render(context,request)
                return HttpResponse(res)
        else:
            msg='incorrect username........login again'
            context={
                'msg':msg
            }
            template=loader.get_template("login.html")
            res=template.render(context,request)
            return HttpResponse(res)
    else:
        template=loader.get_template("login.html")
        res=template.render()
        return HttpResponse(res)

def homepage(request):
    if 'username' not in request.session.keys(): # session dict with key and value
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    else:
        username=request.session['username']
        user_data=User.objects.filter(username=username)
        profile_data=Profile.objects.filter(username=username)
        context={
            'user_data':user_data,
            'profile_data':profile_data
        }
        template=loader.get_template("homepage.html")
        res=template.render(context,request)
        return HttpResponse(res)

def profile(request):
    template=loader.get_template("profile.html")
    res=template.render()
    return HttpResponse(res)

@csrf_exempt # include  this
def profile_save(request):
    if request.method=='POST':
        username=request.session.get('username')
        if(len(User.objects.filter(username=username))):
            profile=Profile()
            profile.username=User.objects.get(username=username)
            profile.fathers_name=request.POST['father_name']
            profile.mothers_name=request.POST['mother_name']
            profile.phone=request.POST['phone']
            profile.email=request.POST['email']
            profile.address=request.POST['address']
            profile.save()
            user_data=User.objects.filter(username=username)
            profile_data=Profile.objects.filter(username=username)
            context={
                'user_data':user_data,
                'profile_data':profile_data
            }
            template=loader.get_template("homepage.html")
            res=template.render(context,request)
            return HttpResponse(res)
        else:
            msg='incorrect username ,profile not updated'
            context={
                'msg':msg
            }
            template=loader.get_template("profile.html")
            res=template.render(context,request)
            return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    
def logout(request):
    del request.session['username'] #must destroy session keys
    template=loader.get_template("welcome.html")
    res=template.render()
    return HttpResponse(res)

@csrf_exempt # include  this
def result(request):
    if 'username' in request.session.keys():
        book_from=request.POST['book_from']
        request.session['book_from']=book_from ##book_from
        book_to=request.POST['book_to']
        request.session['book_to']=book_to  ##book_to
        date=request.POST['date']
        request.session['date']=date  ##date
        from_to_data=from_to.objects.filter(book_from=book_from)
        from_to_data=from_to_data.filter(book_to=book_to)
        from_to_data=from_to_data.filter(date=date)
        context={
            'from_to_data':from_to_data
        }
        template=loader.get_template("result.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)


def book(request):
    if 'username' in request.session.keys():
        template=loader.get_template("booking_page.html")
        res=template.render()
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    
def result2(request):
    if 'username' in request.session.keys():
        username=request.session['username']
        car=request.POST['car']
        book_from=request.session['book_from']
        book_to=request.session['book_to']
        date=request.session['date']
        dist=from_to.objects.filter(book_from=book_from)
        dist=from_to.objects.filter(book_to=book_to)
        for ele in dist:
            km=ele.km
        l=['1','2','3','4','5','6','7','8','9','A','B','R','H','I','H']
        random.shuffle(l)
        perfix=''
        for e in range(3):
            perfix=perfix+l[e]
        book_id=perfix+username
        price=carPrice.objects.filter(car=car)
        for ele in price:
            perKmPrice=ele.perKmPrice
        price=perKmPrice*km
        context={
            'book_from':book_from,
            'book_to':book_to,
            'km':km,
            'date':date,
            'car':car,
            'book_id':book_id,
            "price":price,
            'perKmPrice':perKmPrice,
            'price':price
        }
        data=bookHistory()
        data.book_id=book_id
        data.username=User.objects.get(username=username)
        data.book_from=book_from
        data.book_to=book_to
        data.car=car
        data.price=price
        data.save()
        template=loader.get_template("result2.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
    
def history(request):
    if 'username' in request.session.keys():
        username=request.session['username']
        data=bookHistory.objects.filter(username=username)
        context={
            'data':data
        }
        template=loader.get_template("history.html")
        res=template.render(context,request)
        return HttpResponse(res)
    else:
        template=loader.get_template("welcome.html")
        res=template.render()
        return HttpResponse(res)
 
def about(request):
    template=loader.get_template("about.html")
    res=template.render()
    return HttpResponse(res)

def contact(request):
    template=loader.get_template("contact.html")
    res=template.render()
    return HttpResponse(res)