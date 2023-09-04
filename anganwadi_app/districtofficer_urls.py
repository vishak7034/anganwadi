from django.urls import path

from anganwadi_app.districtofficer_views import Index, view_profile, edit_profile, accepted_anganawadi, \
    reject_anganawadi, add_anganawadi, anganawadi_district, selected_place, add_userfood, add_prengantFood, \
    remove_userfood, remove_pregnantfood, user_food_request_pending, user_food_request_Accepted, \
    user_food_request_Reject, pregnant_food_request_pending, pregnant_food_request_Accepted, \
    pregnant_food_request_Reject, Remove_anganawadi, Accept_anganawadi, user_request_accept, user_request_reject, \
    pregnant_request_accept, pregnant_request_reject, child_food_request_pending, child_food_request_Accepted, \
    child_food_request_Reject, child_request_accept, child_request_reject

urlpatterns = [

    path('',Index.as_view()),
    path('viewprofile',view_profile.as_view()),
    path('edit_profile',edit_profile.as_view()),
    path('accepted_anganawadi',accepted_anganawadi.as_view()),
    path('reject_anganawadi',reject_anganawadi.as_view()),
    path('add_anganawadi',add_anganawadi.as_view()),
    path('anganawadi_district',anganawadi_district.as_view()),
    path('selected_place',selected_place.as_view()),
    path('add_userfood',add_userfood.as_view()),
    path('add_prengantFood',add_prengantFood.as_view()),
    path('remove_userfood',remove_userfood.as_view()),
    path('remove_pregnantfood',remove_pregnantfood.as_view()),
    path('user_food_request_pending',user_food_request_pending.as_view()),
    path('user_food_request_Accepted',user_food_request_Accepted.as_view()),
    path('user_food_request_Reject',user_food_request_Reject.as_view()),
    path('pregnant_food_request_pending',pregnant_food_request_pending.as_view()),
    path('pregnant_food_request_Accepted',pregnant_food_request_Accepted.as_view()),
    path('pregnant_food_request_Reject',pregnant_food_request_Reject.as_view()),
    path('Remove_anganawadi',Remove_anganawadi.as_view()),
    path('Accept_anganawadi',Accept_anganawadi.as_view()),
    path('user_request_accept',user_request_accept.as_view()),
    path('user_request_reject',user_request_reject.as_view()),
    path('pregnant_request_accept',pregnant_request_accept.as_view()),
    path('pregnant_request_reject',pregnant_request_reject.as_view()),
    path('child_food_request_pending',child_food_request_pending.as_view()),
    path('child_food_request_Accepted',child_food_request_Accepted.as_view()),
    path('child_food_request_Reject',child_food_request_Reject.as_view()),
    path('child_request_accept',child_request_accept.as_view()),
    path('child_request_reject',child_request_reject.as_view()),





]
def urls():
    return urlpatterns, 'districtofficer', 'districtofficer'