from django.urls import path

# from . import views as v
from .views import *
urlpatterns = [
    # -------------- company -------------
    path('',Company_Login,name='c_login'),
    path('Company_Regi/',Company_Regi,name='c_regi'),
    path('Profile_Manage/',Profile_Manage,name='Profile_Manage'),
    path('AddCompCustom/',AddCompCustom,name='AddCompCustom'),
    path('ViewCustomers/',ViewCustomers,name='ViewCustomers'),
    path('DeleteCustomer/<int:id>',DeleteCustomer,name='DeleteCustomer'),
    path('ComLogout',ComLogout,name='ComLogout'),
    
    # ---------------- Product
    path('AddProduct/',AddProduct,name='AddProduct'),
    path('ViewProduct/',ViewProduct,name='ViewProduct'),
    path('DeleteProduct/<int:id>',DeleteProduct,name='DeleteProduct'),
    path('UpdateProduct/<int:id>',UpdateProduct,name='UpdateProduct'),
    
    # ---------------- customer --------------
    path('Customer_Login/',Customer_Login,name='Customer_Login'),
    path('Customer_Signup/',Customer_Signup,name='Customer_Signup'),
    path('Customer_dash/',Customer_dash,name='Customer_dash'),
    path('profile/',profile,name='profile'),
    path('Customer_logout/',Customer_logout,name='Customer_logout'),
]
