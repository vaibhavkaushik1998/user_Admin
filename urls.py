from django.urls import path
from user.views import ResUserRegistrationAPI, ResAdminAPI

urlpatterns = [
    # User API Endpoints
    path('user/registration/', ResUserRegistrationAPI.as_view(), name='user_registration_api'),  # POST for user registration
    path('user/update/<int:id>/', ResUserRegistrationAPI.as_view(), name='user_update_api'),  # PUT for updating a user
    path('user/delete/<int:id>/', ResUserRegistrationAPI.as_view(), name='user_delete_api'),  # DELETE for deleting a user
    path('user/list/', ResUserRegistrationAPI.as_view(), name='user_list_api'),  # GET for all users
    path('user/detail/<int:id>/', ResUserRegistrationAPI.as_view(), name='user_detail_api'),  # GET for single user

    # Admin API Endpoints
    path('resadmin/registration/', ResAdminAPI.as_view(), name='admin_registration_api'),  # POST for admin registration
    path('resadmin/update/<int:id>/', ResAdminAPI.as_view(), name='admin_update_api'),  # PUT for updating an admin
    path('resadmin/delete/<int:id>/', ResAdminAPI.as_view(), name='admin_delete_api'),  # DELETE for deleting an admin
    path('resadmin/list/', ResAdminAPI.as_view(), name='admin_list_api'),  # GET for all admins
    path('resadmin/detail/<int:id>/', ResAdminAPI.as_view(), name='admin_detail_api'),  # GET for single admin
]

# from django.urls import path
# from user.views import ResUserRegistrationAPI, ResAdminAPI

# urlpatterns = [
#     # Customer API Endpoints
#     path('registration/api/', ResUserRegistrationAPI.as_view(), name='user_registration_api'),  # POST for registration
#     path('change/api/<int:id>/', ResUserRegistrationAPI.as_view(), name='user_update_api'),  # PUT for updating user
#     path('userdelete/api/<int:id>/', ResUserRegistrationAPI.as_view(), name='user_delete_api'),  # DELETE for deleting user
#     path('get/api/', ResUserRegistrationAPI.as_view(), name='user_list_api'),  # GET for all users
#     path('get/api/<int:id>/', ResUserRegistrationAPI.as_view(), name='user_detail_api'),  # GET for single user

#     # Admin API Endpoints
#     path('resadmin/api/', ResAdminAPI.as_view(), name='admin_registration_api'),  # POST for admin registration
#     path('changeadmin/api/<int:id>/', ResAdminAPI.as_view(), name='admin_update_api'),  # PUT for updating admin
#     path('admindelete/api/<int:id>/', ResAdminAPI.as_view(), name='admin_delete_api'),  # DELETE for deleting admin
#     path('adminget/api/', ResAdminAPI.as_view(), name='admin_list_api'),  # GET for all admins
#     path('adminget/api/<int:id>/', ResAdminAPI.as_view(), name='admin_detail_api'),  # GET for single admin
# ]
