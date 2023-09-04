from  django.urls import path

from anganwadi_app.user_views import  IndexView, profile, edit_profile, AnganwadiServices, viewFoods, ViewHealthTips, \
    ViewAnganwadils, ViewDistrictOfficer, ViewFoodStock, myrequest, complaint, feedback, removecomplaint, removefeedback, \
     accept_requests

urlpatterns = [
    path('',IndexView.as_view()),
    path('profile',profile.as_view()),
    path('edit_profile',edit_profile.as_view()),
    path('AnganwadiServices',AnganwadiServices.as_view()),
    path('viewFoods',viewFoods.as_view()),
    path('ViewHealthTips',ViewHealthTips.as_view()),
    path('ViewAnganwadils',ViewAnganwadils.as_view()),
    path('ViewDistrictOfficer',ViewDistrictOfficer.as_view()),
    path('ViewFoodStock',ViewFoodStock.as_view()),
    path('myrequest',myrequest.as_view()),
    path('complaint',complaint.as_view()),
    path('feedback',feedback.as_view()),
    path('removecomplaint',removecomplaint.as_view()),
    path('removefeedback',removefeedback.as_view()),

    path('accept_requests',accept_requests.as_view())



]
def urls():
    return urlpatterns, 'user', 'user'