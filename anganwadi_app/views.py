from django.contrib.auth import login
from django.contrib.auth.models import auth, User
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from anganwadi import settings
from anganwadi_app.models import UserType, District, Place, Location, tbl_user, tbl_pwomens, Districtofficer, anganawadi


class Index(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            if user.last_name=='1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type=="user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "districofficer":
                    return redirect('/districtofficer')
                elif UserType.objects.get(user_id=user.id).type == "anganwadi":
                    return redirect('/anganwadi')
                elif UserType.objects.get(user_id=user.id).type == "pregnant":
                    return redirect('/pregnant')

            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})

class user_registration(TemplateView):
    template_name = 'user_registration.html'
    def get_context_data(self, **kwargs):
        context = super(user_registration,self).get_context_data(**kwargs)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        return context



class User_place(TemplateView):
    template_name = 'user_registration.html'
    def get_context_data(self, **kwargs):
        context = super(User_place,self).get_context_data(**kwargs)
        id = self.request.GET['dist_id']
        place=Place.objects.filter(status='active',District_id=id)
        print("11111111111111111111111111111111111111111111111111111",place)
        DISTRICT=District.objects.filter(status='active')
        selectdistrict=District.objects.get(status='active',id=id)
        context['district']=DISTRICT
        context['selectdistrict']=selectdistrict.District_name
        context['place']=place
        return context

class User_location(TemplateView):
    template_name = 'user_registration.html'
    def get_context_data(self, **kwargs):
        context = super(User_location,self).get_context_data(**kwargs)
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

    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        print(email)
        age=request.POST['Age']
        print(age)
        Phone=request.POST['phone']
        print(Phone)
        L_id=request.POST['location']
        print(L_id)
        PROOF= request.FILES['proofdoc']
        f = FileSystemStorage()
        prooffile = f.save(PROOF.name, PROOF)
        House=request.POST['House']
        print(House)
        street=request.POST['street']
        print(street)
        pincode=request.POST['pincode']
        print(pincode)
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        confirmpassword=request.POST['ConfirmPassword']
        print(confirmpassword)
        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=0)
            PLACE=Location.objects.get(status='active',id=L_id)
            print(PLACE)
            table_user=tbl_user()
            table_user.user_id =user.id
            table_user.place_id_id = PLACE.place.id
            table_user.location_id_id = L_id
            table_user.user_age = age
            table_user.user_certificate = prooffile
            table_user.user_contact   = Phone
            table_user.user_email       = email
            table_user.user_housename   = House
            table_user.user_name        = name
            table_user.user_username    = username
            table_user.user_pincode     =pincode
            table_user.user_street      =street
            table_user.user_status      = 1
            table_user.user_password    = password
            table_user.usser_confirm    = confirmpassword
            usertype = UserType()
            usertype.user = user
            usertype.type = 'user'
            usertype.save()
            table_user.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})



class pregnant_registration(TemplateView):
    template_name = 'pregnant_registration.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_registration,self).get_context_data(**kwargs)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        return context



class pregnant_place(TemplateView):
    template_name = 'pregnant_registration.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_place,self).get_context_data(**kwargs)
        id = self.request.GET['dist_id']
        place=Place.objects.filter(status='active',District_id=id)
        DISTRICT=District.objects.filter(status='active')
        selectdistrict=District.objects.get(status='active',id=id)
        context['district']=DISTRICT
        context['selectdistrict']=selectdistrict.District_name
        context['place']=place
        return context

