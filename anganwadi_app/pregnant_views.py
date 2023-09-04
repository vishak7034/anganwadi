from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import auth, User
from anganwadi_app.models import tbl_pwomens, tbl_healthtips, tbl_pwomenfood, Districtofficer, Place, anganawadi, \
    tbl_complaint, tbl_feedback, complainttype, tbl_userfoodservice, tbl_pwomenfoodservice, tbl_pfoodbooking


class IndexView(TemplateView):
    template_name = 'pregnant/pregnant_index.html'

class profile(TemplateView):
    template_name = 'pregnant/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile,self).get_context_data(**kwargs)
        id =self.request.user.id
        PREGNANT=tbl_pwomens.objects.get(user_id=id)
        print(PREGNANT)
        context['PREGNANT']=PREGNANT
        return context

class edit_profile(TemplateView):
    template_name = 'pregnant/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        id =self.request.user.id
        pregnat=tbl_pwomens.objects.get(user_id=id)
        context['USER']=pregnat
        return context

    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        email=request.POST['email']
        print(email)
        Phone=request.POST['phone']
        print(Phone)
        House=request.POST['House']
        print(House)
        image = request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        id =self.request.user.id
        table_user=tbl_pwomens.objects.get(user_id=id)
        id =self.request.user.id
        table_user.user_id =id
        table_user.pwomen_contact   = Phone
        table_user.pwomen_email       = email
        table_user.pwomen_house  = House
        table_user.pwomen_name        = name
        table_user.pwomen_photo = file
        table_user.save()
        return redirect(request.META['HTTP_REFERER'])

class AnganwadiServices(TemplateView):
    template_name = 'pregnant/AnganwadiServices.html'

