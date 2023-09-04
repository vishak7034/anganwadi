from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, View
from django.contrib.auth.models import auth, User
from anganwadi_app.models import Districtofficer, Place, District, prooftype, Location, anganawadi, UserType, foodtype, \
    tbl_userfood, tbl_pwomenfood, tbl_foodstockrequest, tbl_pfoodstockrequest, tbl_childfoodstockrequest
from django.shortcuts import redirect, render

class Index(TemplateView):
    template_name = 'districtofficer/index.html'

class view_profile(TemplateView):
    template_name = 'districtofficer/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(view_profile,self).get_context_data(**kwargs)
        dist=Districtofficer.objects.get(user_id=self.request.user.id)
        context['districtofficer']=dist
        return context

class edit_profile(TemplateView):
    template_name = 'districtofficer/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        dist=Districtofficer.objects.get(user_id=self.request.user.id)
        context['districtofficer']=dist
        return context
    def post(self,request,*arg,**kwargs):
        Phone=request.POST['phone']
        email=request.POST['email']
        Housename=request.POST['housename']
        street=request.POST['street']
        image= request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        pincode=request.POST['pincode']

        user = User.objects.get(id=self.request.user.id)
        user.email=email
        user.save()
        DIST= Districtofficer.objects.get(user_id=self.request.user.id)
        DIST.user=user
        DIST.Image=file
        DIST.phone = Phone
        DIST.emil =email
        DIST.housename = Housename
        DIST.street = street
        DIST.pincode = pincode
        DIST.save()
        return redirect(request.META['HTTP_REFERER'])

class accepted_anganawadi(TemplateView):
    template_name = 'districtofficer/view_anganawadiacceptedlist.html'
    def get_context_data(self, **kwargs):
        context = super(accepted_anganawadi,self).get_context_data(**kwargs)
        Anganawadi=anganawadi.objects.filter(a_status='active')
        context['Anganawadi']=Anganawadi
        return context


class reject_anganawadi(TemplateView):
    template_name = 'districtofficer/view_anganawadirejectlist.html'
    def get_context_data(self, **kwargs):
        context = super(reject_anganawadi,self).get_context_data(**kwargs)
        Anganawadi=anganawadi.objects.filter(a_status='reject')
        context['Anganawadi']=Anganawadi
        return context

class add_anganawadi(TemplateView):
    template_name = 'districtofficer/add_anganawadi.html'
    def get_context_data(self, **kwargs):
        context = super(add_anganawadi,self).get_context_data(**kwargs)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        proof=prooftype.objects.filter(status='active')
        context['proof']=proof
        return context
    def post(self,request,*arg,**kwargs):

        name=request.POST['name']
        Phone=request.POST['phone']
        email=request.POST['email']
        L_id=request.POST['location']
        print('cdddddddddd',Location)
        PROOF= request.FILES['proofdoc']
        f = FileSystemStorage()
        prooffile = f.save(PROOF.name, PROOF)
        image= request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        password=request.POST['password']
        confirmpsw=request.POST['ConfirmPassword']
        username=request.POST['username']
        lisence=request.POST['Lisence']

        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=1)
            user.save()
            PLACE=Location.objects.get(status='active',id=L_id)
            district=Districtofficer.objects.get(user_id=self.request.user.id)
            Anganawadi=anganawadi()
            Anganawadi.user_id=user.id
            Anganawadi.a_name=name
            Anganawadi.dofficer_id_id=district.id
            Anganawadi.a_contact=Phone
            Anganawadi.a_email=email
            Anganawadi.location_id_id=L_id
            Anganawadi.a_proof=prooffile
            Anganawadi.a_pic=file
            Anganawadi.a_password=password
            Anganawadi.a_confirmpsw=confirmpsw
            Anganawadi.a_username=username
            Anganawadi.a_status='active'
            Anganawadi.a_licenseno=lisence
            Anganawadi.place_id_id=PLACE.place.id
            usertype = UserType()
            usertype.user = user
            usertype.type = 'anganwadi'
            usertype.save()
            Anganawadi.save()
            return render(request,'districtofficer/index.html',{'messages':'successfully registered'})
        except:
             messages = "Enter Another Username, user already exist"
             return render(request,'districtofficer/index.html',{'messages':messages})

