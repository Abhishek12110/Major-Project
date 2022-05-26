from itertools import product
from django.contrib.sessions import *
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import User,auth 
from unicodedata import category
from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    product_objects=Product.objects.all()
    cv=[]
    v=[]
    for ik in product_objects:
        if ik.category not in cv:
            cv.append(ik.category)
            v.append(ik)
    return render(request,'index.html',{'product_objects': product_objects ,'categry': v })

def registerpage(request):
    if request.method == 'POST':
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['Email']
        username = request.POST['username']
        password = request.POST['Password']
        password2 = request.POST['Confirm_password']
        mobile = request.POST['mobile']
        print(first_name,last_name)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already exists")
                return redirect('/register')
            else:
                user = User.objects.create_user(
                email=email, password=password, first_name=first_name,last_name=last_name,username=username)
                user.save()
                print (User.objects)
                print(user)
                print(auth)
                # send_email(request, user)
                messages.info(request, 'User Created Successfully')
                auth.login(request,user)
                return redirect('/')
        else:
            messages.info(request, "Password didn't match")
            return redirect('/register')
    else:
        return render(request,'register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        userpassword = request.POST['userpassword']
        print(username,userpassword)
        print(User)
        any= auth.authenticate(request,username=username,password=userpassword)
        print(any)
        if any is not None:
            auth.login(request, any)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def breadpage(request):
    product_objects=Product.objects.all()
    bread_objects=Product.objects.filter(category__icontains='bread')
    return render(request,'bread.html',{'product_objects': product_objects , 'bread_objects': bread_objects})

def aboutpage(request):
    about_object=About.objects.all().first()
    print(about_object)
    return render(request,'about.html',{'about': about_object})

def cakepage(request):
    cake_objects=Product.objects.filter(category__icontains='cakes')
    return render(request,'cakes.html',{'cakes': cake_objects})


class detailpage(View):
    def get(self,request,id):
        product_object=Product.objects.get(id=id)
        print(request.session.get('cart'))
        return render(request,'detail.html',{'product_object':product_object})

    def post(self,request,id):
        product=request.POST.get('productid') 
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if product:
            if cart:
                quantity=cart.get(product)
                if quantity:
                    cart[product]=quantity+1
                else:
                    cart[product]=1
            else:
                cart={}
                cart[product]=1

        if remove:
            quantity=cart.get(remove)
            if quantity:
                if quantity==1:
                    cart.pop(remove)
                else:
                    cart[remove]=quantity-1
            else:
                pass
        request.session['cart']=cart
        product_object=Product.objects.get(id=id)
        return render(request,'detail.html',{'product_object':product_object})


# def detailpage(request,id):
#     product_object=Product.objects.get(id=id)
#     return render(request,'detail.html',{'product_object':product_object})

class searchpage(View):
    def get(self,request):
        return render(request,'search.html')
    def post(self,request):
        searchitem=request.POST.get('searchitms')
        if(searchitem=="" or searchitem==" "or searchitem=="  "):
            return render(request,'search.html')
        else:
            search_objects=Product.objects.filter(product_name__icontains=searchitem)
            if len(search_objects)>=1:
                return render(request,'search.html',{'searchitems': search_objects})
            else:
                search_objects=Product.objects.filter(category__icontains=searchitem)
                return render(request,'search.html',{'searchitems': search_objects})
def pastriespage(request):
    pastrie_objects=Product.objects.filter(category__icontains='pastries')
    return render(request,'pastries.html',{'pastries': pastrie_objects})

def cookiespage(request):
    cookie_objects=Product.objects.filter(category__icontains='cookies')
    return render(request,'cookies.html',{'cookies': cookie_objects})

def blogpage(request):
    blogs=Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})
    
def contactuspage(request):
    return render(request,'contactus.html')

def orderspage(request):
    return render(request,'orders.html')

class checkoutpage(View):
    def get(self,request):
        print('getmetgod',request.method)
        print(request.POST)
        return render(request,'checkout.html')
    def post(self,request):
        if request.method == 'POST':
            if len(request.session.get('cart'))>=1:
                address = request.POST['address']
                name = request.POST['name']
                email = request.POST['Email']
                mobile = request.POST['mobile']
                customer=self.request.user
                cart=request.session.get('cart')
                ids=request.session.get('cart').keys()
                products=Product.objects.filter(id__in=ids)
                # print(first_name,last_name,address,email,customer,cart,mobile,products)
                items={}
                totalprice=0
                for product in products:
                    x=str(product.id)
                    price=product.price
                    items[product.product_name]=cart[x]
                    totalprice+=price*cart[x]
                    # print(items)
                    # print(cart[x],product.product_name,price,totalprice)
                Order=orderitem(customer=customer,product=items,price=totalprice,name=name,address=address,phone=mobile,email=email)
                Order.placeorder()
                request.session['cart']={}
                return render(request,'checkout.html')
            else:
                return render(request,'index.html')

def cartpage(request):
    product_objects=Product.objects.all() 
    cart=request.session.get('cart')
    if cart:
        ids=request.session.get('cart').keys()
        cartitems=Product.objects.filter(id__in=ids)
        return render(request,'cart.html',{'product_objects':product_objects,'cartitems':cartitems})
    return render(request,'cart.html',{'product_objects':product_objects})