class viewFoods(TemplateView):
    template_name = 'pregnant/viewFoods.html'
    def get_context_data(self, **kwargs):
        context = super(viewFoods,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        food=tbl_pwomenfood.objects.all()
        context['food']=food
        return context

class ViewHealthTips(TemplateView):
    template_name = 'pregnant/ViewHealthTips.html'
    def get_context_data(self, **kwargs):
        context = super(ViewHealthTips,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        table_healthtips=tbl_healthtips.objects.all()
        context['healthtips']=table_healthtips
        return context

class ViewAnganwadils(TemplateView):
    template_name = 'pregnant/ViewAnganwadils.html'
    def get_context_data(self, **kwargs):
        context = super(ViewAnganwadils,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        place=Place.objects.all()
        context['place']=place
        return context
    def post(self,request,*args,**kwargs):
        loca_id= request.POST['location']
        print(loca_id)
        result=anganawadi.objects.filter(location_id_id=loca_id)
        print("dddddddddddddddddddddddddddd",result)
        place=Place.objects.all()

        return render(request, 'pregnant/ViewAnganwadils.html', {'result':result,'place':place})

class ViewDistrictOfficer(TemplateView):
    template_name = 'pregnant/ViewDistrictOfficer.html'
    def get_context_data(self, **kwargs):
        context = super(ViewDistrictOfficer,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        districtofficer=Districtofficer.objects.all()
        context['districtofficer']=districtofficer
        return context

class ViewFoodStock(TemplateView):
    template_name = 'pregnant/ViewFoodStock.html'
    def get_context_data(self, **kwargs):
        context = super(ViewFoodStock,self).get_context_data(**kwargs)
        USERs=tbl_pwomens.objects.get(user_id=self.request.user.id)
        Anganawadi=anganawadi.objects.get(location_id__id=USERs.location_id.id)
        pwomenfoodservice=tbl_pwomenfoodservice.objects.filter(anganwadi_id_id__location_id_id=Anganawadi.location_id.id).order_by('-upload_date')
        print(pwomenfoodservice)
        context['pwomenfoodservice']=pwomenfoodservice
        return context

class myrequest(TemplateView):
    template_name = 'pregnant/myrequest.html'
    def get_context_data(self, **kwargs):
        context = super(myrequest,self).get_context_data(**kwargs)
        pfoodbooking =tbl_pfoodbooking.objects.filter(pwomen_id=self.request.user.id)
        context['pfoodbooking']=pfoodbooking
        return context

class complaint(TemplateView):
    template_name = 'pregnant/Complaint.html'
    def get_context_data(self, **kwargs):
        context = super(complaint,self).get_context_data(**kwargs)
        USERs=tbl_pwomens.objects.get(user_id=self.request.user.id)

        Complainttype=complainttype.objects.all()
        context['Complainttype']=Complainttype

        result=tbl_complaint.objects.filter(pwomen_id_id=USERs.id)
        context['result']=result
        return context
    def post(self,request,*args,**kwargs):
        USER=tbl_pwomens.objects.get(user_id=self.request.user.id)
        complaint_id =request.POST['complaint_id']
        Complainttype=complainttype.objects.get(id=complaint_id)
        complaints= request.POST['complaint']
        tablecomplaint=tbl_complaint()
        tablecomplaint.complaint=complaints
        tablecomplaint.pwomen_id_id = USER.id
        tablecomplaint.complaint_status="pending"
        tablecomplaint.complainttype_id_id=Complainttype.id
        tablecomplaint.usertype="pregnant"
        tablecomplaint.save()

        Complainttype=complainttype.objects.all()

        return redirect(request.META['HTTP_REFERER'])

class feedback(TemplateView):
    template_name = 'pregnant/Feedback.html'
    def get_context_data(self, **kwargs):
        context = super(feedback,self).get_context_data(**kwargs)
        USERs=tbl_pwomens.objects.get(user_id=self.request.user.id)
        result=tbl_feedback.objects.filter(pwomen_id_id=USERs.id)
        context['result']=result
        return context

    def post(self,request,*args,**kwargs):
        USER=tbl_pwomens.objects.get(user_id=self.request.user.id)
        feedbacks= request.POST['feedback']
        fdb=tbl_feedback()
        fdb.feedback = feedbacks
        fdb.pwomen_id_id= USER.id
        fdb.usertype="pregnant"
        fdb.save()
        return redirect(request.META['HTTP_REFERER'])

class removecomplaint(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_complaint.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class removefeedback(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        tbl_feedback.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class change_password(TemplateView):
    template_name = 'pregnant/change_password.html'
    def post(self,request,*args,**kwargs):
        id=self.request.user.id
        username=User.objects.get(id=id)
        password1=request.POST['password1']
        password2=request.POST['password2']
        password3=request.POST['password3']
        if password2== password3:
            user = authenticate(username=username,password=password1,id=id)
            try:
                 if user is not None:
                   a= user.set_password(password2)
                   print("1111111111111111",a)
                   return render(request,'Index.html',{'messages':"Update password"})
                 else:
                   return render(request,'pregnant/pregnant_index.html',{'messages':"user is not exist"})

            except:
                  return render(request,'pregnant/pregnant_index.html',{'messages':"user is not exist"})
        else:
             return render(request,'pregnant/pregnant_index.html',{'messages':"Retype is not correct"})


class accept_foodrequestrequest(TemplateView):
    template_name = 'pregnant/ViewFoodStock.html'
    def get_context_data(self, **kwargs):
        context = super(accept_foodrequestrequest,self).get_context_data(**kwargs)
        # foodbooking =tbl_pfoodbooking.objects.filter(pwomen_id=self.request.user.id,pfoodbooking_status="Request accept")
        id = self.request.GET['id']
        Users = User.objects.get(id=self.request.user.id)
        try:
            id = self.request.GET['id']
            if tbl_pfoodbooking.objects.filter(pwomen_id=self.request.user.id,pfoodbooking_status="Request accept",pwomenfoodservice_id=id) :
                context['messages']="Request already accepted"
                return context
            else:
                pfoodservice=tbl_pwomenfoodservice.objects.get(id=id)
                pfoodbooking =tbl_pfoodbooking()
                pfoodbooking.pfoodbooking_status = "Request accept"
                pfoodbooking.pwomen_id_id           = Users.id
                pfoodbooking.pwomenfoodservice_id_id = pfoodservice.id
                pfoodbooking.anganwadi_id=pfoodservice.anganwadi_id
                pfoodbooking.save()
                context['messages']="Request accepted"
                return context
        except:
                pfoodservice=tbl_pwomenfoodservice.objects.get(id=id)
                pfoodbooking =tbl_pfoodbooking()
                pfoodbooking.pfoodbooking_status = "Request accept"
                pfoodbooking.pwomen_id_id           = Users.id
                pfoodbooking.pwomenfoodservice_id_id = pfoodservice.id
                pfoodbooking.anganwadi_id=pfoodservice.anganwadi_id
                pfoodbooking.save()
                context['messages']="Request accepted"
                return context
