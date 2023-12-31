from django.urls import path
from . import views


urlpatterns = [
    path('ngo/',views.ngo_views, name='ngo'),
    path('ngo/list/', views.ngo_list_views, name='ngo_list'),
    path('ngo/<int:id>/delete/', views.ngo_delete_views, name='ngo_delete'),
    path('ngo/register/', views.ngo_register_views, name='ngo_reg'),
    path('ngo/forget/', views.ngo_forget_pass_views, name='ngo_forget_password'),
    path('ngo/table/', views.ngo_table_views, name='ngo_table'),
    path('ngo/<int:id>/edit/',views.ngo_edit_views, name='ngo_edit'),

    path('volunteer/<int:id>/edit/',views.volunteer_edit_views, name='volunteer_edit'),
    path('volunteer/list/',views.volunteer_list_views, name='volunteer_list'),
    path('volunteer/ngo/list/',views.volunteer_ngo_list_views, name='volunteer_ngo_list'),
    path('volunteer/<int:id>/delete/', views.volunteer_delete_views, name='delete_volunteer'),
    path('volunteer/register/', views.volunteer_register_views, name='volunteer_reg'),
    path('volunteer/forget/', views.volunteer_forget_pass_views, name='volunteer_forget_password'),
    path('volunteer/table/', views.volunteer_table_views, name='volunteer_table'),
    path('donator/table/', views.donor_table_views, name='donor_table'),
    path('volunteer/', views.volunteer_views, name='volunteer'),

    path('donator/ngo/list/', views.donator_ngo_list_views, name='donor_ngo_list'),
    path('donator/list/', views.donator_list_views, name='donor_list'),
    path('donator/forget/', views.donator_forget_pass_views, name='donator_forget_password'),
    path('donator/register/', views.donator_register_views, name='donator_reg'),
    path('donator/', views.donator_views, name='donator'),
    path('donor/<int:id>/delete/', views.donor_delete_views, name='donor_delete'),
    path('donor/<int:id>/edit/',views.donor_edit_views, name='donor_edit'),

    path('staff/', views.staff_views, name='staff'),
    path('staff/forget/', views.staff_forget_pass_views, name='staff_forget_password'),
    path('staff/register/', views.staff_register_views, name='staff_reg'),
    path('staff/list/', views.staff_list_views, name='staff_list'),
    path('staff/ngo/list/', views.staff_ngo_list_views, name='staff_ngo_list'),
    path('staff/<int:id>/delete/', views.staff_delete_views, name='staff_delete'),
    path('staff/table/', views.staff_table_views, name='staff_table'),
    path('staff/<int:id>/edit/',views.staff_edit_views, name='staff_edit'),

    path('event/add/', views.event_add_views, name='event_add'),
    path('event/ngo/', views.event_ngo_views, name='event_ngo'),
    path('event/',views.event_views, name='event'),
    path('event/<int:id>/edit/',views.event_edit_views, name='event_edit'),

    path('donation/ngo/', views.donation_ngo_views, name='donation_ngo'),
    path('donation/add/', views.donation_add_views, name='donation_add'),
    path('donation/<int:id>/edit/', views.donation_edit_views, name='donation_edit'),
    path('donation/<int:id>/delete/', views.donation_delete_views, name='donation_delete'),
    path('donation/',views.donation_views, name='donation'),

    path('project/<int:id>/delete/', views.project_delete_views, name='project_delete'),
    path('project/ngo/',views.project_ngo_views, name='project_ngo'),
    path('project/',views.project_views, name='project'),
    path('project/<int:id>/edit/',views.project_edit_views, name='project_edit'),
    path('project/add/',views.project_add_views, name='project_add'),

    path('home/',views.home_views, name='home'),
    path('',views.home_views, name='home'),
    path('code/',views.code_views, name='code'),
    path('reset/',views.reset_views, name='reset'),
    path('logout/',views.logout_views, name='logout'),

]

