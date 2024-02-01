
from django.contrib.auth.models import User
from product.models import Product
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from product.models import Product,Cart,Order,deatail
from django.contrib import  messages
from django.views import View
from product.forms import RegistrationForm,LoginForm,Forgot,DetailForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


class Registration(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'regi.html',{'form':form})
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            messages.success(request,'Congratulations! Registered Sucessfully')
        return render(request,'regi.html',{'form':form}) 

class CustomLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the home page or any other desired page after login
                return redirect('home')
            else:
                return render('regi')
        else:
            return render(request, 'login.html', {'form': form})   

def home(request):
    return render(request,'home.html')
        
def saree(request):
    sarees=Product.objects.filter(category='SA')
    return render(request,'saree.html',{'sarees':sarees})

def mentopwear(request):
    topwears=Product.objects.filter(category='MTW')
    return render(request,'mentop.html',{'topwear':topwears})

def menbottomwear(request):
    bw=Product.objects.filter(category='MBW')
    print(bw)
    return render(request,'menbott.html',{'b':bw})

def menfootwear(request):
    fw=Product.objects.filter(category='MFW')
    return render(request,'menfoot.html',{'f':fw})

def womentopwear(request):
    wt=Product.objects.filter(category='WTW')
    return render(request,'womentop.html',{'w':wt})

def womenbottomwear(request):
    wb=Product.objects.filter(category='WBW')
    print(wb)
    return render(request,'womenbott.html',{'w':wb})

def womenfootear(request):
    wf=Product.objects.filter(category='WFW')
    print(wf)
    return render(request,'womenfoot.html',{'w':wf})

def softtoys(request):
    sf=Product.objects.filter(category='SFT')
    print(sf)
    return render(request,'softtoys.html',{'s':sf})

def kiddress(request):
    kd=Product.objects.filter(category='DRE')
    print(kd)
    return render(request,'kiddress.html',{'kd':kd})

def kidfootware(request):
    kf=Product.objects.filter(category='KF')
    print(kf)
    return render(request,'kidfoot.html',{'kf':kf})

def stickers(request):
    st=Product.objects.filter(category='ST')
    print(st)
    return render(request,'stickers.html',{'st':st})

def clocks(request):
    cl=Product.objects.filter(category='CL')
    print(cl)
    return render(request,'clocks.html',{'cl':cl})

def showpiece(request):
    sp=Product.objects.filter(category='SP')
    print(sp)
    return render(request,'showpiece.html',{'sp':sp})

def kitchen(request):
    ks=Product.objects.filter(category='KS')
    print(ks)
    return render(request,'kitchen.html',{'ks':ks})

def makeup(request):
    mk=Product.objects.filter(category='MAKE')
    print(mk)
    return render(request,'makeup.html',{'mk':mk})

def skincare(request):
    sk=Product.objects.filter(category='SC')
    print(sk)
    return render(request,'skincare.html',{'sk':sk})

def haircare(request):
    ha=Product.objects.filter(category='HA')
    print(ha)
    return render(request,'haircare.html',{'ha':ha})

def fragrance(request):
    fr=Product.objects.filter(category='FR')
    print(fr)
    return render(request,'fragrance.html',{'fr':fr})

def mobile(request):
    mb=Product.objects.filter(category='MOB')
    print(mb)
    return render(request,'mobile.html',{'mb':mb})

def smartwatch(request):
    sw=Product.objects.filter(category='SW')
    print(sw)
    return render(request,'smartwatch.html',{'sw':sw})







def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'productdetail.html', {'product': product})


from django.contrib.auth.models import AnonymousUser

def add_to_cart(request,id):
    user=request.user
    if user.is_authenticated:
        product=Product.objects.get(id=id)
        Cart(user=user,product=product).save()
        return redirect('showcart')
    else:
        return redirect('login')

@login_required 
def view_cart(request):
    
    if request.user.is_authenticated:
        user=request.user 
        cart=Cart.objects.filter(user=user)
        amount=0
        shipping_amount=70
        total_amount=0
        cart_product=[p for p in Cart.objects.filter(user=user) if p.user==user]
        
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.price)
                amount+=tempamount
            total_amount=amount+shipping_amount
            return render(request,'showcart.html',{'carts':cart,'total':total_amount,'sa':shipping_amount})    
        else:
            return render(request,'emptycart.html')
        
