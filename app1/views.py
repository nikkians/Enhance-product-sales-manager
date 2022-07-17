from django.http import HttpResponse
from django.shortcuts import render, redirect
from app1.models import Company_Details, Company_Customers, Company_Product
from django.db.models import Q
import random
# Create your views here.
# ------------------------------------- Company ---------------------

def Company_Login(request):
    if request.POST:
        em = request.POST['email']
        pass1 = request.POST['pass']
        print(em, pass1)
        
        try:
            var = Company_Details.objects.get(c_email = em)
            print(var)
            if var.c_pass == pass1:
                request.session['com_data'] = var.id
                return redirect('Profile_Manage')
            else:
                return HttpResponse("<h1><a href=""> You Have Entered Wrong Password </a></h1>")    
        except:
            return HttpResponse("<h1><a href=""> Email Id Is Not Registered </a></h1>")
    return render(request,'company/login/login.html')

def Company_Regi(request):
    if request.POST:
        nm = request.POST['name']
        em = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        
        try:
            var = Company_Details.objects.get(c_email = em)
            return HttpResponse("<h1><a href=""> Email Id Already Registered... </a></h1>")    
        except:
            if pass1 == pass2:
                obj = Company_Details()
                obj.c_name = nm
                obj.c_email = em
                obj.c_pass = pass2
                obj.save()
                return redirect('c_login')
    return render(request,'company/login/regi.html')

def Profile_Manage(request):
    if 'com_data' in request.session.keys():
        comp = Company_Details.objects.get(id = int(request.session['com_data']))
        if request.POST:
            nm = request.POST['nm1']
            em = request.POST['em1']
            con = request.POST['con1']
            add1 = request.POST['add1']
            pass1 = request.POST['pass1']
            img1 = request.FILES.get('img1')
            
            comp.c_name = nm
            comp.c_email = em
            comp.c_cno = con
            comp.c_add = add1
            comp.c_pass = pass1
            print(img1)
            if img1 != None:
                comp.profile = img1
            
            comp.save()
            # return redirect('CompDashBoard')
        return render(request,'company/dash/Profile.html',{'USERS':comp})
    else:
        return redirect('c_login')

def AddCompCustom(request):
    if 'com_data' in request.session.keys():
        comp = Company_Details.objects.get(id = int(request.session['com_data']))
        if request.POST:
            nm = request.POST['nm1']
            em = request.POST['em1']
            con = request.POST['con1']
                
            obj = Company_Customers()
            obj.comp = comp
            obj.cust_nm = nm
            obj.cust_em = em
            obj.cust_con = con
            
            # Password Create---------
            salfa = 'qwertyuiopasdfghjklzxcvbnm'
            ualfa = salfa.upper()
            spic = '!@#$%^&*()'
            num = '1234567890'
            data = salfa + ualfa + spic + num
            otp = ""
            for i in range(8):
                otp += str(random.choice(data))
                print(otp)
            print(otp)
            
            obj.cust_pass = otp
            obj.save()    
        return render(request,'company/dash/add_custom.html',{'USERS':comp})
    else:
        return redirect('c_login')

def ViewCustomers(request):
    if 'com_data' in request.session.keys():
        comp_user = Company_Details.objects.get(id = int(request.session['com_data']))
        custs = Company_Customers.objects.filter(comp=comp_user)
        print(custs)
        return render(request,'company/dash/view_customer.html',{'USERS':comp_user,'cust':custs})
    else:
        return redirect('c_login')

def DeleteCustomer(request,id):
    if 'com_data' in request.session.keys():
        custs = Company_Customers.objects.get(id=id)
        custs.delete()
        return redirect('ViewCustomers')
    else:
        return redirect('c_login')

def AddProduct(request):
    if 'com_data' in request.session.keys():
        comp = Company_Details.objects.get(id = int(request.session['com_data']))
        if request.POST:
            nm = request.POST['nm1']
            pr = request.POST['pr1']
            qty = request.POST['qty1']
            img = request.FILES.get('img1')
            
            var = Company_Product()
            var.comp = comp
            var.prod_nm = nm
            var.prod_price = pr
            var.prod_qty = qty
            var.prod_img = img
            var.save()
            return redirect('ViewProduct')
        return render(request,'company/dash/add_product.html',{'USERS':comp})
    else:
        return redirect('c_login')

