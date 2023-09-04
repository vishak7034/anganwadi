import datetime
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

from anganwadi_app.models import tbl_user, tbl_healthtips, tbl_userfood, Place, anganawadi, Districtofficer, \
    complainttype, tbl_complaint, tbl_feedback, tbl_pfoodbooking, tbl_foodbooking, tbl_userfoodservice
from django.contrib.auth.models import auth, User

class IndexView(TemplateView):
    template_name = 'user/user_index.html'

class profile(TemplateView):
    template_name = 'user/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile,self).get_context_data(**kwargs)
        id =self.request.user.id
        USER=tbl_user.objects.get(user_id=id)
        context['USER']=USER
        return context

class edit_profile(TemplateView):
    template_name = 'user/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        id =self.request.user.id
        USER=tbl_user.objects.get(user_id=id)
        context['USER']=USER
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
        id =self.request.user.id
        table_user=tbl_user.objects.get(user_id=id)
        id =self.request.user.id
        table_user.user_id =id
        table_user.user_contact   = Phone
        table_user.user_email       = email
        table_user.user_housename   = House
        table_user.user_name        = name
        table_user.save()
        return redirect(request.META['HTTP_REFERER'])

class AnganwadiServices(TemplateView):
    template_name = 'user/AnganwadiServices.html'


class viewFoods(TemplateView):
    template_name = 'user/viewFoods.html'
    def get_context_data(self, **kwargs):
        context = super(viewFoods,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        food=tbl_userfood.objects.all()
        context['food']=food
        return context

class ViewHealthTips(TemplateView):
    template_name = 'user/ViewHealthTips.html'
    def get_context_data(self, **kwargs):
        context = super(ViewHealthTips,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        table_healthtips=tbl_healthtips.objects.all()
        context['healthtips']=table_healthtips
        return context

class ViewAnganwadils(TemplateView):
    template_name = 'user/ViewAnganwadils.html'
    def get_context_data(self, **kwargs):
        context = super(ViewAnganwadils,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        place=Place.objects.all()
        context['place']=place
        return context
    def post(self,request,*args,**kwargs):
        loca_id= request.POST['location']
        print(loca_id)
        result=anganawadi.objects.filter(place_id_id=loca_id)
        print("dddddddddddddddddddddddddddd",result)
        place=Place.objects.all()

        return render(request, 'user/ViewAnganwadils.html', {'result':result,'place':place})

class ViewDistrictOfficer(TemplateView):
    template_name = 'user/ViewDistrictOfficer.html'
    def get_context_data(self, **kwargs):
        context = super(ViewDistrictOfficer,self).get_context_data(**kwargs)
        # Anganawadi=anganawadi.objects.get(user_id=self.request.user.id)
        districtofficer=Districtofficer.objects.all()
        context['districtofficer']=districtofficer
        return context
class ViewFoodStock(TemplateView):
    template_name = 'user/ViewFoodStock.html'
    def get_context_data(self, **kwargs):
        context = super(ViewFoodStock,self).get_context_data(**kwargs)
        USERs=tbl_user.objects.get(user_id=self.request.user.id)
        Anganawadi=anganawadi.objects.get(location_id__id=USERs.location_id.id)
        foodservice=tbl_userfoodservice.objects.filter(anganwadi_id_id__location_id_id=Anganawadi.location_id.id).order_by('-upload_date')
        context['foodservice']=foodservice
        return context

class myrequest(TemplateView):
    template_name = 'user/myrequest.html'
    def get_context_data(self, **kwargs):
        context = super(myrequest,self).get_context_data(**kwargs)
        foodbooking =tbl_foodbooking.objects.filter(user_id=self.request.user.id)
        context['foodbooking']=foodbooking
        return context

class complaint(TemplateView):
    template_name = 'user/Complaint.html'
    def get_context_data(self, **kwargs):
        context = super(complaint,self).get_context_data(**kwargs)
        USERs=tbl_user.objects.get(user_id=self.request.user.id)

        Complainttype=complainttype.objects.all()
        context['Complainttype']=Complainttype

        result=tbl_complaint.objects.filter(user_id_id=USERs.id)
        context['result']=result
        return context
    def post(self,request,*args,**kwargs):
        USER=tbl_user.objects.get(user_id=self.request.user.id)
        complaint_id =request.POST['complaint_id']
        Complainttype=complainttype.objects.get(id=complaint_id)
        complaints= request.POST['complaint']
        tablecomplaint=tbl_complaint()
        tablecomplaint.complaint=complaints
        tablecomplaint.user_id_id = USER.id
        tablecomplaint.complaint_status="pending"
        tablecomplaint.complainttype_id_id=Complainttype.id
        tablecomplaint.usertype="user"
        tablecomplaint.save()

        Complainttype=complainttype.objects.all()

        return redirect(request.META['HTTP_REFERER'])

class feedback(TemplateView):
    template_name = 'user/Feedback.html'
    def get_context_data(self, **kwargs):
        context = super(feedback,self).get_context_data(**kwargs)
        USERs=tbl_user.objects.get(user_id=self.request.user.id)
        result=tbl_feedback.objects.filter(user_id_id=USERs.id)
        context['result']=result
        return context
    def post(self,request,*args,**kwargs):
        USER=tbl_user.objects.get(user_id=self.request.user.id)
        feedbacks= request.POST['feedback']
        fdb=tbl_feedback()
        fdb.feedback = feedbacks
        fdb.usertype = "user"
        fdb.user_id_id= USER.id
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


class accept_requests(TemplateView):
    template_name = 'user/ViewFoodStock.html'
    def get_context_data(self, **kwargs):
        context = super(accept_requests,self).get_context_data(**kwargs)
        foodbooking =tbl_foodbooking.objects.filter(user_id=self.request.user.id,foodbooking_status="Request accept")
        id = self.request.GET['id']
        Users = User.objects.get(id=self.request.user.id)
        try:
            id = self.request.GET['id']
            if tbl_foodbooking.objects.filter(user_id=self.request.user.id,foodbooking_status="Request accept",userfoodservice_id=id) :
                context['messages']="Request already accepted"
                return context
            else:
                foodservice=tbl_userfoodservice.objects.get(id=id)
                foodbooking =tbl_foodbooking()
                foodbooking.foodbooking_status = "Request accept"
                foodbooking.user_id_id           = Users.id
                foodbooking.userfoodservice_id_id = foodservice.id
                foodbooking.anganwadi_id=foodservice.anganwadi_id
                foodbooking.save()
                print(2)
                context['messages']="Request accepted"
                return context
        except:
                foodservice=tbl_userfoodservice.objects.get(id=id)
                foodbooking =tbl_foodbooking()
                foodbooking.foodbooking_status = "Request accept"
                foodbooking.user_id_id           = Users.id
                foodbooking.userfoodservice_id_id = foodservice.id
                foodbooking.anganwadi_id=foodservice.anganwadi_id

                foodbooking.save()
                context['messages']="Request accepted"
                return context
