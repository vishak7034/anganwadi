from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=100,null=True)
    Address = models.CharField(max_length=100,null=True)
    emil = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    id_proof= models.ImageField('images/',null=True)
    place = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)



class foodtype(models.Model):
    foodtype = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class complainttype(models.Model):
    Complainttype = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class prooftype(models.Model):
    proof_type = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class District(models.Model):
    District_name = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class Place(models.Model):
    place = models.CharField(max_length=100,null=True)
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True)

class Location(models.Model):
    location = models.CharField(max_length=100,null=True)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True)


class Districtofficer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=100,null=True)
    housename = models.CharField(max_length=100,null=True)
    emil = models.CharField(max_length=100,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    id_proof= models.ImageField('images/',null=True)
    Image= models.ImageField('images/',null=True)
    street = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=100,null=True)
    prooftype = models.ForeignKey(prooftype,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    confirmpassword = models.CharField(max_length=100,null=True)


class anganawadi(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    a_name = models.CharField(max_length=100,null=True)
    location_id =models.ForeignKey(Location,on_delete=models.CASCADE)
    a_pic = models.ImageField('images/',null=True)
    a_proof = models.ImageField('images/',null=True)
    dofficer_id= models.ForeignKey(Districtofficer,on_delete=models.CASCADE)
    a_licenseno =models.CharField(max_length=100,null=True)
    a_contact =models.CharField(max_length=100,null=True)
    a_email =models.CharField(max_length=100,null=True)
    place_id = models.ForeignKey(Place,on_delete=models.CASCADE)
    a_username =models.CharField(max_length=100,null=True)
    a_password =models.CharField(max_length=100,null=True)
    a_confirmpsw=models.CharField(max_length=100,null=True)
    a_status   =models.CharField(max_length=100,null=True)

class tbl_userfood(models.Model):
    foodtype_id=models.ForeignKey(foodtype,on_delete=models.CASCADE)
    food_pic =models.ImageField('images/',null=True)
    food_name =  models.CharField(max_length=100,null=True)
    food_description = models.CharField(max_length=200,null=True)
    dofficer_id =models.ForeignKey(Districtofficer,on_delete=models.CASCADE)
    status = models.CharField(max_length=200,null=True)

class tbl_pwomenfood(models.Model):
    foodtype_id=models.ForeignKey(foodtype,on_delete=models.CASCADE)
    food_pic =models.ImageField('images/',null=True)
    pfood_amt =  models.CharField(max_length=100,null=True)
    pfood_duration =  models.CharField(max_length=100,null=True)
    pfood_name =  models.CharField(max_length=100,null=True)
    food_description = models.CharField(max_length=200,null=True)
    dofficer_id =models.ForeignKey(Districtofficer,on_delete=models.CASCADE)

class tbl_userfoodservice(models.Model):
    anganwadi_id = models.ForeignKey(anganawadi,on_delete=models.CASCADE)
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    food_qty = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    start_date = models.DateField(max_length=100,null=True)
    end_date = models.DateField(max_length=100,null=True)
    active_status = models.CharField(max_length=100,null=True)
    upload_date = models.DateField(auto_now_add=True, blank=True)

class tbl_foodstock(models.Model):
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    food_stock = models.IntegerField(null=True)
    foodstock_date = models.DateField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class tbl_totalfoodstock(models.Model):
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_totalStock = models.IntegerField(null=True)

class tbl_foodstockrequest(models.Model):
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    fsrequest_date = models.DateField(auto_now_add=True, blank=True)
    user = models.ForeignKey(anganawadi,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    f_status = models.CharField(max_length=100,null=True)
    dofficer_id = models.ForeignKey(Districtofficer,on_delete=models.CASCADE,null=True)



class tbl_pwomenfoodservice(models.Model):
    anganwadi_id = models.ForeignKey(anganawadi,on_delete=models.CASCADE)
    food_id = models.ForeignKey(tbl_pwomenfood,on_delete=models.CASCADE)
    food_qty = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    start_date = models.DateField(max_length=100,null=True)
    end_date = models.DateField(max_length=100,null=True)
    active_status = models.CharField(max_length=100,null=True)
    upload_date = models.DateField(auto_now_add=True, blank=True)



class tbl_pfoodstock(models.Model):
    pfood_id = models.ForeignKey(tbl_pwomenfood,on_delete=models.CASCADE)
    pfood_stock = models.IntegerField(null=True)
    pfoodstock_date = models.DateField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class tbl_totalpfoodstock(models.Model):
    pfood_id = models.ForeignKey(tbl_pwomenfood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pfood_totalStock = models.IntegerField(max_length=100,null=True)


class tbl_pfoodstockrequest(models.Model):
    food_id = models.ForeignKey(tbl_pwomenfood,on_delete=models.CASCADE)
    fsrequest_date = models.DateField(auto_now_add=True, blank=True)
    user = models.ForeignKey(anganawadi,on_delete=models.CASCADE)
    pquantity = models.IntegerField(null=True)
    f_status = models.CharField(max_length=100,null=True)
    dofficer_id = models.ForeignKey(Districtofficer,on_delete=models.CASCADE,null=True)



class child(models.Model):
    child_id = models.ForeignKey(User,on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100,null=True)

class tbl_child(models.Model):
    child_id = models.ForeignKey(User,on_delete=models.CASCADE)
    child_name = models.CharField(max_length=100,null=True)
    child_age = models.CharField(max_length=100,null=True)
    child_image = models.ImageField('images/',null=True)
    child_fathername = models.CharField(max_length=100,null=True)
    child_mothername = models.CharField(max_length=100,null=True)
    child_gender = models.CharField(max_length=100,null=True)
    a_id = models.ForeignKey(anganawadi,on_delete=models.CASCADE)
    place_id = models.ForeignKey(Place,on_delete=models.CASCADE)
    child_status = models.CharField(max_length=100,null=True)
    birthcertificate =  models.ImageField('images/',null=True)
    location_id = models.ForeignKey(Location,on_delete=models.CASCADE)
    child_hname = models.CharField(max_length=100,null=True)
    child_street =  models.CharField(max_length=100,null=True)
    child_pin    = models.CharField(max_length=100,null=True)
    child_contact =models.CharField(max_length=100,null=True)

class tbl_childfoodstockrequest(models.Model):
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    fsrequest_date = models.DateField(auto_now_add=True, blank=True)
    user = models.ForeignKey(anganawadi,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    f_status = models.CharField(max_length=100,null=True)
    dofficer_id = models.ForeignKey(Districtofficer,on_delete=models.CASCADE,null=True)

class tbl_childfoodstock(models.Model):
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    food_stock = models.IntegerField(null=True)
    foodstock_date = models.DateField(max_length=100,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class tbl_totalchildfoodstock(models.Model):
    food_id = models.ForeignKey(tbl_userfood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_totalStock = models.IntegerField(max_length=100,null=True)

class tbl_healthtips(models.Model):
    tips_title = models.CharField(max_length=100,null=True)
    tips_description =models.CharField(max_length=300,null=True)
    a_id = models.ForeignKey(anganawadi,on_delete=models.CASCADE)

class tbl_user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=300,null=True)
    user_contact = models.CharField(max_length=300,null=True)
    user_email = models.CharField(max_length=300,null=True)
    user_username = models.CharField(max_length=300,null=True)
    user_password = models.CharField(max_length=300,null=True)
    usser_confirm = models.CharField(max_length=300,null=True)
    place_id      = models.ForeignKey(Place,on_delete=models.CASCADE ,null=True)
    location_id   = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    user_housename = models.CharField(max_length=300,null=True)
    user_street    = models.CharField(max_length=300,null=True)
    user_pincode   = models.CharField(max_length=300,null=True)
    user_certificate = models.ImageField('images/',null=True)
    user_age         = models.CharField(max_length=300,null=True)
    user_status      = models.CharField(max_length=300,null=True)

class tbl_pwomens(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pwomen_name = models.CharField(max_length=300,null=True)
    pwomen_husbandname = models.CharField(max_length=300,null=True)
    pwomen_contact = models.CharField(max_length=300,null=True)
    pwomen_medicalproof = models.ImageField('images/',null=True)
    pwomen_photo  = models.ImageField('images/',null=True)
    pwomen_email = models.CharField(max_length=300,null=True)
    pwomen_isactive = models.CharField(max_length=300,null=True)
    pwomen_username = models.CharField(max_length=300,null=True)
    pwomen_pincode = models.CharField(max_length=300,null=True)
    pwomen_password = models.CharField(max_length=300,null=True)
    pwomen_confirmpassword = models.CharField(max_length=300,null=True)
    place_id = models.ForeignKey(Place,on_delete=models.CASCADE,null=True)
    location_id = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    p_street  = models.CharField(max_length=300,null=True)
    pwomen_age         = models.CharField(max_length=300,null=True)
    pwomen_house        = models.CharField(max_length=300,null=True)

class tbl_complaint(models.Model):
    complainttype_id =  models.ForeignKey(complainttype,on_delete=models.CASCADE,null=True)
    complaint        = models.CharField(max_length=300,null=True)
    complaint_date   = models.DateField(auto_now_add=True, blank=True)
    complaint_reply  = models.CharField(max_length=300,null=True)
    complaint_status = models.CharField(max_length=300,null=True)
    user_id          = models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    pwomen_id        = models.ForeignKey(tbl_pwomens,on_delete=models.CASCADE,null=True)
    usertype= models.CharField(max_length=300,null=True)


class tbl_feedback(models.Model):
    feedback_date = models.DateField(auto_now_add=True, blank=True)
    feedback  = models.CharField(max_length=300,null=True)
    usertype= models.CharField(max_length=300,null=True)
    user_id = models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    pwomen_id = models.ForeignKey(tbl_pwomens,on_delete=models.CASCADE,null=True)

class tbl_foodbooking(models.Model):
    foodbooking_date =  models.DateField(auto_now_add=True, blank=True)
    foodbooking_status = models.CharField(max_length=300,null=True)
    user_id =            models.ForeignKey(User,on_delete=models.CASCADE)
    userfoodservice_id =models.ForeignKey(tbl_userfoodservice,on_delete=models.CASCADE,null=True)
    Anganwadi =models.ForeignKey(anganawadi,on_delete=models.CASCADE,null=True)


class tbl_pfoodbooking(models.Model):
    pfoodbooking_date =  models.DateField(auto_now_add=True, blank=True)
    pfoodbooking_status = models.CharField(max_length=300,null=True)
    pwomen_id =            models.ForeignKey(User,on_delete=models.CASCADE)
    pwomenfoodservice_id =models.ForeignKey(tbl_pwomenfoodservice,on_delete=models.CASCADE,null=True)
    Anganwadi =models.ForeignKey(anganawadi,on_delete=models.CASCADE,null=True)