class Pregnant_location(TemplateView):
    template_name = 'pregnant_registration.html'
    def get_context_data(self, **kwargs):
        context = super(Pregnant_location,self).get_context_data(**kwargs)
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

    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        print(email)
        age=request.POST['Age']
        print(age)
        Phone=request.POST['phone']
        print(Phone)
        L_id=request.POST['location']
        print(L_id)
        PROOF= request.FILES['proof']
        f = FileSystemStorage()
        prooffile = f.save(PROOF.name, PROOF)
        image= request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        husbandname=request.POST['husbandname']
        print(husbandname)
        street=request.POST['street']
        print(street)
        pincode=request.POST['pincode']
        print(pincode)
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        confirmpassword=request.POST['ConfirmPassword']
        house =request.POST['house']
        print(confirmpassword)
        try:
            user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=0)
            PLACE=Location.objects.get(status='active',id=L_id)
            print(PLACE)
            table_pregnant=tbl_pwomens()
            table_pregnant.user_id =user.id
            table_pregnant.place_id_id = PLACE.place.id
            table_pregnant.location_id_id = L_id
            table_pregnant.pwomen_age = age
            table_pregnant.pwomen_medicalproof = prooffile
            table_pregnant.pwomen_contact   = Phone
            table_pregnant.pwomen_email       = email
            table_pregnant.pwomen_husbandname  = husbandname
            table_pregnant.pwomen_name        = name
            table_pregnant.pwomen_username    = username
            table_pregnant.pwomen_pincode     =pincode
            table_pregnant.pwomen_photo=file
            table_pregnant.p_street      =street
            table_pregnant.pwomen_isactive      = 1
            table_pregnant.pwomen_password    = password
            table_pregnant.pwomen_confirmpassword    = confirmpassword
            table_pregnant.pwomen_house = house
            usertype = UserType()
            usertype.user = user
            usertype.type = 'pregnant'
            usertype.save()
            table_pregnant.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

class FrogotpasswordView1(TemplateView):
    template_name = 'change_password.html'
    # def get_context_data(self, **kwargs):
    #     context=super(FrogotpasswordView1,self).get_context_data(**kwargs)
    #     USER=tbl_user.objects.filter(user__last_name='1').count()
    #     PREGNANT =tbl_pwomens.objects.filter(user__last_name='1').count()
    #     DISTRICTOFFICER=Districtofficer.objects.filter(user__last_name='1').count()
    #     admin=User.objects.get(is_superuser='1')
    #     context['USER'] = USER
    #     context['PREGNANT'] = PREGNANT
    #     context['DISTRICTOFFICER'] = DISTRICTOFFICER
    #     context['admin']=admin
    #     return context
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        print(name)
        email= request.POST['email']
        print(email)
        user_id=self.request.user.id
        if User.objects.filter(last_name='1',first_name=name,email=email):
           user=User.objects.get(last_name='1',first_name=name,email=email)
           Type=UserType.objects.get(user_id=user.id)
           if Type.type=='user':
              USERs=tbl_user.objects.get(user_id=user.id)
              Password=USERs.user_password
              email = EmailMessage(
              'Your password',
              USERs.user_password,
              settings.EMAIL_HOST_USER,
              [user.email],
              )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'messages':"Send mail successfully"})
           elif Type.type=='pregnant':

              pregnant=tbl_pwomens.objects.get(user_id=user.id)
              print(user)
              email = EmailMessage(
              'Your password',
              pregnant.pwomen_password,
              settings.EMAIL_HOST_USER,
              [user.email],
               )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'messages':"Send mail successfully"})
           elif Type.type=='districofficer':

              disoffice=Districtofficer.objects.get(user_id=user.id)
              print(user)
              email = EmailMessage(
              'Your password',
              disoffice.password,
              settings.EMAIL_HOST_USER,
              [user.email],
               )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'messages':"Send mail successfully"})
           elif Type.type=='anganwadi':

              Anganawadi=anganawadi.objects.get(user_id=user.id)

              email = EmailMessage(
              'Your password',
              Anganawadi.a_password,
              settings.EMAIL_HOST_USER,
              [user.email],
               )
              email.fail_silently = False
              email.send()
              return render(request,'index.html',{'messages':"Send mail successfully"})

        else:
           return render(request,'index.html',{'message':"Tis User Is Not Exist"})