def UpdateProduct(request,id):
    if 'com_data' in request.session.keys():
        comp = Company_Details.objects.get(id = int(request.session['com_data']))
        prod = Company_Product.objects.get(id = id)
        if request.POST:
            nm = request.POST['nm1']
            pr = request.POST['pr1']
            qty = request.POST['qty1']
            img = request.FILES.get('img1')
            
            prod.comp = comp
            prod.prod_nm = nm
            prod.prod_price = pr
            prod.prod_qty = qty
            if img != None:
                prod.prod_img = img
            prod.save()
            return redirect('ViewProduct')
        return render(request,'company/dash/update_product.html',{'USERS':comp,'prod':prod})
    else:
        return redirect('c_login')

def ViewProduct(request):
    if 'com_data' in request.session.keys():
        comp = Company_Details.objects.get(id = int(request.session['com_data']))
        prods = Company_Product.objects.filter(comp = comp)
        q=request.GET.get('search')
        if q:
            pr=Company_Product.objects.filter(Q(prod_nm__icontains=q)| Q(prod_price__icontains=q))
            return render(request,'company/dash/view_product.html',{'USERS':comp,'pr':pr})

        return render(request,'company/dash/view_product.html',{'USERS':comp,'prod':prods})
    else:
        return redirect('c_login')



def DeleteProduct(request,id):
    if 'com_data' in request.session.keys():
        prod = Company_Product.objects.get(id = id)
        prod.delete()
        return redirect('ViewProduct')
    else:
        return redirect('c_login')

# 
def ComLogout(request):
    if 'com_data' in request.session.keys():
        del request.session['com_data']
        return redirect('c_login')
    else:
        return redirect('c_login')

# ------------------------------------- Company ---------------------

# ------------------------------------- Customer ---------------------

def Customer_Login(request):
    if request.POST:
        em = request.POST['email']
        ps = request.POST['pass']
        
        try:
            valid = Company_Customers.objects.get(cust_em = em, cust_pass = ps)
            request.session['custom_user'] = valid.id
            return redirect('Customer_dash')
        except:
            return redirect('Customer_Login')
        
    return render(request,'customer/login/login.html')

def Customer_Signup(request):
    if request.POST:
        nm = request.POST['name']
        em = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        
        try:
            var = Company_Customers.objects.get(cust_em = em)
            return HttpResponse("<h1><a href=""> Email Id Already Registered... </a></h1>")    
        except:
            if pass1 == pass2:
                obj = Company_Customers()
                obj.cust_nm = nm
                obj.cust_em = em
                obj.cust_pass = pass2
                obj.save()
                return redirect('Customer_Login')
    return render(request,'customer/login/signup.html')

def Customer_dash(request):
    if 'custom_user' in request.session.keys():
        prod = Company_Product.objects.all()
        return render(request,'customer/dash/index.html',{'prod':prod})
    else:
        return redirect('Customer_Login')

def profile(request):
    if 'custom_user' in request.session.keys():
        cust = Company_Customers.objects.get(id = int(request.session['custom_user']))
        if request.POST:
            nm = request.POST['nm']
            em = request.POST['em']
            con = request.POST['cno']
            pa1 = request.POST['pass']
            img1 = request.FILES.get('img1')
            ad1 = request.POST['ad1']
            ad2 = request.POST['ad2']
            
            cust.cust_nm = nm
            cust.cust_em = em
            cust.cust_con = con
            cust.cust_add1 = ad1
            cust.cust_add2 = ad2
            cust.cust_pass = pa1
            if img1 != None:
                cust.cust_profile = img1
            cust.save()
        return render(request,'customer/dash/profile.html',{'cust':cust})
    else:
        return redirect('Customer_Login')

def Customer_logout(request):
    if 'custom_user' in request.session.keys():
        request.session['custom_user']
        return redirect('Customer_Login')    
    else:
        return redirect('Customer_Login')    

# ------------------------------------- Customer ---------------------

