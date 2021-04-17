from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def course_list(request):
    
    # user and group detail
    current_user = request.user
    gr_id = current_user.group_id
    group_courses = gr_id.course_set.all()
    l = len(group_courses)
    
    context = {'current':current_user, 'gr_id':gr_id, 'group_courses':group_courses, 'l':l}
    return render(request, "materials/course_list_handout.html", context)

@login_required(login_url="/accounts/login/")
def handouts(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    CU = course.objects.get(id=id)
    Hd = CU.handout_set.all()
    l= len(Hd)

    context = {'current':current_user, 'gr_id':gr_id, 'CU':CU, 'Hd':Hd, 'l':l}
    return render(request, "materials/handouts.html", context)

@login_required(login_url="/accounts/login/")
def books(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    CU = course.objects.get(id=id)
    bk = CU.book_set.all()
    l = len(bk)

    context = {'current':current_user, 'gr_id':gr_id, 'CU':CU, 'Book':bk, 'l':l}
    return render(request, "materials/books.html", context)

@login_required(login_url="/accounts/login/")
def syllabos(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    CU = course.objects.get(id=id)
    sl = CU.syllabus_set.all()
    l = len(sl)

    context = {'current': current_user, 'gr_id': gr_id, 'syllabus':sl, 'l':l}
    return render (request, "materials/syllabus.html", context)

@login_required(login_url="/accounts/login/")
def past_Questions(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    CU = course.objects.get(id=id)
    pq = CU.past_question_set.all()
    l = len(pq)

    context = {'current': current_user, 'gr_id': gr_id, 'past_questions':pq, 'l':l}
    return render (request, "materials/past_question.html", context)