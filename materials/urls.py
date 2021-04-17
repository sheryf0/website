from django.urls import path
from . import views


urlpatterns = [
    path('couse_name', views.course_list, name="course_handout"),
    path('handouts/<str:id>', views.handouts, name="handout"),
    path('past_question/<str:id>', views.past_Questions, name="past_question"),
    path('syllabus/<str:id>', views.syllabos, name="syllabus"),
    path('books/<str:id>', views.books, name="books")
]
