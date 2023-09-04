from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import auth, User

from anganwadi_app.models import foodtype, complainttype, prooftype, District, Place, Location, Districtofficer, \
    UserType,Districtofficer, tbl_feedback, tbl_complaint, anganawadi, tbl_user, tbl_pwomens, tbl_child


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class indexViews(TemplateView):
    template_name = 'admin/admin_index.html'

class addproof_type(TemplateView):
    template_name = 'admin/addproof_type.html'
    def get_context_data(self, **kwargs):
        context = super(addproof_type,self).get_context_data(**kwargs)
        PROOF=prooftype.objects.filter(status='active')
        context['PROOF']=PROOF
        return context

    def post(self,request,*args,**kwargs):
        PROOFS=request.POST['proof']
        PROOF=prooftype()
        PROOF.proof_type=PROOFS
        PROOF.status='active'
        PROOF.save()
        return redirect(request.META['HTTP_REFERER'])
class remove_prooftype(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        prooftype.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class edit_prooftype(TemplateView):
    template_name = 'admin/editprooftype.html'
    def get_context_data(self, **kwargs):
        context = super(edit_prooftype,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        PROOF=prooftype.objects.get(status='active',id=id)
        context['proof_id']=PROOF.id
        context['prooftype']=PROOF.proof_type
        return context

    def post(self,request,*args,**kwargs):

        complaints=request.POST['proof']
        proofid=request.POST['proof_id']
        PROOF=prooftype.objects.get(id=proofid)
        PROOF.proof_type=complaints
        PROOF.status='active'
        PROOF.save()
        return redirect(request.META['HTTP_REFERER'])

class addcomplaint_type(TemplateView):
    template_name = 'admin/addcomplaint_type.html'
    def get_context_data(self, **kwargs):
        context = super(addcomplaint_type,self).get_context_data(**kwargs)
        COMP=complainttype.objects.filter(status='active')
        context['complaints']=COMP
        return context

    def post(self,request,*args,**kwargs):
        complaints=request.POST['complaints']
        COMP=complainttype()
        COMP.Complainttype=complaints
        COMP.status='active'
        COMP.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_complainttype(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        complainttype.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class edit_complainttype(TemplateView):
    template_name = 'admin/editcomplainttype.html'
    def get_context_data(self, **kwargs):
        context = super(edit_complainttype,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        COMP=complainttype.objects.get(status='active',id=id)
        context['complaint_id']=COMP.id
        context['complaint']=COMP.Complainttype
        return context

    def post(self,request,*args,**kwargs):

        complaints=request.POST['complaints']
        compl_id=request.POST['complaint_id']
        COM=complainttype.objects.get(id=compl_id)
        COM.Complainttype=complaints
        COM.status='active'
        COM.save()
        return redirect(request.META['HTTP_REFERER'])

class addfood_type(TemplateView):
    template_name = 'admin/addfood_type.html'
    def get_context_data(self, **kwargs):
        context = super(addfood_type,self).get_context_data(**kwargs)
        FOOD=foodtype.objects.filter(status='active')
        context['food']=FOOD
        return context

    def post(self,request,*args,**kwargs):
        Foodtype=request.POST['foodtype']
        food=foodtype()
        food.foodtype=Foodtype
        food.status='active'
        food.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_foodtype(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        foodtype.objects.get(id=id).delete()

        return redirect(request.META['HTTP_REFERER'])

class edit_foodtype(TemplateView):
    template_name = 'admin/editfoodtype.html'
    def get_context_data(self, **kwargs):
        context = super(edit_foodtype,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        FOOD=foodtype.objects.get(status='active',id=id)
        context['food_id']=FOOD.id
        context['food']=FOOD.foodtype
        print(FOOD.foodtype)
        return context

    def post(self,request,*args,**kwargs):

        Foodtype=request.POST['foodtype']
        foodid=request.POST['foodid']
        food=foodtype.objects.get(id=foodid)
        food.foodtype=Foodtype
        food.status='active'
        food.save()
        return redirect(request.META['HTTP_REFERER'])


class add_district(TemplateView):
    template_name = 'admin/add_district.html'
    def get_context_data(self, **kwargs):
        context = super(add_district,self).get_context_data(**kwargs)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        return context

    def post(self,request,*args,**kwargs):
        Districtname=request.POST['district']
        district=District()
        district.District_name=Districtname
        district.status='active'
        district.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_district(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        District.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class add_place(TemplateView):
    template_name = 'admin/add_place.html'
    def get_context_data(self, **kwargs):
        context = super(add_place,self).get_context_data(**kwargs)
        PLACE=Place.objects.filter(status='active')
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        context['place']=PLACE
        return context

    def post(self,request,*args,**kwargs):
        PLACE=request.POST['place']
        add_district=request.POST['slctDistrict']
        district=Place()
        district.place=PLACE
        district.District_id=add_district
        district.status='active'
        district.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_place(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        Place.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])


class add_location(TemplateView):
    template_name = 'admin/add_locations.html'
    def get_context_data(self, **kwargs):
        context = super(add_location,self).get_context_data(**kwargs)
        PLACE=Place.objects.filter(status='active')
        DISTRICT=District.objects.filter(status='active')
        location=Location.objects.filter(status='active')
        context['district']=DISTRICT

        context['location']=location
        context['place']=PLACE
        return context

    def post(self,request,*args,**kwargs):
        PLACE=request.POST['PLACEs']
        add_district=request.POST['slctDistrict']
        LOCATION=request.POST['location']
        locat=Location()
        locat.location=LOCATION
        locat.place_id=PLACE
        locat.status='active'
        locat.save()
        return redirect(request.META['HTTP_REFERER'])

class remove_location(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        Location.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class add_districtofficers(TemplateView):
    template_name = 'admin/add_districtofficers.html'
    def get_context_data(self, **kwargs):
        context = super(add_districtofficers,self).get_context_data(**kwargs)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        proof=prooftype.objects.filter(status='active')
        context['proof']=proof
        return context
    def post(self,request,*arg,**kwargs):
        name=request.POST['name']
        print(name)
        Phone=request.POST['phone']
        print(Phone)
        email=request.POST['email']
        Housename=request.POST['housename']
        Location=request.POST['location']
        prooftype=request.POST['prooftype']
        PROOF= request.FILES['proofdoc']
        f = FileSystemStorage()
        prooffile = f.save(PROOF.name, PROOF)
        image= request.FILES['image']
        j = FileSystemStorage()
        file = j.save(image.name, image)
        password=request.POST['password']
        confirmpsw=request.POST['ConfirmPassword']
        username=request.POST['username']
        street=request.POST['street']
        pincode=request.POST['pincode']


        user = User.objects.create_user(first_name = name,email=email,password=password,username=username,last_name=1)
        user.save()
        print('bbbbbbbbbbbbbbbbbbbbbbbb')
        DIST= Districtofficer()
        DIST.user=user
        DIST.phone = Phone
        DIST.emil =email
        DIST.housename = Housename
        DIST.location_id = Location
        DIST.id_proof = prooffile
        DIST.Image = file
        DIST.street = street
        DIST.pincode = pincode
        DIST.status = 'active'
        DIST.password = password
        DIST.prooftype_id=prooftype
        DIST.confirmpassword = confirmpsw

        usertype = UserType()
        usertype.user = user
        usertype.type = 'districofficer'
        usertype.save()
        DIST.save()
        return render(request,'admin/admin_index.html',{'messages':'successfully registered'})





class officers_district(TemplateView):
    template_name = 'admin/add_districtofficers.html'
    def get_context_data(self, **kwargs):
        context = super(officers_district,self).get_context_data(**kwargs)
        id = self.request.GET['dist_id']
        place=Place.objects.filter(status='active',District_id=id)
        DISTRICT=District.objects.filter(status='active')
        context['district']=DISTRICT
        selectdistrict=District.objects.get(status='active',id=id)
        context['selectdistrict']=selectdistrict.District_name
        context['place']=place
        proof=prooftype.objects.filter(status='active')
        context['proof']=proof
        return context

class selected_place(TemplateView):
    template_name = 'admin/add_districtofficers.html'
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
        proof=prooftype.objects.filter(status='active')
        context['proof']=proof
        return context


class view_districtofficers(TemplateView):
    template_name = 'admin/view_districtofficers.html'
    def get_context_data(self, **kwargs):
        context = super(view_districtofficers,self).get_context_data(**kwargs)
        districtofficer=Districtofficer.objects.filter(status='active')
        context['Districtofficer']=districtofficer
        return context

class Delete_districtofficers(View):
     def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        Districtofficer.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])

class view_user_feedback(TemplateView):
    template_name = 'admin/view_userfeedback.html'
    def get_context_data(self, **kwargs):
        context = super(view_user_feedback,self).get_context_data(**kwargs)
        feedback =tbl_feedback.objects.filter(usertype="user")
        context['feedback']=feedback
        return context

class view_pregnant_feedback(TemplateView):
    template_name = 'admin/view_pregnantfeedback.html'
    def get_context_data(self, **kwargs):
        context = super(view_pregnant_feedback,self).get_context_data(**kwargs)
        feedback =tbl_feedback.objects.filter(usertype="pregnant")
        context['feedback']=feedback
        return context

class user_complaints(TemplateView):
    template_name = 'admin/user_complaints.html'
    def get_context_data(self, **kwargs):
        context = super(user_complaints,self).get_context_data(**kwargs)
        complaint =tbl_complaint.objects.filter(usertype="user")
        print("ssssss",complaint)
        context['complaint']=complaint
        return context

class pregnant_complaints(TemplateView):
    template_name = 'admin/pregnant_complaints.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_complaints,self).get_context_data(**kwargs)
        complaint =tbl_complaint.objects.filter(usertype="pregnant")
        print("ssssss",complaint)
        context['complaint']=complaint
        return context

class curent_report(TemplateView):
    template_name = 'admin/curent_report.html'
    def get_context_data(self, **kwargs):
        context =super(curent_report,self).get_context_data(**kwargs)
        Anganwadi = anganawadi.objects.all()
        context['Anganwadi']= Anganwadi
        return context
    def post(self,request,*args,**kwargs):
        Anganwadis = request.POST['Anganwadi']
        options= request.POST['options']
        startdate =request.POST['start_date']
        enddate = request.POST['end_date']
        ang=anganawadi.objects.get(id=Anganwadis)
        if options=='user':
            Users=tbl_user.objects.filter(user_status='accepted',location_id=ang.location_id)
            return render(request,'admin/user_report.html',{'result':Users})
        elif options=='child':
            child=tbl_child.objects.filter(a_id=Anganwadis)
            return render(request,'admin/child_report.html',{'result':child})
        elif options=='pregnant':
            Pregnant = tbl_pwomens.objects.filter(pwomen_isactive='accepted')
            return render(request,'admin/pregnant_report.html',{'result':Pregnant})
        else:
            return render(request,'admin/curent_report.html')


class pregnant_complaint_reply(TemplateView):
    template_name = 'admin/pregnant_complaints.html'
    def get_context_data(self, **kwargs):
        context = super(pregnant_complaint_reply,self).get_context_data(**kwargs)
        complaint =tbl_complaint.objects.filter(usertype="pregnant")
        print("ssssss",complaint)
        context['complaint']=complaint
        return context
    def post(self,request,*args,**kwargs):
        id=request.POST['id']
        complaints= request.POST['reply']
        complaint =tbl_complaint.objects.get(usertype="pregnant",id=id)
        complaint.complaint_reply = complaints
        complaint.complaint_status = "replied"
        complaint.save()
        print("ssssss",complaint)
        return redirect(request.META['HTTP_REFERER'])

class user_complaint_reply(TemplateView):
     def get_context_data(self, **kwargs):
        context = super(user_complaint_reply,self).get_context_data(**kwargs)
        complaint =tbl_complaint.objects.filter(usertype="user")
        context['complaint']=complaint
        return context
     def post(self,request,*args,**kwargs):
        id=request.POST['id']
        complaints= request.POST['reply']
        complaint =tbl_complaint.objects.get(usertype="user",id=id)
        complaint.complaint_reply = complaints
        complaint.complaint_status ="replied"
        complaint.save()
        print("ssssss",complaint)
        return redirect(request.META['HTTP_REFERER'])

class user_report(TemplateView):
    template_name = 'admin/user_report.html'

class pregnant_report(TemplateView):
    template_name = 'admin/pregnant_report.html'

class child_report(TemplateView):
    template_name = 'admin/child_report.html'