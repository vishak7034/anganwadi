from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.views.generic import TemplateView, View
from django.contrib.auth.models import auth, User

from anganwadi import settings
from anganwadi_app.models import anganawadi, foodtype, tbl_userfood, tbl_userfoodservice, tbl_foodstock, \
    tbl_totalfoodstock, tbl_foodstockrequest, tbl_pwomenfoodservice, tbl_pwomenfood, tbl_pfoodstock, tbl_totalpfoodstock, \
    tbl_pfoodstockrequest, District, prooftype, Place, Location, UserType, tbl_child, child, tbl_healthtips, tbl_user, \
    tbl_pwomens, tbl_foodbooking, tbl_pfoodbooking, tbl_childfoodstock, tbl_totalchildfoodstock, \
    tbl_childfoodstockrequest
from django.shortcuts import redirect, render


class IndexView(TemplateView):
    template_name = 'anganwadi/anganwadi_index.html'

class view_profile(TemplateView):
    template_name = 'anganwadi/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(view_profile,self).get_context_data(**kwargs)
        Anganwadi=anganawadi.objects.get(user_id=self.request.user.id)
        context['Anganwadi']=Anganwadi
        return context

class edit_profile(TemplateView):
    template_name = 'anganwadi/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        Anganwadi=anganawadi.objects.get(user_id=self.request.user.id)
        context['Anganwadi']=Anganwadi
        return context
    def post(self,request,*arg,**kwargs):
        Phone=request.POST['phone']
        email=request.POST['email']
        image= request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        user = User.objects.get(id=self.request.user.id)
        user.email=email
        user.save()
        Anganawadi= anganawadi.objects.get(user_id=self.request.user.id)
        Anganawadi.user=user
        Anganawadi.a_pic=file
        Anganawadi.a_contact = Phone
        Anganawadi.a_email =email
        Anganawadi.save()
        return redirect(request.META['HTTP_REFERER'])


class user_foodServices(TemplateView):
    template_name = 'anganwadi/user_foodServices.html'
    def get_context_data(self, **kwargs):
        context = super(user_foodServices,self).get_context_data(**kwargs)
        userfoodservice=tbl_userfoodservice.objects.filter(anganwadi_id__user_id=self.request.user.id,active_status='active')
        Foodtype=foodtype.objects.filter(status='active')
        context['Foodtype']=Foodtype
        context['userfoodservice']=userfoodservice
        return context
    def post(self,request,*args,**kwargs):
        food=request.POST['food']
        Month=request.POST['month']
        quantity=request.POST['Quantity']
        starting_date=request.POST['st_date']
        ending_date=request.POST['ed_date']
        userfoodservice=tbl_userfoodservice()
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        userfoodservice.anganwadi_id_id=Anganawadi.id
        userfoodservice.food_id_id=food
        userfoodservice.month=Month
        userfoodservice.food_qty=quantity
        userfoodservice.start_date=starting_date
        userfoodservice.end_date=ending_date
        userfoodservice.active_status='active'
        userfoodservice.save()
        USERs=tbl_user.objects.filter(location_id=Anganawadi.location_id)
        for i in USERs:
            print(i.user_email)
            email = EmailMessage(
            'Your food added',
            userfoodservice.month,
            settings.EMAIL_HOST_USER,
            [i.user_email],
             )
            email.fail_silently = False
            email.send()
        return redirect(request.META['HTTP_REFERER'])