def forgot_password(request):
    if request.method == 'POST':
        form = Forgot(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']
            if new_password != confirm_password:
                messages.warning(request,'Password didn\'t match')
            else:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                return redirect('login')
    else:
        form = Forgot()

    return render(request, 'forgotpass.html', {'form': form})   

@login_required
def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, id=cart_item_id, user=user)
        cart_item.delete()
        return redirect('showcart')
    else:
        return redirect('login')    

@login_required
def increase_quantity(request,cart_item_id):
    if request.user.is_authenticated:
        user=request.user
        cart_item=get_object_or_404(Cart,id=cart_item_id,user=user)
        cart_item.quantity+=1
        cart_item.save()
        return redirect('showcart')
    else:
        return redirect('login')
    
@login_required 
def decrease_quantity(request, cart_item_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = get_object_or_404(Cart, id=cart_item_id, user=user)
        cart_item.quantity = max(cart_item.quantity - 1, 1)
        cart_item.save()

        return redirect('showcart')
    else:
        return redirect('login')    

    
@login_required 
def placeorder(request):
    if request.user.is_authenticated:
        user=request.user 
        orders=Order.objects.filter(user=user)
        print(orders)
        amount=0
        shipping_amount=70
        total_amount=0
        order_product=[p for p in Order.objects.filter(user=user) if p.user==user]
    
    if order_product:
        for p in order_product:
            tempamount=(p.quantity*p.product.price)
            amount+=tempamount
        total_amount=amount+shipping_amount
        
        return render(request,'buynow.html',{'orders':orders,'total':float(total_amount),'sa':shipping_amount}) 
    else:
        return redirect("home")   
    


def buynow(request,id):
    user=request.user
    if user.is_authenticated:
        product=get_object_or_404(Product,id=id)
        order=Order(user=user,product=product)
        order.save()
        
        order_details = {
        'items': [{'product_id': product.id}],
        }
        if 'orders' not in request.session:
            request.session['orders'] = []
            orders = request.session['orders']
            orders.append(order_details)
            request.session.modified = True    
        return redirect('placeorder')
    else:
        return redirect('login')

@login_required
def continuee(request):
    user = request.user
    if user.is_authenticated:
        cart_items = Cart.objects.filter(user=user)
        order = Order.objects.create(user=user)
        for cart_item in cart_items:
            order.products.add(cart_item.product)
        cart_items.delete()
        return redirect('orderplace')
    else:
        return redirect('login')

    

def orderplace(request):
    user = request.user
    if user.is_authenticated:
        Order.objects.filter(user=user).delete()
    return HttpResponse("placed order successfully")   

@login_required
def increases_quantity(request,order_item_id):
    if request.user.is_authenticated:
        user=request.user
        order_item=get_object_or_404(Order,id=order_item_id,user=user)
        order_item.quantity+=1
        order_item.save()
        return redirect('placeorder')
    else:
        return redirect('login')
    
@login_required 
def decreases_quantity(request, order_item_id):
    if request.user.is_authenticated:
        user = request.user
        order_item = get_object_or_404(Order, id=order_item_id, user=user)
        order_item.quantity = max(order_item.quantity - 1, 1)
        order_item.save()

        return redirect('placeorder')
    else:
        return redirect('login')     

def remove_from_order(request, order_item_id):
    if request.user.is_authenticated:
        user = request.user
        order_item = get_object_or_404(Order, id=order_item_id, user=user)
        order_item.delete()
        return redirect('placeorder')
    else:
        return redirect('login')   


@login_required
def detailform(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            payment_method = form.cleaned_data['payment_method']
            contact_number = form.cleaned_data['contact_number']
            email = form.cleaned_data['email']
            d= deatail(name=name,address=address,payment_method=payment_method,contact_number=contact_number,email=email)
            d.save()
            return redirect('placeorder')
    else:
        form = DetailForm()

    return render(request, 'order.html', {'form': form})

    
         
        

                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    