from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='dashboard'),
    path('lecture_update/', views.lecturee_update, name="lecture_update"),
    path('upcoming_tests/', views.upcomingg_test, name="upcoming_test"),
    path('pending_assignment/', views.pendingg_assignment,
         name="pending_assignment"),
    path('important_information/', views.importangt_information,
         name="important_information"),

    path('lecture_update/add', views.add_lecture_update,
         name="add_lecture_update"),
    path('pending_assignment/add', views.add_pendingAssignment,
         name="add_pending_assignment"),
    path('upcoming_test/add', views.add_upcomingTest, name="add_upcoming_test"),
    path('important_information/add', views.add_important_information,
         name="add_important_information"),

    path('edit_lecture_update/<str:id>', views.edit_lecture_update, name="edit_lecture_update"),
    path('edit_pending_assignment/<str:id>', views.edit_pending_assignment, name="edit_pending_assignment"),
    path('edit_upcoming_test/<str:id>', views.edit_upcoming_test, name="edit_upcoming_test"),
    path('edit_important_information/<str:id>', views.edit_important_information, name="edit_important_information"),

    path('delete_lecture_update/<str:id>', views.delete_lecture_update, name="delete_lecture_update"),
    path('delete_pending_assignment/<str:id>', views.delete_pending_assignment, name="delete_pending_assignment"),
    path('delete_upcoming_test/<str:id>', views.delete_upcoming_test, name ="delete_upcoming_test"),
    path('delete_important_information/<str:id>', views.delete_important_information, name="delete_important_information")
]