class typeof_food(TemplateView):
   template_name = 'anganwadi/user_foodServices.html'
   def get_context_data(self, **kwargs):
        context = super(typeof_food,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        userselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        context['typefood']=userselectfoodtype
        userfood=tbl_userfood.objects.filter(status='active',foodtype_id_id=self.request.GET['food_id'])
        userfoodservice=tbl_userfoodservice.objects.filter(anganwadi_id__user_id=self.request.user.id,active_status='active')
        context['userfood']=userfood
        context['userfoodservice']=userfoodservice
        context['Foodtype']=Foodtype
        return context


class user_foodServices_remove(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_userfoodservice.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class ViewUserBooking_food(TemplateView):
    template_name = 'anganwadi/ViewUserBooking_food.html'
    def get_context_data(self, **kwargs):
        context = super(ViewUserBooking_food,self).get_context_data(**kwargs)
        foodid = self.request.GET['food_id']
        pfoodbooking =tbl_foodbooking.objects.filter(userfoodservice_id__anganwadi_id__user_id=self.request.user.id,foodbooking_status="Request accept",userfoodservice_id__food_id=foodid)
        print(pfoodbooking)
        context['pfoodbooking']=pfoodbooking
        return context

class user_FoodStockMasterDetails(TemplateView):
    template_name = 'anganwadi/user_FoodStockMasterDetails.html'
    def get_context_data(self, **kwargs):
        context = super(user_FoodStockMasterDetails,self).get_context_data(**kwargs)
        total_foodstock=tbl_totalfoodstock.objects.filter(user_id=self.request.user.id)
        id=self.request.user.id
        print(id)
        print("aaaaaasdfghjkl",total_foodstock)
        context['total_foodstock']=total_foodstock
        return context

class user_chartStockMasterDetails(TemplateView):
    template_name = 'anganwadi/user_ChartStockMasterDetails.html'
    def get_context_data(self, **kwargs):
        context = super(user_chartStockMasterDetails,self).get_context_data(**kwargs)
        id=self.request.GET['id']
        FoodType =tbl_userfood.objects.get(id=id)
        foodstock=tbl_foodstock.objects.filter(user_id=self.request.user.id,food_id=FoodType.id)
        context['foodstock']=foodstock
        return context



class user_AddFoodStock(TemplateView):
    template_name = 'anganwadi/user_addstock.html'
    def get_context_data(self, **kwargs):
        context = super(user_AddFoodStock,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        foodstock=tbl_foodstock.objects.filter()
        context['foodstock']=foodstock
        context['Foodtype']=Foodtype
        return context

    def post(self,request,*args,**kwargs):

        Food = request.POST['food']
        stock =request.POST['Stock']
        Stock_date =request.POST['stock_date']
        FoodType =tbl_userfood.objects.get(id=Food)
        total=0
        try:
          if tbl_totalfoodstock.objects.get(user_id=self.request.user.id,food_id=FoodType.id):
             ANGENWADI=User.objects.get(id=self.request.user.id)
             FoodType =tbl_userfood.objects.get(id=Food)
             foodstock = tbl_foodstock()
             foodstock.user_id=ANGENWADI.id
             foodstock.food_id_id=FoodType.id
             foodstock.food_stock=stock
             foodstock.foodstock_date=Stock_date
             foodstock.save()
             total_foddstock=tbl_totalfoodstock.objects.get(user_id=self.request.user.id,food_id=FoodType.id)
             print(total_foddstock)
             stock=tbl_foodstock.objects.filter(user_id=self.request.user.id,food_id=FoodType.id)
             FoodType =tbl_userfood.objects.get(id=Food)
             for i in stock:
                 total=int(total)+int(i.food_stock)
             total_foddstock.food_totalStock=total
             total_foddstock.user_id=self.request.user.id
             total_foddstock.save()
             print(total)
             print("aaaaaaaaaaa",stock)
             print("111111111111111111111111")
             return redirect(request.META['HTTP_REFERER'])
          else:
            ANGENWADI=User.objects.get(id=self.request.user.id)
            FoodType =tbl_userfood.objects.get(id=Food)
            foodstock = tbl_foodstock()
            foodstock.user_id=ANGENWADI.id
            foodstock.food_id_id=FoodType.id
            foodstock.food_stock=stock
            foodstock.foodstock_date=Stock_date
            foodstock.save()
            total_userstock=tbl_totalfoodstock()
            total_userstock.user_id=self.request.user.id
            FoodType =tbl_userfood.objects.get(id=Food)
            total_userstock.food_id_id=FoodType.id
            total_userstock.food_totalStock=stock
            total_userstock.save()

            print("2222222222222222222222222222222222222")
            return redirect(request.META['HTTP_REFERER'])

        except:
            ANGENWADI=User.objects.get(id=self.request.user.id)
            FoodType =tbl_userfood.objects.get(id=Food)
            foodstock = tbl_foodstock()
            foodstock.user_id=ANGENWADI.id
            foodstock.food_id_id=FoodType.id
            foodstock.food_stock=stock
            foodstock.foodstock_date=Stock_date
            foodstock.save()
            total_userstock=tbl_totalfoodstock()
            total_userstock.user_id=self.request.user.id
            FoodType =tbl_userfood.objects.get(id=Food)
            total_userstock.food_id_id=FoodType.id
            total_userstock.food_totalStock=stock
            total_userstock.save()
            foodstock.save()
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(request.META['HTTP_REFERER'])




        # return redirect(request.META['HTTP_REFERER'])

class typeof_food_stock(TemplateView):
   template_name = 'anganwadi/user_addstock.html'
   def get_context_data(self, **kwargs):
        context = super(typeof_food_stock,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        userselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        userfood=tbl_userfood.objects.filter(status='active',foodtype_id_id=self.request.GET['food_id'])
        foodstock=tbl_foodstock.objects.filter()
        context['foodstock']=foodstock
        context['userfood']=userfood
        context['Foodtype']=Foodtype
        context['typefood']=userselectfoodtype
        return context

class remove_user_foodstock(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_foodstock.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class anganwadi_send_foodrquest(TemplateView):
    template_name = 'anganwadi/user_SendRequest.html'
    def get_context_data(self, **kwargs):
        context = super(anganwadi_send_foodrquest,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        Anganawadis =  anganawadi.objects.get(user_id=self.request.user.id)
        user_request=tbl_foodstockrequest.objects.filter(user_id=Anganawadis.id)
        context['user_request']=user_request
        context['Foodtype']=Foodtype
        return context
    def post(self,request,*args,**kwargs):
        foodid=request.POST['food']
        quantity=request.POST['Quantity']
        user_request=tbl_foodstockrequest()
        Anganawadis =  anganawadi.objects.get(user_id=self.request.user.id)
        user_request.user_id=Anganawadis.id
        FoodType =tbl_userfood.objects.get(id=foodid)
        user_request.food_id_id=FoodType.id
        user_request.quantity=quantity
        user_request.f_status="pending"
        user_request.save()
        return redirect(request.META['HTTP_REFERER'])



class type_food_userrequest(TemplateView):
    template_name = 'anganwadi/user_SendRequest.html'
    def get_context_data(self, **kwargs):
        context = super(type_food_userrequest,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        userselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        userfood=tbl_userfood.objects.filter(status='active',foodtype_id_id=self.request.GET['food_id'])
        Anganawadis =  anganawadi.objects.get(user_id=self.request.user.id)
        user_request=tbl_foodstockrequest.objects.filter(user_id=Anganawadis.id)
        context['user_request']=user_request
        context['userfood']=userfood
        context['Foodtype']=Foodtype
        context['typefood']=userselectfoodtype
        return context

class Remove_type_food_userrequest(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_foodstockrequest.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class user_acceptedfoodbooking(TemplateView):
    template_name = 'anganwadi/user_acceptedBookings.html'
    def post(self,request,*arg,**kwargs):
        starting = request.POST['starting_date']
        print(starting)
        enddate = request.POST['ending_date']
        print(enddate)
        id=self.request.user.id
        print(id)
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)

        data = tbl_foodbooking.objects.filter(Anganwadi=Anganwadi.id,foodbooking_status="anganwadi request accepted",foodbooking_date__range=[starting, enddate])
        print("33333333333",data)
        return render(request,'anganwadi/user_acceptedBookings.html',{'result':data})



class view_userfood_report(TemplateView):
    template_name = 'anganwadi/userfood_report.html'
    def post(self,request,*arg,**kwargs):
        starting = request.POST['starting_date']
        print(starting)
        enddate = request.POST['ending_date']
        print(enddate)
        id=self.request.user.id
        print(id)
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        data = tbl_foodbooking.objects.filter(Anganwadi=Anganwadi.id,foodbooking_status="Completed Request",foodbooking_date__range=[starting, enddate])
        print("33333333333",data)
        return render(request, 'anganwadi/userfood_report.html',{'result':data})

class pregnantfoodServices(TemplateView):
     template_name =  'anganwadi/PwomenFoodServices.html'
     def get_context_data(self, **kwargs):
        context = super(pregnantfoodServices,self).get_context_data(**kwargs)
        pfoodservice=tbl_pwomenfoodservice.objects.filter(anganwadi_id__user_id=self.request.user.id,active_status='active')
        Foodtype=foodtype.objects.filter(status='active')
        context['Foodtype']=Foodtype
        context['pfoodservice']=pfoodservice
        return context
     def post(self,request,*args,**kwargs):
        food=request.POST['food']
        Month=request.POST['month']
        quantity=request.POST['Quantity']
        starting_date=request.POST['st_date']
        ending_date=request.POST['ed_date']
        pfoodservice=tbl_pwomenfoodservice()
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        pfoodservice.anganwadi_id_id=Anganawadi.id
        pfoodservice.food_id_id=food
        pfoodservice.month=Month
        pfoodservice.food_qty=quantity
        pfoodservice.start_date=starting_date
        pfoodservice.end_date=ending_date
        pfoodservice.active_status='active'
        USERs=tbl_pwomens.objects.filter(location_id=Anganawadi.location_id)
        pfoodservice.save()
        for i in USERs:
            print(i.pwomen_email)
            email = EmailMessage(
            'Your food added',
            pfoodservice.month,
            settings.EMAIL_HOST_USER,
            [i.pwomen_email],
             )
            email.fail_silently = False
            email.send()

        return redirect(request.META['HTTP_REFERER'])

class type_food_preganant(TemplateView):
    template_name = 'anganwadi/PwomenFoodServices.html'
    def get_context_data(self, **kwargs):
        context = super(type_food_preganant,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        pselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        pregnantfood=tbl_pwomenfood.objects.filter(foodtype_id_id=self.request.GET['food_id'])
        print("qqqqqqqqqqqqqqqq",pregnantfood)
        context['pregnantfood']=pregnantfood
        pfoodservice=tbl_pwomenfoodservice.objects.filter(anganwadi_id__user_id=self.request.user.id,active_status='active')
        context['pfoodservice']=pfoodservice
        context['Foodtype']=Foodtype
        context['typefood']=pselectfoodtype
        return context


class pregnant_foodServices_remove(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_pwomenfoodservice.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class ViewPregnantBooking_food(TemplateView):
    template_name = 'anganwadi/ViewPregnantBooking_food.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPregnantBooking_food,self).get_context_data(**kwargs)
        foodid = self.request.GET['food_id']
        pfoodbooking =tbl_pfoodbooking.objects.filter(pwomenfoodservice_id__anganwadi_id__user_id=self.request.user.id,pfoodbooking_status="Request accept",pwomenfoodservice_id__food_id=foodid).order_by('-pfoodbooking_date')
        context['pfoodbooking']=pfoodbooking
        return context


class pregnant_FoodStockMasterDetails(TemplateView):
    template_name = 'anganwadi/pregnant_FoodStockMasterDetails.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_FoodStockMasterDetails,self).get_context_data(**kwargs)
        total_pfoodstock=tbl_totalpfoodstock.objects.filter(user_id=self.request.user.id)
        context['total_foodstock']=total_pfoodstock
        return context

class pregnant_chartStockMasterDetails(TemplateView):
    template_name = 'anganwadi/pregnant_chartStockMasterDetails.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_chartStockMasterDetails,self).get_context_data(**kwargs)
        id=self.request.GET['id']
        FoodType =tbl_pwomenfood.objects.get(id=id)
        pfoodstock=tbl_pfoodstock.objects.filter(user_id=self.request.user.id,pfood_id=FoodType.id)
        context['foodstock']=pfoodstock
        return context

class Pregnant_AddFoodStock(TemplateView):
    template_name = 'anganwadi/Pregnant_AddFoodStock.html'
    def get_context_data(self, **kwargs):
        context = super(Pregnant_AddFoodStock,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        Pfoodstock=tbl_pfoodstock.objects.filter()
        context['foodstock']=Pfoodstock
        context['Foodtype']=Foodtype
        return context
    def post(self,request,*args,**kwargs):

        Food = request.POST['food']
        stock =request.POST['Stock']
        Stock_date =request.POST['stock_date']
        FoodType =tbl_pwomenfood.objects.get(id=Food)
        print("bbbbbbbbbbbbbbbbbbbb",FoodType.id)
        total=0
        try:
          if tbl_totalpfoodstock.objects.get(user_id=self.request.user.id,pfood_id=FoodType.id):
             ANGENWADI=User.objects.get(id=self.request.user.id)
             FoodType =tbl_pwomenfood.objects.get(id=Food)
             foodstock = tbl_pfoodstock()
             foodstock.user_id=ANGENWADI.id
             foodstock.pfood_id_id=FoodType.id
             foodstock.pfood_stock=stock
             foodstock.pfoodstock_date=Stock_date
             foodstock.save()
             total_pfoodstock=tbl_totalpfoodstock.objects.get(user_id=self.request.user.id,pfood_id=FoodType.id)
             print(total_pfoodstock)
             stock=tbl_pfoodstock.objects.filter(user_id=self.request.user.id,pfood_id=FoodType.id)
             FoodType =tbl_pwomenfood.objects.get(id=Food)
             for i in stock:
                 total=int(total)+int(i.pfood_stock)
             total_pfoodstock.pfood_totalStock=total
             total_pfoodstock.user_id=self.request.user.id
             total_pfoodstock.save()
             print(total)
             print("aaaaaaaaaaa",total)
             print("111111111111111111111111")
             return redirect(request.META['HTTP_REFERER'])
          else:
            ANGENWADI=User.objects.get(id=self.request.user.id)
            # FoodType =tbl_pwomenfood.objects.get(id=Food)
            foodstock = tbl_pfoodstock()
            foodstock.user_id=ANGENWADI.id
            foodstock.pfood_id_id=FoodType.id
            foodstock.pfood_stock=stock
            foodstock.pfoodstock_date=Stock_date
            foodstock.save()
            total_pstock=tbl_totalpfoodstock()
            total_pstock.user_id=self.request.user.id
            FoodType =tbl_pwomenfood.objects.get(id=Food)
            total_pstock.pfood_id_id=FoodType.id
            total_pstock.pfood_totalStock=stock
            total_pstock.save()

            print("2222222222222222222222222222222222222")
            return redirect(request.META['HTTP_REFERER'])

        except:
            ANGENWADI=User.objects.get(id=self.request.user.id)
            FoodType =tbl_pwomenfood.objects.get(id=Food)
            foodstock = tbl_pfoodstock()
            foodstock.user_id=ANGENWADI.id
            foodstock.pfood_id_id=FoodType.id
            foodstock.pfood_stock=stock
            foodstock.pfoodstock_date=Stock_date
            foodstock.save()
            total_pstock=tbl_totalpfoodstock()
            total_pstock.user_id=self.request.user.id
            FoodType =tbl_pwomenfood.objects.get(id=Food)
            total_pstock.pfood_id_id=FoodType.id
            total_pstock.pfood_totalStock=stock
            total_pstock.save()
            # foodstock.save()
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(request.META['HTTP_REFERER'])

class typeof_pregnant_food_stock(TemplateView):
   template_name = 'anganwadi/Pregnant_AddFoodStock.html'
   def get_context_data(self, **kwargs):
        context = super(typeof_pregnant_food_stock,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        pselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        pfood=tbl_pwomenfood.objects.filter(foodtype_id_id=self.request.GET['food_id'])
        foodstock=tbl_pfoodstock.objects.filter()
        context['foodstock']=foodstock
        context['userfood']=pfood
        context['Foodtype']=Foodtype
        context['typefood']=pselectfoodtype
        return context


class remove_pregnant_foodstock(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_pfoodstock.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class anganwadi_pregnant_send_foodrquest(TemplateView):
    template_name = 'anganwadi/anganwadi_pregnant_send_foodrquest.html'
    def get_context_data(self, **kwargs):
        context = super(anganwadi_pregnant_send_foodrquest,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        p_request=tbl_pfoodstockrequest.objects.filter(user_id=Anganwadi.id)
        context['user_request']=p_request
        context['Foodtype']=Foodtype
        return context
    def post(self,request,*args,**kwargs):
        foodid=request.POST['food']
        quantity=request.POST['Quantity']
        user_request=tbl_pfoodstockrequest()
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        FoodType =tbl_pwomenfood.objects.get(id=foodid)
        user_request.food_id_id=FoodType.id
        user_request.pquantity=quantity
        user_request.f_status="pending"
        user_request.user_id= Anganwadi.id
        user_request.save()
        return redirect(request.META['HTTP_REFERER'])


class food_type_preganant_request(TemplateView):
    template_name = 'anganwadi/anganwadi_pregnant_send_foodrquest.html'
    def get_context_data(self, **kwargs):
        context = super(food_type_preganant_request,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        pselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        pregnantfood=tbl_pwomenfood.objects.filter(foodtype_id_id=self.request.GET['food_id'])
        print("qqqqqqqqqqqqqqqq",pregnantfood)
        context['pregnantfood']=pregnantfood
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        p_request=tbl_pfoodstockrequest.objects.filter(user_id=Anganwadi.id)
        context['user_request']=p_request
        context['Foodtype']=Foodtype
        context['typefood']=pselectfoodtype
        return context

class Remove_pregnantfood_userrequest(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_pfoodstockrequest.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class pregnant_acceptedfoodbooking(TemplateView):
    template_name = 'anganwadi/pregnant_acceptedfoodbooking.html'
    def post(self,request,*arg,**kwargs):
        starting = request.POST['starting_date']
        print(starting)
        enddate = request.POST['ending_date']
        print(enddate)
        id=self.request.user.id
        print(id)
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        print(Anganwadi.id)
        data = tbl_pfoodbooking.objects.filter(pfoodbooking_date__range=[starting, enddate])
        print("33333333333333333333333333333333",data)
        return render(request,'anganwadi/pregnant_acceptedfoodbooking.html',{'result':data})

class view_pregnantfood_report(TemplateView):
    template_name = 'anganwadi/view_pregnantfood_report.html'
    def post(self,request,*arg,**kwargs):
        starting = request.POST['starting_date']
        print(starting)
        enddate = request.POST['ending_date']
        print(enddate)
        id=self.request.user.id
        print(id)
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        data = tbl_pfoodbooking.objects.filter(Anganwadi=Anganwadi.id,pfoodbooking_status="Completed Request",pfoodbooking_date__range=[starting, enddate])
        return render(request,'anganwadi/view_pregnantfood_report.html',{'result':data})


class add_child(TemplateView):
    template_name = 'anganwadi/add_child.html'
    def get_context_data(self, **kwargs):
        context = super(add_child,self).get_context_data(**kwargs)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        return context
    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        father=request.POST['Father']
        print(father)
        mother=request.POST['Mother']
        print(mother)
        age=request.POST['Age']
        print(age)
        Phone=request.POST['phone']
        print(Phone)
        gender=request.POST['gender']
        print(gender)
        L_id=request.POST['location']
        print(L_id)
        PROOF= request.FILES['proofdoc']
        f = FileSystemStorage()
        prooffile = f.save(PROOF.name, PROOF)
        image= request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        House=request.POST['House']
        print(House)
        street=request.POST['street']
        print(street)
        pincode=request.POST['pincode']
        print(pincode)

        try:
            user = User.objects.create_user(first_name = name,password=name,username=name,last_name=1)
            print("22222222222",user)
            CHILD=child()
            CHILD.child_id_id=user.id
            CHILD.child_name=name
            CHILD.save()
            user.save()

            PLACE=Location.objects.get(status='active',id=L_id)
            print(PLACE)
            Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
            table_child=tbl_child()
            table_child.child_name = name
            table_child.child_age = age
            table_child.child_fathername = father
            table_child.child_mothername = mother
            table_child.child_contact = Phone
            table_child.child_gender = gender
            table_child.location_id_id = L_id
            table_child.place_id_id=PLACE.place.id
            table_child.a_id_id = Anganawadi.id
            table_child.child_status=1
            table_child.child_hname=House
            table_child.child_street= street
            table_child.child_pin=pincode
            table_child.birthcertificate=prooffile
            table_child.child_image=file
            table_child.child_id_id=user.id
            table_child.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = 'child'
            usertype.save()

            return render(request,'anganwadi/anganwadi_index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'anganwadi/anganwadi_index.html',{'messages':messages})


class child_district(TemplateView):
    template_name = 'anganwadi/add_child.html'
    def get_context_data(self, **kwargs):
        context = super(child_district,self).get_context_data(**kwargs)
        id = self.request.GET['dist_id']
        place=Place.objects.filter(status='active',District_id=id)
        DISTRICT=District.objects.filter(status='active')
        selectdistrict=District.objects.get(status='active',id=id)
        context['district']=DISTRICT
        context['selectdistrict']=selectdistrict.District_name
        context['place']=place
        return context

class selected_child_place(TemplateView):
    template_name = 'anganwadi/add_child.html'
    def get_context_data(self, **kwargs):
        context = super(selected_child_place,self).get_context_data(**kwargs)
        id = self.request.GET['place_id']
        place=Place.objects.filter(status='active',District_id=id)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        selectplace=Place.objects.get(status='active',id=id)
        context['selectplace']=selectplace.place
        context['selectdistrict']=selectplace.District.District_name
        locations=Location.objects.filter(status='active',place_id=id)
        context['locations']=locations
        context['place']=place
        return context


class AcceptedListChild(TemplateView):
    template_name = 'anganwadi/AcceptedListChild.html'
    def get_context_data(self, **kwargs):
        context = super(AcceptedListChild,self).get_context_data(**kwargs)
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        table_child=tbl_child.objects.filter(a_id_id=Anganawadi.id,child_status=1)
        print(table_child)
        context['CHILD']=table_child
        return context

class child_remove(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tablechild=tbl_child.objects.get(child_id_id=id)
        tablechild.child_status=0
        tablechild.save()
        return redirect(request.META['HTTP_REFERER'])
class child_accept(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tablechild=tbl_child.objects.get(child_id_id=id)
        tablechild.child_status=1
        tablechild.save()
        return redirect(request.META['HTTP_REFERER'])

class RejectedListChild(TemplateView):
    template_name = 'anganwadi/RejectedListChild.html'
    def get_context_data(self, **kwargs):
        context = super(RejectedListChild,self).get_context_data(**kwargs)
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        table_child=tbl_child.objects.filter(a_id_id=Anganawadi.id,child_status=0)
        print(table_child)
        context['CHILD']=table_child
        return context

class healthtips(TemplateView):
    template_name = 'anganwadi/Healthtips.html'
    def post(self,request,*args,**kwargs):
        Title = request.POST['title']
        Descrip =request.POST['Description']
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        table_healthtips=tbl_healthtips()
        table_healthtips.tips_title=Title
        table_healthtips.tips_description=Descrip
        table_healthtips.a_id_id=Anganawadi.id
        table_healthtips.save()
        return redirect(request.META['HTTP_REFERER'])
    def get_context_data(self, **kwargs):
        context = super(healthtips,self).get_context_data(**kwargs)
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        table_healthtips=tbl_healthtips.objects.filter(a_id_id=Anganawadi.id)
        context['healthtips']=table_healthtips
        return context

class remove_healthtip(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_healthtips.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class ActiveUserList(TemplateView):
    template_name = 'anganwadi/ActiveUserList.html'
    def get_context_data(self, **kwargs):
        context = super(ActiveUserList,self).get_context_data(**kwargs)
        id = self.request.user.id
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        USER= tbl_user.objects.filter(user__last_name=0,location_id_id=Anganawadi.location_id,user_status=1)
        print(USER)
        context['USER']=USER
        return context

class AcceptedListUser(TemplateView):
    template_name = 'anganwadi/AcceptedListUser.html'
    def get_context_data(self, **kwargs):
        context = super(AcceptedListUser,self).get_context_data(**kwargs)
        id = self.request.user.id
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        USER= tbl_user.objects.filter(user__last_name=1,location_id_id=Anganawadi.location_id,user_status='accepted')
        print(USER)
        context['USER']=USER
        return context

class RejectedListUse(TemplateView):
    template_name = 'anganwadi/RejectedListUse.html'
    def get_context_data(self, **kwargs):
        context = super(RejectedListUse,self).get_context_data(**kwargs)
        id = self.request.user.id
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        USER= tbl_user.objects.filter(user__last_name=0,location_id_id=Anganawadi.location_id,user_status='Reject')
        print(USER)
        context['USER']=USER
        return context

class ViewPwomenlist(TemplateView):
    template_name = 'anganwadi/ViewPwomenlist.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPwomenlist,self).get_context_data(**kwargs)
        id = self.request.user.id
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        pregnant= tbl_pwomens.objects.filter(user__last_name=0,location_id_id=Anganawadi.location_id,pwomen_isactive=1)
        context['pregnant']=pregnant
        return context

class ActiveListPwomen(TemplateView):
    template_name = 'anganwadi/ActiveListPwomen.html'
    def get_context_data(self, **kwargs):
        context = super(ActiveListPwomen,self).get_context_data(**kwargs)
        id = self.request.user.id
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        pregnant= tbl_pwomens.objects.filter(user__last_name=1,location_id_id=Anganawadi.location_id,pwomen_isactive='accepted')
        print(pregnant)
        context['pregnant']=pregnant
        return context

class RejectedListPwomen(TemplateView):
    template_name = 'anganwadi/RejectedListPwomen.html'
    def get_context_data(self, **kwargs):
        context = super(RejectedListPwomen,self).get_context_data(**kwargs)
        id = self.request.user.id
        Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        print("2222222222222222222222",Anganawadi)
        pregnant = tbl_pwomens.objects.filter(user__last_name=0, location_id_id=Anganawadi.location_id,
                                              pwomen_isactive='Reject')
        print("33333333333333333333333333333",pregnant)
        context['pregnant']=pregnant
        return context

class approve_users(View):
     def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(id=id)
        uSRE= tbl_user.objects.get(user_id=user.id)
        uSRE.user_status="accepted"
        uSRE.save()
        user.last_name='1'
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class reject_users(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(id=id)
        uSRE= tbl_user.objects.get(user_id=user.id)
        uSRE.user_status="Reject"
        uSRE.save()
        user.last_name='0'
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class approve_pregnant(View):
     def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(id=id)
        uSRE= tbl_pwomens.objects.get(user_id=user.id)
        uSRE.pwomen_isactive="accepted"
        uSRE.save()
        user.last_name='1'
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class reject_pregnant(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(id=id)
        uSRE= tbl_pwomens.objects.get(user_id=user.id)
        uSRE.pwomen_isactive="Reject"
        uSRE.save()
        user.last_name='0'
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class approve_users_foodrequest(View):
     def dispatch(self, request, *args, **kwargs):
         id = request.GET['id']
         ang =anganawadi.objects.get(user_id=self.request.user.id)

         food_id = request.GET['foodid']
         qnty = request.GET['quantity']
         tblfoodbooking =tbl_foodbooking.objects.get(id=id)
         tbltotalfoodstock=tbl_totalfoodstock.objects.get(food_id=food_id,user_id=self.request.user.id)
         tbltotalfoodstock.food_totalStock=int(tbltotalfoodstock.food_totalStock)- int(qnty)
         print(tbltotalfoodstock.food_totalStock)
         tbltotalfoodstock.food_totalStock =tbltotalfoodstock.food_totalStock
         tblfoodbooking.foodbooking_status="anganwadi request accepted"
         tblfoodbooking.Anganwadi_id = ang.id
         tblfoodbooking.save()
         return redirect(request.META['HTTP_REFERER'])

class approve_pregnant_foodrequest(TemplateView):
     def dispatch(self, request, *args, **kwargs):
         id = request.GET['id']
         ang = anganawadi.objects.get(user_id=self.request.user.id)
         food_id = request.GET['foodid']
         qnty = request.GET['quantity']
         tblpfoodbooking =tbl_pfoodbooking.objects.get(id=id)
         tbltotalpfoodstock=tbl_totalpfoodstock.objects.get(pfood_id=food_id,user_id=self.request.user.id)
         tbltotalpfoodstock.pfood_totalStock=int(tbltotalpfoodstock.pfood_totalStock)- int(qnty)
         tbltotalpfoodstock.pfood_totalStock =tbltotalpfoodstock.pfood_totalStock
         tblpfoodbooking.pfoodbooking_status="anganwadi request accepted"
         tblpfoodbooking.Anganwadi_id = ang.id
         tblpfoodbooking.save()
         tbltotalpfoodstock.save()
         return redirect(request.META['HTTP_REFERER'])

class user_provide_food(TemplateView):
    template_name = 'anganwadi/user_acceptedBookings.html'
    def get_context_data(self, **kwargs):
        context = super(user_provide_food,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        userbooking=tbl_foodbooking.objects.get(id=id)
        userbooking.foodbooking_status="Completed Request"
        userbooking.save()
        context['messages']="Completed requests"
        return context

class pregnant_complete_foodrequest(TemplateView):
    template_name = 'anganwadi/pregnant_acceptedfoodbooking.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_complete_foodrequest,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        pregnantbooking=tbl_pfoodbooking.objects.get(id=id)
        pregnantbooking.pfoodbooking_status="Completed Request"
        pregnantbooking.save()
        context['messages']="Completed requests"
        return context


class child_FoodStockMasterDetails(TemplateView):
    template_name = 'anganwadi/child_FoodStockMasterDetails.html'
    def get_context_data(self, **kwargs):
        context = super(child_FoodStockMasterDetails,self).get_context_data(**kwargs)
        total_foodstock=tbl_totalchildfoodstock.objects.filter(user_id=self.request.user.id)
        id=self.request.user.id
        context['total_foodstock']=total_foodstock
        return context



class child_chartStockMasterDetails(TemplateView):
    template_name = 'anganwadi/child_chartStockMasterDetails.html'
    def get_context_data(self, **kwargs):
        context = super(child_chartStockMasterDetails,self).get_context_data(**kwargs)
        id=self.request.GET['id']
        FoodType =tbl_userfood.objects.get(id=id)
        foodstock=tbl_childfoodstock.objects.filter(user_id=self.request.user.id,food_id=FoodType.id)
        context['foodstock']=foodstock
        return context


class child_AddFoodStock(TemplateView):
    template_name = 'anganwadi/child_AddFoodStock.html'
    def get_context_data(self, **kwargs):
        context = super(child_AddFoodStock,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        foodstock=tbl_childfoodstock.objects.filter()
        context['foodstock']=foodstock
        context['Foodtype']=Foodtype
        return context

    def post(self,request,*args,**kwargs):

        Food = request.POST['food']
        stock =request.POST['Stock']
        Stock_date =request.POST['stock_date']
        FoodType =tbl_userfood.objects.get(id=Food)
        total=0
        try:
          if tbl_totalchildfoodstock.objects.get(user_id=self.request.user.id,food_id=FoodType.id):
             ANGENWADI=User.objects.get(id=self.request.user.id)
             FoodType =tbl_userfood.objects.get(id=Food)
             foodstock = tbl_childfoodstock()
             foodstock.user_id=ANGENWADI.id
             foodstock.food_id_id=FoodType.id
             foodstock.food_stock=stock
             foodstock.foodstock_date=Stock_date
             foodstock.save()
             total_foddstock=tbl_totalchildfoodstock.objects.get(user_id=self.request.user.id,food_id=FoodType.id)
             print(total_foddstock)
             stock=tbl_childfoodstock.objects.filter(user_id=self.request.user.id,food_id=FoodType.id)
             FoodType =tbl_userfood.objects.get(id=Food)
             for i in stock:
                 total=int(total)+int(i.food_stock)
             total_foddstock.food_totalStock=total
             total_foddstock.user_id=self.request.user.id
             total_foddstock.save()
             print(total)
             print("aaaaaaaaaaa",stock)
             print("111111111111111111111111")
             return redirect(request.META['HTTP_REFERER'])
          else:
            ANGENWADI=User.objects.get(id=self.request.user.id)
            FoodType =tbl_userfood.objects.get(id=Food)
            foodstock = tbl_childfoodstock()
            foodstock.user_id=ANGENWADI.id
            foodstock.food_id_id=FoodType.id
            foodstock.food_stock=stock
            foodstock.foodstock_date=Stock_date
            foodstock.save()
            total_userstock=tbl_totalchildfoodstock()
            total_userstock.user_id=self.request.user.id
            FoodType =tbl_userfood.objects.get(id=Food)
            total_userstock.food_id_id=FoodType.id
            total_userstock.food_totalStock=stock
            total_userstock.save()

            print("2222222222222222222222222222222222222")
            return redirect(request.META['HTTP_REFERER'])

        except:
            ANGENWADI=User.objects.get(id=self.request.user.id)
            FoodType =tbl_userfood.objects.get(id=Food)
            foodstock = tbl_childfoodstock()
            foodstock.user_id=ANGENWADI.id
            foodstock.food_id_id=FoodType.id
            foodstock.food_stock=stock
            foodstock.foodstock_date=Stock_date
            foodstock.save()
            total_userstock=tbl_totalchildfoodstock()
            total_userstock.user_id=self.request.user.id
            FoodType =tbl_userfood.objects.get(id=Food)
            total_userstock.food_id_id=FoodType.id
            total_userstock.food_totalStock=stock
            total_userstock.save()
            foodstock.save()
            print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            return redirect(request.META['HTTP_REFERER'])

class typeof_child_food_stock(TemplateView):
   template_name = 'anganwadi/child_AddFoodStock.html'
   def get_context_data(self, **kwargs):
        context = super(typeof_child_food_stock,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        userselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        userfood=tbl_userfood.objects.filter(status='active',foodtype_id_id=self.request.GET['food_id'])
        foodstock=tbl_childfoodstock.objects.filter()
        context['foodstock']=foodstock
        context['userfood']=userfood
        context['Foodtype']=Foodtype
        context['typefood']=userselectfoodtype
        return context

class child_SendRequest(TemplateView):
    template_name = 'anganwadi/child_SendRequest.html'
    def get_context_data(self, **kwargs):
        context = super(child_SendRequest,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        Anganawadis =  anganawadi.objects.get(user_id=self.request.user.id)
        user_request=tbl_childfoodstockrequest.objects.filter(user_id=Anganawadis.id)
        context['user_request']=user_request
        context['Foodtype']=Foodtype
        return context
    def post(self,request,*args,**kwargs):
        foodid=request.POST['food']
        quantity=request.POST['Quantity']
        child_request=tbl_childfoodstockrequest()
        Anganawadis =  anganawadi.objects.get(user_id=self.request.user.id)
        child_request.user_id=Anganawadis.id
        FoodType =tbl_userfood.objects.get(id=foodid)
        child_request.food_id_id=FoodType.id
        child_request.quantity=quantity
        child_request.f_status="pending"
        child_request.save()
        return redirect(request.META['HTTP_REFERER'])

class type_food_childrrequest(TemplateView):
    template_name = 'anganwadi/child_SendRequest.html'
    def get_context_data(self, **kwargs):
        context = super(type_food_childrrequest,self).get_context_data(**kwargs)
        Foodtype=foodtype.objects.filter(status='active')
        userselectfoodtype=foodtype.objects.get(id=self.request.GET['food_id'])
        userfood=tbl_userfood.objects.filter(status='active',foodtype_id_id=self.request.GET['food_id'])
        Anganawadis =  anganawadi.objects.get(user_id=self.request.user.id)
        user_request=tbl_childfoodstockrequest.objects.filter(user_id=Anganawadis.id)
        context['user_request']=user_request
        context['userfood']=userfood
        context['Foodtype']=Foodtype
        context['typefood']=userselectfoodtype
        return context

class child_foodreport(TemplateView):
    template_name = 'anganwadi/child_foodreport.html'
    def post(self,request,*arg,**kwargs):
        starting = request.POST['starting_date']
        print(starting)
        enddate = request.POST['ending_date']
        print(enddate)
        id=self.request.user.id
        print(id)
        Anganwadi = anganawadi.objects.get(user_id=self.request.user.id)
        data = tbl_foodbooking.objects.filter(Anganwadi=Anganwadi.id,foodbooking_status="Completed Request",foodbooking_date__range=[starting, enddate])
        print("33333333333",data)
        return render(request, 'anganwadi/userfood_report.html',{'result':data})



class remove_child_foodstock(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_childfoodstock.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class Remove_type_food_childrrequest(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_childfoodstockrequest.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])