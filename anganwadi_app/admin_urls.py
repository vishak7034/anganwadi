from django.urls import path

from anganwadi_app.admin_views import IndexView, indexViews, addfood_type, addproof_type, addcomplaint_type, \
    remove_foodtype, edit_foodtype, remove_complainttype, edit_complainttype, remove_prooftype, edit_prooftype, \
    add_district, remove_district, add_place, remove_place, add_location, remove_location, add_districtofficers, \
    officers_district, selected_place, view_districtofficers, Delete_districtofficers, view_user_feedback, \
    view_pregnant_feedback, user_complaints, pregnant_complaints, curent_report, pregnant_complaint_reply, \
    user_complaint_reply, user_report, pregnant_report, child_report

urlpatterns = [

    path('',IndexView.as_view()),
    path('index',indexViews.as_view()),
    path('addfoodtype',addfood_type.as_view()),
    path('addprooftype',addproof_type.as_view()),
    path('addcomplainttype',addcomplaint_type.as_view()),
    path('remove_foodtype',remove_foodtype.as_view()),
    path('edit_foodtype',edit_foodtype.as_view()),
    path('remove_complainttype',remove_complainttype.as_view()),
    path('edit_complainttype',edit_complainttype.as_view()),
    path('remove_prooftype',remove_prooftype.as_view()),
    path('edit_prooftype',edit_prooftype.as_view()),
    path('add_district',add_district.as_view()),
    path('remove_district',remove_district.as_view()),
    path('add_place',add_place.as_view()),
    path('remove_place',remove_place.as_view()),
    path('add_location',add_location.as_view()),
    path('remove_location',remove_location.as_view()),
    path('add_districtofficers',add_districtofficers.as_view()),
    path('officers_district',officers_district.as_view()),
    path('selected_place',selected_place.as_view()),
    path('view_districtofficers',view_districtofficers.as_view()),
    path('Delete_districtofficers',Delete_districtofficers.as_view()),
    path('view_user_feedback',view_user_feedback.as_view()),
    path('view_pregnant_feedback',view_pregnant_feedback.as_view()),
    path('user_complaints',user_complaints.as_view()),
    path('pregnant_complaints',pregnant_complaints.as_view()),
    path('curent_report',curent_report.as_view()),
    path('pregnant_complaint_reply',pregnant_complaint_reply.as_view()),
    path('user_complaint_reply',user_complaint_reply.as_view()),
    path('user_report',user_report.as_view()),
    path('pregnant_report',pregnant_report.as_view()),
    path('child_report',child_report.as_view()),




]
def urls():
    return urlpatterns, 'admin', 'admin'