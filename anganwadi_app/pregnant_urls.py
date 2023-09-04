
from django.urls import path

from anganwadi_app.pregnant_views import IndexView, profile, edit_profile, AnganwadiServices, viewFoods, ViewHealthTips, \
    ViewDistrictOfficer, ViewAnganwadils, myrequest, ViewFoodStock, complaint, feedback, removecomplaint, removefeedback, \
     accept_foodrequestrequest

urlpatterns =[
    path('',IndexView.as_view()),
    path('profiles',profile.as_view()),
    path('edit_profiles',edit_profile.as_view()),
    path('AnganwadiServicess',AnganwadiServices.as_view()),
    path('viewFoodss',viewFoods.as_view()),
    path('ViewHealthTipss',ViewHealthTips.as_view()),
    path('ViewAnganwadilss',ViewAnganwadils.as_view()),
    path('ViewDistrictOfficers',ViewDistrictOfficer.as_view()),
    path('ViewFoodStocks',ViewFoodStock.as_view()),
    path('myrequests',myrequest.as_view()),
    path('complaints',complaint.as_view()),
    path('feedbacks',feedback.as_view()),
    path('removecomplaints',removecomplaint.as_view()),
    path('removefeedbacks',removefeedback.as_view()),
    path('accept_foodrequestrequest',accept_foodrequestrequest.as_view())

]
def urls():
    return urlpatterns, 'pregnant', 'pregnant'