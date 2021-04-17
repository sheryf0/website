from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import lecture_updateAdd, Add_pending_assignment, Add_upcoming_test, Add_important_information
from .models import *

# will check later

'''the page here is just my main notificaation page its here to help just to show a quick notfication about the user his department and his first 
lecture update with other important stuffs its like the main map that will be linking users to the  main page to check important fields like lecture
updates ....pending assignments etc '''


@login_required(login_url="/accounts/login/")
def main(request):
    # this is here to form a context of anything related to user
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update
    lecture_update = gr_id.lecture_update_set.all().order_by('time_start')

    lecture_number = len(
        lecture_update)
    if lecture_number:
        first_lecture_update = lecture_update[0]
    else:
        first_lecture_update = "your course rep hasn't updated any lecture update in the group"

    # this is here to form a context of anything related to pending assignments
    pending_assignment = gr_id.pending_assignment_set.all().order_by('assignment_dueDate')

    assignment_number = len(
        pending_assignment)
    if assignment_number:
        latest_assigment = pending_assignment[0]
    else:
        latest_assigment = "your course rep hasn't updated any assignment in the group"

    # this is here to form a context of anything related to upcoming test
    upcoming_test = gr_id.upcoming_test_set.all().order_by('test_time')

    test_number = len(
        upcoming_test)
    if test_number:
        latest_test = upcoming_test[0]
    else:
        latest_test = "your course rep hasnt updated any test in the group"

    # this is here to form a context of anything related to important information
    important_information = gr_id.important_information_set.all()

    information_number = len(
        important_information)
    if information_number:
        latest_information = important_information[0]
    else:
        latest_information = "your course rep hasn't updated information in the group yet"

    context = {'current': current_user, 'gr_id': gr_id,
               'LU': lecture_update, 'FLU': first_lecture_update, 'LN': lecture_number,
               'PA': pending_assignment, 'AN': assignment_number, 'LA': latest_assigment,
               'UT': upcoming_test, 'TN': test_number, 'LT': latest_test,
               'II': important_information, 'IN': information_number, 'LI': latest_information
               }
    return render(request, "dashboard/main.html", context)


# this should just be here to check for lecture update
@login_required(login_url="/accounts/login")
def lecturee_update(request):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update
    lecture_update = gr_id.lecture_update_set.all().order_by('time_start')

    lecture_number = len(
        lecture_update)
    if lecture_number:
        first_lecture_update = lecture_update[0]
    else:
        first_lecture_update = "your course rep hasn't updated any lecture update in the group"

    context = {'current': current_user, 'gr_id': gr_id,
               'LU': lecture_update, 'FLU': first_lecture_update, 'LN': lecture_number,

               }
    return render(request, "dashboard/lecture_update.html", context)


@login_required(login_url="/accounts/login")
def upcomingg_test(request):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to upcoming test
    upcoming_test = gr_id.upcoming_test_set.all().order_by('test_time')

    test_number = len(
        upcoming_test)
    if test_number:
        latest_test = upcoming_test[0]
    else:
        latest_test = "your course rep hasnt updated any test in the group"

    context = {'current': current_user, 'gr_id': gr_id,

               'UT': upcoming_test, 'TN': test_number, 'LT': latest_test,

               }
    return render(request, "dashboard/upcoming_test.html", context)


@login_required(login_url="/accounts/login")
def pendingg_assignment(request):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update

    # this is here to form a context of anything related to pending assignments
    pending_assignment = gr_id.pending_assignment_set.all().order_by('assignment_dueDate')

    assignment_number = len(
        pending_assignment)
    if assignment_number:
        latest_assigment = pending_assignment[0]
    else:
        latest_assigment = "your course rep hasn't updated any assignment in the group"

    # this is here to form a context of anything related to upcoming test

    context = {'current': current_user, 'gr_id': gr_id,

               'PA': pending_assignment, 'AN': assignment_number, 'LA': latest_assigment,

               }
    return render(request, "dashboard/pending_assignment.html", context)


@login_required(login_url="/accounts/login")
def importangt_information(request):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update
    # this is here to form a context of anything related to important information
    important_information = gr_id.important_information_set.all().order_by('-date_posted')

    information_number = len(
        important_information)
    if information_number:
        latest_information = important_information[0]
        print(important_information[0])
    else:
        latest_information = "your course rep hasn't updated information in the group yet"

    context = {'current': current_user, 'gr_id': gr_id,
               'II': important_information, 'IN': information_number, 'LI': latest_information
               }
    return render(request, "dashboard/important_information.html", context)


