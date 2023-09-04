from django.urls import path

from anganwadi_app.anganwadi_views import IndexView, view_profile, edit_profile, user_foodServices, typeof_food, \
    user_foodServices_remove, ViewUserBooking_food, user_FoodStockMasterDetails, user_chartStockMasterDetails, \
    user_AddFoodStock, typeof_food_stock, remove_user_foodstock, anganwadi_send_foodrquest, type_food_userrequest, \
    Remove_type_food_userrequest, user_acceptedfoodbooking, view_userfood_report, pregnantfoodServices, \
     pregnant_foodServices_remove, ViewPregnantBooking_food, pregnant_FoodStockMasterDetails, \
    pregnant_chartStockMasterDetails, Pregnant_AddFoodStock, typeof_pregnant_food_stock, remove_pregnant_foodstock, \
    anganwadi_pregnant_send_foodrquest, type_food_preganant, food_type_preganant_request, \
    Remove_pregnantfood_userrequest, pregnant_acceptedfoodbooking, view_pregnantfood_report, add_child, child_district, \
    selected_child_place, AcceptedListChild, RejectedListChild, child_remove, child_accept, healthtips, remove_healthtip, \
    ActiveUserList, AcceptedListUser, RejectedListUse, ViewPwomenlist, ActiveListPwomen, RejectedListPwomen, \
    approve_users, reject_users, approve_pregnant, reject_pregnant, approve_users_foodrequest, \
    approve_pregnant_foodrequest, user_provide_food, pregnant_complete_foodrequest, child_FoodStockMasterDetails, \
    child_chartStockMasterDetails, child_AddFoodStock, child_SendRequest, child_foodreport, typeof_child_food_stock, \
    remove_child_foodstock, type_food_childrrequest, Remove_type_food_childrrequest

urlpatterns = [
    path('',IndexView.as_view()),
    path('view_profile',view_profile.as_view()),
    path('edit_profile',edit_profile.as_view()),
    path('user_foodServices',user_foodServices.as_view()),
    path('typeof_food',typeof_food.as_view()),
    path('user_foodServices_remove',user_foodServices_remove.as_view()),
    path('ViewUserBooking_food',ViewUserBooking_food.as_view()),
    path('user_FoodStockMasterDetails',user_FoodStockMasterDetails.as_view()),
    path('user_chartStockMasterDetails',user_chartStockMasterDetails.as_view()),
    path('user_AddFoodStock',user_AddFoodStock.as_view()),
    path('typeof_food_stock',typeof_food_stock.as_view()),
    path('remove_user_foodstock',remove_user_foodstock.as_view()),
    path('anganwadi_send_foodrquest',anganwadi_send_foodrquest.as_view()),
    path('type_food_userrequest',type_food_userrequest.as_view()),
    path('Remove_type_food_userrequest',Remove_type_food_userrequest.as_view()),
    path('user_acceptedfoodbooking',user_acceptedfoodbooking.as_view()),
    path('view_userfood_report',view_userfood_report.as_view()),
    path('pregnantfoodServices',pregnantfoodServices.as_view()),
    path('type_food_preganantrequest',type_food_preganant.as_view()),
    path('pregnant_foodServices_remove',pregnant_foodServices_remove.as_view()),
    path('ViewPregnantBooking_food',ViewPregnantBooking_food.as_view()),
    path('pregnant_FoodStockMasterDetails',pregnant_FoodStockMasterDetails.as_view()),
    path('pregnant_chartStockMasterDetails',pregnant_chartStockMasterDetails.as_view()),
    path('Pregnant_AddFoodStock',Pregnant_AddFoodStock.as_view()),
    path('typeof_pregnant_food_stock',typeof_pregnant_food_stock.as_view()),
    path('remove_pregnant_foodstock',remove_pregnant_foodstock.as_view()),
    path('anganwadi_pregnant_send_foodrquest',anganwadi_pregnant_send_foodrquest.as_view()),
    path('food_type_preganant_request',food_type_preganant_request.as_view()),
    path('Remove_pregnantfood_userrequest',Remove_pregnantfood_userrequest.as_view()),
    path('pregnant_acceptedfoodbooking',pregnant_acceptedfoodbooking.as_view()),
    path('view_pregnantfood_report',view_pregnantfood_report.as_view()),
    path('add_child',add_child.as_view()),
    path('child_district',child_district.as_view()),
    path('selected_child_place',selected_child_place.as_view()),
    path('AcceptedListChild',AcceptedListChild.as_view()),
    path('RejectedListChild',RejectedListChild.as_view()),
    path('child_remove',child_remove.as_view()),
    path('child_accept',child_accept.as_view()),
    path('healthtips',healthtips.as_view()),
    path('remove_healthtip',remove_healthtip.as_view()),
    path('ActiveUserList',ActiveUserList.as_view()),
    path('AcceptedListUser',AcceptedListUser.as_view()),
    path('RejectedListUse',RejectedListUse.as_view()),
    path('ViewPwomenlist',ViewPwomenlist.as_view()),
    path('ActiveListPwomen',ActiveListPwomen.as_view()),
    path('RejectedListPwomen',RejectedListPwomen.as_view()),
    path('approve_users',approve_users.as_view()),
    path('reject_users',reject_users.as_view()),
    path('approve_pregnant',approve_pregnant.as_view()),
    path('reject_pregnant',reject_pregnant.as_view()),
    path('approve_users_foodrequest',approve_users_foodrequest.as_view()),
    path('approve_pregnant_foodrequest',approve_pregnant_foodrequest.as_view()),
    path('user_provide_food',user_provide_food.as_view()),
    path('pregnant_complete_foodrequest',pregnant_complete_foodrequest.as_view()),
    path('child_FoodStockMasterDetails',child_FoodStockMasterDetails.as_view()),
    path('child_chartStockMasterDetails',child_chartStockMasterDetails.as_view()),
    path('child_AddFoodStock',child_AddFoodStock.as_view()),
    path('child_SendRequest',child_SendRequest.as_view()),
    path('child_foodreport',child_foodreport.as_view()),
    path('typeof_child_food_stock',typeof_child_food_stock.as_view()),
    path('remove_child_foodstock',remove_child_foodstock.as_view()),
    path('type_food_childrrequest',type_food_childrrequest.as_view()),
    path('Remove_type_food_childrrequest',Remove_type_food_childrrequest.as_view())

]
def urls():
    return urlpatterns, 'anganwadi', 'anganwadi'