class anganawadi_district(TemplateView):
    template_name = 'districtofficer/add_anganawadi.html'
    def get_context_data(self, **kwargs):
        context = super(anganawadi_district,self).get_context_data(**kwargs)
        id = self.request.GET['dist_id']
        place=Place.objects.filter(status='active',District_id=id)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        print('22222222222',DISTRICT)
        selectdistrict=District.objects.get(status='active',id=id)
        context['selectdistrict']=selectdistrict.District_name
        context['place']=place
        return context

class selected_place(TemplateView):
    template_name = 'districtofficer/add_anganawadi.html'
    def get_context_data(self, **kwargs):
        context = super(selected_place,self).get_context_data(**kwargs)
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

class add_userfood(TemplateView):
    template_name = 'districtofficer/add_userFood.html'
    def get_context_data(self, **kwargs):
        context = super(add_userfood,self).get_context_data(**kwargs)
        footype=foodtype.objects.filter(status='active')
        userfoodtype=tbl_userfood.objects.filter(status='active')
        context['foodtype']=footype
        context['userfoodtype']=userfoodtype
        return context
    def post(self,request,*args,**kwargs):
        foodname= request.POST['name']
        print(foodname)
        footype=request.POST['foodtype']
        print(footype)
        details=request.POST['FOODdetails']
        print(details)
        FOODTYPE=foodtype.objects.get(id=footype)
        userfoodtype=tbl_userfood()
        districtofficer =Districtofficer.objects.get(user_id=self.request.user.id)
        userfoodtype.dofficer_id_id=districtofficer.id
        userfoodtype.food_description=details
        userfoodtype.food_name=foodname
        userfoodtype.status='active'
        userfoodtype.foodtype_id_id=FOODTYPE.id
        image= request.FILES['Image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        userfoodtype.food_pic=file
        userfoodtype.save()
        return redirect(request.META['HTTP_REFERER'])


class add_prengantFood(TemplateView):
    template_name = 'districtofficer/add_pregnantFood.html'
    def get_context_data(self, **kwargs):
        context = super(add_prengantFood,self).get_context_data(**kwargs)
        footype=foodtype.objects.filter(status='active')
        pregnantfood=tbl_pwomenfood.objects.all()
        context['pregnantfood']=pregnantfood
        context['foodtype']=footype
        return context
    def post(self,request,*args,**kwargs):
        foodname= request.POST['name']
        print(foodname)
        footype=request.POST['foodtype']
        amound=request.POST['Amount']
        duration=request.POST['Duration']
        print(footype)
        details=request.POST['FOODdetails']
        print(details)
        FOODTYPE=foodtype.objects.get(id=footype)
        pregnantfoodtype=tbl_pwomenfood()
        districtofficer =Districtofficer.objects.get(user_id=self.request.user.id)
        pregnantfoodtype.dofficer_id_id=districtofficer.id
        pregnantfoodtype.food_description=details
        pregnantfoodtype.pfood_name=foodname
        pregnantfoodtype.status='active'
        pregnantfoodtype.pfood_amt=amound
        pregnantfoodtype.pfood_duration=duration
        pregnantfoodtype.foodtype_id_id=FOODTYPE.id
        image= request.FILES['Image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        pregnantfoodtype.food_pic=file
        pregnantfoodtype.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_pregnantfood(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_pwomenfood.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class remove_userfood(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_userfood.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class user_food_request_pending(TemplateView):
    template_name = 'districtofficer/user_food_requestPending.html'
    def get_context_data(self, **kwargs):
        context = super(user_food_request_pending,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        foodstockrequest=tbl_foodstockrequest.objects.filter(f_status='pending',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=foodstockrequest
        return context

class user_food_request_Accepted(TemplateView):
    template_name = 'districtofficer/user_food_requestAccepted.html'
    def get_context_data(self, **kwargs):
        context = super(user_food_request_Accepted,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        foodstockrequest=tbl_foodstockrequest.objects.filter(f_status='accepted',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=foodstockrequest
        return context



class user_food_request_Reject(TemplateView):
    template_name = 'districtofficer/user_food_requestReject.html'
    def get_context_data(self, **kwargs):
        context = super(user_food_request_Reject,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        foodstockrequest=tbl_foodstockrequest.objects.filter(f_status='Rejected',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=foodstockrequest
        return context


class pregnant_food_request_pending(TemplateView):
    template_name = 'districtofficer/pregnant_food-requestPending.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_food_request_pending,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        pfoodstockrequest=tbl_pfoodstockrequest.objects.filter(f_status='pending',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=pfoodstockrequest
        return context

class pregnant_food_request_Accepted(TemplateView):
    template_name = 'districtofficer/pregnant_food_requestAccepted.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_food_request_Accepted,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        pfoodstockrequest=tbl_pfoodstockrequest.objects.filter(f_status='accepted',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=pfoodstockrequest
        return context

class pregnant_food_request_Reject(TemplateView):
    template_name = 'districtofficer/pregnant_food_requestReject.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_food_request_Reject,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        pfoodstockrequest=tbl_pfoodstockrequest.objects.filter(f_status='Rejected',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=pfoodstockrequest
        return context


class Remove_anganawadi(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        Anganawadi=anganawadi.objects.get(id=id)
        Users= User.objects.get(id=Anganawadi.user_id)
        Users.last_name=0
        Users.save()
        Anganawadi.a_status='reject'
        Anganawadi.save()
        return redirect(request.META['HTTP_REFERER'])

class Accept_anganawadi(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        Anganawadi=anganawadi.objects.get(id=id)
        Users= User.objects.get(id=Anganawadi.user_id)
        Users.last_name=1
        Users.save()
        Anganawadi.a_status='active'
        Anganawadi.save()
        return redirect(request.META['HTTP_REFERER'])

class user_request_accept(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodstock= tbl_foodstockrequest.objects.get(id=id)
        District =Districtofficer.objects.get(user_id=self.request.user.id)
        foodstock.dofficer_id_id=District.id
        foodstock.f_status ="accepted"
        foodstock.save()
        return redirect(request.META['HTTP_REFERER'])


class user_request_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodstock= tbl_foodstockrequest.objects.get(id=id)
        District =Districtofficer.objects.get(user_id=self.request.user.id)
        foodstock.dofficer_id_id=District.id
        foodstock.f_status ="Rejected"
        foodstock.save()
        return redirect(request.META['HTTP_REFERER'])


class pregnant_request_accept(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodstock= tbl_pfoodstockrequest.objects.get(id=id)
        District =Districtofficer.objects.get(user_id=self.request.user.id)
        foodstock.dofficer_id_id=District.id
        foodstock.f_status ="accepted"
        foodstock.save()
        return redirect(request.META['HTTP_REFERER'])


class pregnant_request_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodstock= tbl_pfoodstockrequest.objects.get(id=id)
        District =Districtofficer.objects.get(user_id=self.request.user.id)
        foodstock.dofficer_id_id=District.id
        foodstock.f_status ="Rejected"
        foodstock.save()
        return redirect(request.META['HTTP_REFERER'])


class child_food_request_pending(TemplateView):
    template_name = 'districtofficer/child_food_requestPending.html'
    def get_context_data(self, **kwargs):
        context = super(child_food_request_pending,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        foodstockrequest=tbl_childfoodstockrequest.objects.filter(f_status='pending',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=foodstockrequest
        return context

class child_food_request_Accepted(TemplateView):
    template_name = 'districtofficer/child_food_requestAccepted.html'
    def get_context_data(self, **kwargs):
        context = super(child_food_request_Accepted,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        foodstockrequest=tbl_childfoodstockrequest.objects.filter(f_status='accepted',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=foodstockrequest
        return context



class child_food_request_Reject(TemplateView):
    template_name = 'districtofficer/child_food_requestReject.html'
    def get_context_data(self, **kwargs):
        context = super(child_food_request_Reject,self).get_context_data(**kwargs)
        distric = Districtofficer.objects.get(user_id=self.request.user.id)
        foodstockrequest=tbl_childfoodstockrequest.objects.filter(f_status='Rejected',user_id__dofficer_id=distric.id)
        context['foodstockrequest']=foodstockrequest
        return context

class child_request_accept(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodstock= tbl_childfoodstockrequest.objects.get(id=id)
        District =Districtofficer.objects.get(user_id=self.request.user.id)
        foodstock.dofficer_id_id=District.id
        foodstock.f_status ="accepted"
        foodstock.save()
        return redirect(request.META['HTTP_REFERER'])


class child_request_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodstock= tbl_childfoodstockrequest.objects.get(id=id)
        District =Districtofficer.objects.get(user_id=self.request.user.id)
        foodstock.dofficer_id_id=District.id
        foodstock.f_status ="Rejected"
        foodstock.save()
        return redirect(request.META['HTTP_REFERER'])