@login_required(login_url="/accounts/login")
def add_lecture_update(request):

    form = lecture_updateAdd()
    if request.method == "POST":
        form = lecture_updateAdd(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('dashboard')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/add_lecture_update.html", context)


@login_required(login_url="/accounts/login")
def add_pendingAssignment(request):

    form = Add_pending_assignment()
    if request.method == "POST":
        form = Add_pending_assignment(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('pending_assignment')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/add_pending_assignment.html", context)


@login_required(login_url="/accounts/login")
def add_upcomingTest(request):

    form = Add_upcoming_test()
    if request.method == "POST":
        form = Add_upcoming_test(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('upcoming_test')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/add_upcoming_test.html", context)


@login_required(login_url="/accounts/login")
def add_important_information(request):

    form = Add_important_information()
    if request.method == "POST":
        form = Add_important_information(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('important_information')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/add_important_information.html", context)

@login_required(login_url="/accounts/login")
def edit_lecture_update(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update
    lu = lecture_update.objects.get(id=id)

    form = lecture_updateAdd(instance=lu)
    if request.method == "POST":
        form = lecture_updateAdd(request.POST, instance=lu)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('lecture_update')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/edit_lecture_update.html", context)

@login_required(login_url="/accounts/login")
def edit_pending_assignment(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update
    lu = pending_assignment.objects.get(id=id)

    form = Add_pending_assignment(instance=lu)
    if request.method == "POST":
        form = Add_pending_assignment(request.POST, instance=lu)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('pending_assignment')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/edit_lecture_update.html", context)


@login_required(login_url="/accounts/login")
def edit_upcoming_test(request, id):
    current_user = request.user
    gr_id = current_user.group_id

    # this is here to form a context of anything related to lecture update
    lu = upcoming_test.objects.get(id=id)

    form = Add_upcoming_test(instance=lu)
    if request.method == "POST":
        form = Add_upcoming_test(request.POST, instance=lu)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('upcoming_test')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/edit_upcoming_test.html", context)

@login_required(login_url="/accounts/login")
def edit_important_information(request, id):
    
    lu = important_information.objects.get(id=id)

    form = Add_important_information(instance=lu)
    if request.method == "POST":
        form = Add_important_information(request.POST, instance=lu)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.group_id = request.user.group_id
            obj.author = request.user.first_name
            obj.save()
            return redirect('important_information')
    current_user = request.user
    gr_id = current_user.group_id
    context = {'form': form, 'current': current_user, 'gr_id': gr_id}
    return render(request, "dashboard/edit_important_information.html", context)


def delete_lecture_update(request, id):
    lU = lecture_update.objects.get(id=id)
    if request.method=="POST":
        lU.delete()
        return redirect('lecture_update')

    current_user = request.user
    gr_id = current_user.group_id

    context ={'lU':lU, 'current':current_user, 'gr_id':gr_id}
    return render(request, "dashboard/delete_lecture_update.html", context)

def delete_pending_assignment(request, id):
    li = pending_assignment.objects.get(id=id)
    if request.method=="POST":
        li.delete()
        return redirect('pending_assignment')

    current_user = request.user
    gr_id = current_user.group_id

    context ={'lU':li, 'current':current_user, 'gr_id':gr_id}
    return render(request, "dashboard/delete_pending_assignment.html", context)

def delete_upcoming_test(request, id):
    li = upcoming_test.objects.get(id=id)
    if request.method=="POST":
        li.delete()
        return redirect('upcoming_test')

    current_user = request.user
    gr_id = current_user.group_id

    context ={'lU':li, 'current':current_user, 'gr_id':gr_id}
    return render(request, "dashboard/delete_upcoming_test.html", context)


def delete_important_information(request, id):
    li = important_information.objects.get(id=id)
    if request.method=="POST":
        li.delete()
        return redirect('important_information')

    current_user = request.user
    gr_id = current_user.group_id

    context ={'lU':li, 'current':current_user, 'gr_id':gr_id}
    return render(request, "dashboard/delete_important_information.html", context)