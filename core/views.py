from random import randrange
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import *


# Create your views here.
def logout_views(request):
    logout(request)
    return redirect('/home/')


def ngo_views(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/ngo/table/')
            else:
                context['error'] = "Please enter valid Email and Password"
        except:
            context['error'] = "Please enter valid Email and Password"

    template = loader.get_template('ngo_login.html')
    return HttpResponse(template.render(context, request))


def ngo_table_views(request):
    user = request.user
    ngo = User.objects.all().order_by('id')[:5]
    volunteer = Volunteer.objects.all().order_by('id')[:3]
    staff = Staff.objects.all().order_by('id')[:5]
    donor = Donor.objects.all().order_by('id')[:5]
    project = Project.objects.all().order_by('id')[:5]
    event = Event.objects.all().order_by('id')[:5]
    donation = Donation.objects.all().order_by('id')[:5]

    context = {
        'ngo': ngo,
        'user': user,
        'volunteer': volunteer,
        'staff': staff,
        'donor': donor,
        'project': project,
        'event': event,
        'donation': donation
    }
    template = loader.get_template('ngo_table.html')
    return HttpResponse(template.render(context, request))


def ngo_register_views(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pas1 = request.POST.get('password1')
        pas2 = request.POST.get('password2')
        last_name = request.POST.get('last_name')
        try:
            if pas1 == pas2:
                user = User(username=username, email=email, password=pas1,last_name=last_name)
                user.save()
                return redirect('/ngo/')
            else:
                context['error'] = "Please enter Matching Password"
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('ngo_register.html')
    return HttpResponse(template.render(context, request))


def ngo_edit_views(request,id):
    user = User.objects.get(id=id)
    context = {
        'ngo': user
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pas1 = request.POST.get('password1')
        last_name = request.POST.get('last_name')
        user = authenticate(request, username=username, password=pas1)
        try:
            if user is not None:
                user.username = username
                user.email = email
                user.last_name = last_name
                user.save()
                return redirect('/ngo/table/')
            else:
                context['error'] = "Please enter Matching Password"
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('ngo_edit.html')
    return HttpResponse(template.render(context, request))


def volunteer_edit_views(request, id):
    volunteer = Volunteer.objects.get(id=id)
    context = {
        'volunteer': volunteer,
        'user': volunteer.user
    }
    if request.method == 'POST':
        user_get = request.POST.get('username')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=user_get)
            volunteer.user = user
            volunteer.name = name
            volunteer.contact=contact
            volunteer.address=address
            volunteer.email=email
            volunteer.save()
            return redirect('/ngo/table/')
        except:
            context['error'] = "Please enter Right Password"
    template = loader.get_template('volunteer_edit.html')
    return HttpResponse(template.render(context, request))


def donor_edit_views(request, id):
    donor = Donor.objects.get(id=id)
    user = donor.user
    context = {
        'donor': donor,
        'user': user
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        user_get = request.POST.get('username')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=user_get)
            donor.name = name
            donor.user = user
            donor.contact = contact
            donor.address = address
            donor.email = email
            donor.save()
            return redirect('/ngo/table/')
            # else:
            #     context['error'] = "Please enter Right Password"
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('donor_edit.html')
    return HttpResponse(template.render(context, request))


def staff_edit_views(request, id):
    staff = Staff.objects.get(id=id)
    context = {
        'staff': staff
    }
    if request.method == 'POST':
        user_get = request.POST.get('username')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=user_get)
            staff.name = name
            staff.user = user
            staff.contact = contact
            staff.address = address
            staff.email = email
            staff.save()
            return redirect('/ngo/table/')
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('staff_edit.html')
    return HttpResponse(template.render(context, request))


def ngo_forget_pass_views(request):
    data_to_send = "User"
    request.session['data'] = data_to_send
    context = {
        'title': "ngo"
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = randrange(111111, 1000000)
        except:
            context['error'] = 'This Email Does"n Exist !!'
        else:
            send_mail(
                f'Your Code is:{otp} ',
                "Here is the message.",
                "chotaliyarahul68@gmail.com",
                [email],
                fail_silently=False
            )
            code = Otp(otp=otp)
            code.save()
            return redirect('/code/')
    template = loader.get_template('ngo_forget_pass.html')
    return HttpResponse(template.render(context, request))


def volunteer_views(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            volunteer = Volunteer.objects.get(password=password, email=email)
            user = User.objects.get(username=volunteer.user)

        except:
            context['error'] = "Please enter valid username and password"
        try:
            if volunteer is not None:
                login(request, user)
                return redirect('/volunteer/table/')
        except:
            context['error'] = "Please enter valid username and password"
    template = loader.get_template('volunteer_login.html')
    return HttpResponse(template.render(context, request))


def volunteer_register_views(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        volunteer_user = request.POST.get('user')
        email = request.POST.get('email')
        pas1 = request.POST.get('pas1')
        pas2 = request.POST.get('pas2')
        address = request.POST.get('address')
        user = User.objects.get(username=volunteer_user)
        try:
            if pas1 == pas2:
                user = Volunteer(contact=contact, user=user, email=email, password=pas1, address=address,name=name)
                user.save()
                return redirect('/volunteer/')
            else:
                context['error'] = "Please enter valid Email and Password"
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('volunteer_register.html')
    return HttpResponse(template.render(context, request))


def volunteer_forget_pass_views(request):
    data_to_send = "Volunteer"
    request.session['data'] = data_to_send
    context = {
        'title': "volunteer"
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = randrange(111111, 1000000)
        try:
            volunteer = Volunteer.objects.get(email=email)
        except:
            context['error'] = 'This Email Does"n Exist !!'
        else:
            send_mail(
                f'Your Code is:{otp} ',
                "Here is the message.",
                "chotaliyarahul68@gmail.com",
                [email],
                fail_silently=False
            )
            code = Otp(otp=otp)
            code.save()
            return redirect('/code/')
    template = loader.get_template('ngo_forget_pass.html')
    return HttpResponse(template.render(context, request))


def volunteer_table_views(request):
    user = request.user
    profile = Volunteer.objects.get(user=user)
    ngo = User.objects.all()
    volunteer = Volunteer.objects.all()
    staff = Staff.objects.all()
    donor = Donor.objects.all()
    project = Project.objects.all()
    event = Event.objects.all()
    donation = Donation.objects.all()
    context = {
        'ngo': ngo,
        'user': profile,
        'volunteer': volunteer,
        'staff': staff,
        'donor': donor,
        'project': project,
        'event': event,
        'donation': donation,
    }
    template = loader.get_template('Volunteer_table.html')
    return HttpResponse(template.render(context, request))


def donator_views(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            donor = Donor.objects.get(password=password, email=email)
            user = User.objects.get(username=donor.user)
            if donor is not None:
                login(request, user)
                return redirect('/donator/table/')
            else:
                context['error'] = "Please enter valid username and password"
        except:
            context['error'] = "Please enter valid username and password"

    template = loader.get_template('donator_login.html')
    return HttpResponse(template.render(context, request))


def donator_register_views(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        don_user = request.POST.get('user')
        email = request.POST.get('email')
        pas1 = request.POST.get('pas1')
        pas2 = request.POST.get('pas2')
        address = request.POST.get('address')
        userr = User.objects.get(username=don_user)
        print(userr, 'lplpplp')
        try:
            if pas1 == pas2:
                user = Donor(name=name,contact=contact, user=userr, email=email, password=pas1, address=address)
                user.save()
                return redirect('/donator/')
            else:
                context['error'] = "Please enter valid Email and Password"
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('donator_register.html')
    return HttpResponse(template.render(context, request))


def donator_forget_pass_views(request):
    data_to_send = "Donor"
    request.session['data'] = data_to_send
    context = {
        'title': "donator"
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = randrange(111111, 1000000)
        try:
            donator = Donor.objects.get(email=email)
        except:
            context['error'] = 'This Email Does"n Exist !!'
        else:
            send_mail(
                f'Your Code is:{otp} ',
                "Here is the message.",
                "chotaliyarahul68@gmail.com",
                [email],
                fail_silently=False
            )
            code = Otp(otp=otp)
            code.save()
            return redirect('/code/')
    template = loader.get_template('ngo_forget_pass.html')
    return HttpResponse(template.render(context, request))


def donor_table_views(request):
    user = request.user
    profile = Donor.objects.get(user=user)
    ngo = User.objects.all().order_by('id')[:5]
    volunteer = Volunteer.objects.all().order_by('id')[:5]
    staff = Staff.objects.all().order_by('id')[:5]
    donor = Donor.objects.all().order_by('id')[:5]
    project = Project.objects.all().order_by('id')[:5]
    event = Event.objects.all().order_by('id')[:5]
    donation = Donation.objects.all().order_by('id')[:5]
    context = {
        'ngo': ngo,
        'user': profile,
        'volunteer': volunteer,
        'staff': staff,
        'donor': donor,
        'project': project,
        'event': event,
        'donation': donation
    }
    template = loader.get_template('donor_table.html')
    return HttpResponse(template.render(context, request))


def staff_views(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            staff = Staff.objects.get(password=password, email=email)
            user = User.objects.get(username=staff.user)
            if staff is not None:
                login(request, user)
                return redirect('/staff/table/')
            else:
                context['error'] = "Please enter valid username and password"
        except:
            context['error'] = "Please enter valid username and password"
    template = loader.get_template('staff_login.html')
    return HttpResponse(template.render(context, request))


def staff_register_views(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        st_user = request.POST.get('user')
        email = request.POST.get('email')
        pas1 = request.POST.get('pas1')
        pas2 = request.POST.get('pas2')
        address = request.POST.get('address')
        user = User.objects.get(username=st_user)
        try:
            if pas1 == pas2:
                user = Staff(name=name,contact=contact, user=user, email=email, password=pas1, address=address)
                user.save()
                return redirect('/staff/')
            else:
                context['error'] = "Please enter valid Email and Password"
        except:
            context['error'] = "Please enter valid details"
    template = loader.get_template('staff_register.html')
    return HttpResponse(template.render(context, request))


def staff_forget_pass_views(request):
    data_to_send = "Staff"
    request.session['data'] = data_to_send
    context = {
        'title': "staff"
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = randrange(111111, 1000000)
        try:
            donator = Donor.objects.get(email=email)
        except:
            context['error'] = 'This Email Does"n Exist !!'
        else:
            send_mail(
                f'Your Code is:{otp} ',
                "Here is the message.",
                "chotaliyarahul68@gmail.com",
                [email],
                fail_silently=False
            )
            code = Otp(otp=otp)
            code.save()
            return redirect('/code/')
    template = loader.get_template('ngo_forget_pass.html')
    return HttpResponse(template.render(context, request))


def staff_table_views(request):
    user = request.user
    profile = Staff.objects.get(user=user)
    ngo = User.objects.all()
    volunteer = Volunteer.objects.all()
    staff = Staff.objects.all()
    donor = Donor.objects.all()
    project = Project.objects.all()
    event = Event.objects.all()
    donation = Donation.objects.all()
    context = {
        'ngo': ngo,
        'user': profile,
        'volunteer': volunteer,
        'staff': staff,
        'donor': donor,
        'project': project,
        'event': event,
        'donation': donation
    }
    template = loader.get_template('staff_table.html')
    return HttpResponse(template.render(context, request))


def home_views(request):
    user = request.user
    ngo = User.objects.all().order_by('-id')[:5]
    volunteer = Volunteer.objects.all().order_by('-id')[:5]
    staff = Staff.objects.all().order_by('-id')[:5]
    donor = Donor.objects.all().order_by('-id')[:5]
    project = Project.objects.all()
    event = Event.objects.all()
    donation = Donation.objects.all()
    context = {
        'ngo': ngo,
        'volunteer': volunteer,
        'staff': staff,
        'donor': donor,
        'project': project,
        'event': event,
        'donation': donation,
        'user': user
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def code_views(request):
    context = {}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        try:
            code = Otp.objects.get(otp=otp)
        except:
            context['error'] = "Please enter valid OTP"
        else:
            if code is not None:
                code.delete()

                return redirect('/reset/')
            else:
                context['error'] = "Please enter valid OTP"
    template = loader.get_template('code.html')
    return HttpResponse(template.render(context, request))


def reset_views(request):
    data_received = request.session.get('data')
    if data_received == 'Donor':
        Model = Donor
        title = 'donor'
    elif data_received == 'Staff':
        Model = Staff
        title = 'staff'
    elif data_received == 'Volunteer':
        Model = Volunteer
        title = 'volunteer'
    else:
        Model = ''
        title = 'ngo'
    print(data_received, 'lpolpo')
    user = request.user
    context = {
        'title': title
    }
    try:
        model = Model.objects.get(user=user.username)
    except:
        pass
    if request.method == 'POST':
        pas1 = request.POST.get('pas1')
        pas2 = request.POST.get('pas2')
        if pas1 == pas2:
            try:
                if model != "User" | model == '':
                    model.password = pas1
                    model.save()
                    context['error'] = "Your password has been changed successfully"
            except:
                user.set_password(pas1)
                user.save()
                context['error'] = "Your password has been changed successfully"
    template = loader.get_template('reset_password.html')
    return HttpResponse(template.render(context, request))


def event_views(request):
    event = Event.objects.all()
    context = {
        'event': event
    }
    template = loader.get_template('event.html')
    return HttpResponse(template.render(context, request))


def event_ngo_views(request):
    user = request.user
    event = Event.objects.all()
    context = {
        'event': event,
        'user': user
    }
    template = loader.get_template('event_ngo.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/home/')
def event_add_views(request):
    volunteer = Volunteer.objects.all()
    ngo = User.objects.all()
    context = {
        'volunteer': volunteer,
        'ngo': ngo
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        associated_volunteer = request.POST.get('associated_volunteer')
        pic = request.POST.get('pic')
        event_for = request.POST.get('event_for')

        try:
            associated_volunteer = Volunteer.objects.get(id=associated_volunteer)
            event_for = User.objects.get(id=event_for)
        except:
            context['msg'] = "Please enter valid data"
        else:
            event = Event(title=title, description=description, start_date=start_date, time=time, location=location,
                          associated_volunteer=associated_volunteer, pic=pic, event_for=event_for)
            event.save()
            context['msg']= 'Your event has been successfully added!!'

    template = loader.get_template('event_add.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/home/')
def event_edit_views(request, id):
    ngo = User.objects.all()
    event = Event.objects.get(id=id)
    volunteer = Volunteer.objects.all()
    context = {
        'volunteer': volunteer,
        'ngo': ngo,
        'event': event
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date =  event.start_date
        time =  event.time
        location = request.POST.get('location')
        associated_volunteers = request.POST.get('associated_volunteers')
        event_for = request.POST.get('event_for')
        try:
            associated_volunteers = Volunteer.objects.get(id=associated_volunteers)
            event_for = User.objects.get(id=event_for)
        except:
            context['msg'] = "Please enter valid data"
        else:
            event.title=title
            event.description=description
            event.start_date=start_date
            event.time=time
            event.location=location
            event.associated_volunteer=associated_volunteers
            event.event_for= event_for
            event.save()
            context['msg'] = 'Your event has been successfully added!!'
            return redirect('/event/ngo/')
    template = loader.get_template('event_edit.html')
    return HttpResponse(template.render(context, request))


def project_views(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    template = loader.get_template('project.html')
    return HttpResponse(template.render(context, request))


def project_ngo_views(request):
    project = Project.objects.all()
    user = request.user
    context = {
        'project': project,
        'user': user
    }
    template = loader.get_template('project_ngo.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/home/')
def project_add_views(request):
    volunteer = Volunteer.objects.all()
    ngo = User.objects.all()
    context = {
        'volunteer': volunteer,
        'ngo': ngo
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        associated_volunteers = request.POST.get('associated_volunteers')
        project_for = request.POST.get('project_for')
        pic = request.POST.get('pic')
        try:
            associated_volunteers = Volunteer.objects.get(id=associated_volunteers)
            project_for = User.objects.get(id=project_for)
        except:
            context['msg'] = "Please enter valid data"
        else:
            project = Project(title=title, description=description, start_date=start_date, end_date=end_date,associated_volunteers=associated_volunteers, pic=pic, project_for=project_for)
            project.save()
            context['msg'] = 'Your event has been successfully added!!'
            return redirect('/project/')
    template = loader.get_template('project_add.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/project/')
def project_edit_views(request,id):
    project = Project.objects.get(id=id)
    volunteer = Volunteer.objects.all()
    ngo = User.objects.all()
    context = {
        'volunteer': volunteer,
        'ngo': ngo,
        'project': project
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = project.start_date
        end_date = project.end_date
        associated_volunteers = request.POST.get('associated_volunteers')
        project_for = request.POST.get('project_for')
        try:
            associated_volunteers = Volunteer.objects.get(id=associated_volunteers)
            project_for = User.objects.get(id=project_for)
        except:
            context['msg'] = "Please enter valid data"
        else:
            project.title = title
            project.description = description
            project.start_date = start_date
            project.end_date = end_date
            project.associated_volunteers = associated_volunteers
            project.project_for = project_for
            project.save()
            context['msg'] = 'Your event has been successfully added!!'
            return redirect('/project/')
    template = loader.get_template('project_edit.html')
    return HttpResponse(template.render(context, request))


def donation_views(request):
    donation = Donation.objects.all()
    context = {
        'donation': donation
    }
    template = loader.get_template('donation.html')
    return HttpResponse(template.render(context, request))


def donation_ngo_views(request):
    user = request.user
    donation = Donation.objects.all()
    context = {
        'donation': donation,
        'user': user
    }
    template = loader.get_template('donation_ngo.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/home/')
def donation_add_views(request):
    donor = Donor.objects.all()
    donation_all = User.objects.all()
    context = {
        'donor': donor,
        'donation':donation_all
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        donation_for = request.POST.get('donation_for')
        about_donation = request.POST.get('about_donation')
        upcoming_donation = request.POST.get('upcoming_donation')
        donation_amount = request.POST.get('donation_amount')
        donor = request.POST.get('donor')
        pic = request.POST.get('pic')
        try:
            donor_obj = Donor.objects.get(id=donor)
            donation_for_obj = User.objects.get(id=donation_for)
        except:
            context['msg'] = "Please enter valid data"
        else:
            donation = Donation(upcoming_donation=upcoming_donation, donor=donor_obj, donation_amount=donation_amount, pic=pic,name=name, about_donation=about_donation, donation_for=donation_for_obj)
            donation.save()
            context['msg'] = 'Your event has been successfully added!!'
            return redirect('/donation/')
    template = loader.get_template('donation_add.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/donation/')
def donation_edit_views(request, id):
    donation = Donation.objects.get(id=id)
    ngo = User.objects.all()
    donor = Donor.objects.all()
    context = {
        'donation': donation,
        'donor': donor,
        'ngo': ngo
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        donation_for = request.POST.get('donation_for')
        about_donation = request.POST.get('about_donation')
        upcoming_donation = request.POST.get('upcoming_donation')
        donation_amount = request.POST.get('donation_amount')
        donor = request.POST.get('donor')
        try:
            donor_obj = Donor.objects.get(id=donor)
            donation_for_ngo = User.objects.get(id=donation_for)
        except:
            context['msg'] = "Please enter valid data"
        else:
            donation.name=name
            donation.donation_for=donation_for_ngo
            donation.about_donation=about_donation
            donation.upcoming_donation=upcoming_donation
            donation.donation_amount=donation_amount
            donation.donor=donor_obj
            donation.save()
            context['msg'] = 'Your event has been successfully added!!'
            return redirect('/donation/')
    template = loader.get_template('donation_edit.html')
    return HttpResponse(template.render(context, request))


def ngo_list_views(request):
    ngo = User.objects.all()
    volunteer = Volunteer.objects.all()
    context = {
        'ngo': ngo,
        'volunteer': volunteer
    }
    template = loader.get_template('ngo_list.html')
    return HttpResponse(template.render(context, request))


def donator_list_views(request):
    donor = Donor.objects.all()
    context ={
        'donor': donor
    }
    template = loader.get_template('donor_list.html')
    return HttpResponse(template.render(context, request))


def donator_ngo_list_views(request):
    donor = Donor.objects.all()
    context = {
        'donor': donor
    }
    template = loader.get_template('donor_ngo_list.html')
    return HttpResponse(template.render(context, request))


def volunteer_list_views(request):
    volunteer = Volunteer.objects.all()
    context = {
        'volunteer': volunteer
    }
    template = loader.get_template('volunteer_list.html')
    return HttpResponse(template.render(context, request))


def volunteer_ngo_list_views(request):
    volunteer = Volunteer.objects.all()
    context = {
        'volunteer': volunteer
    }
    template = loader.get_template('volunteer_ngo_list.html')
    return HttpResponse(template.render(context, request))


def staff_list_views(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff
    }
    template = loader.get_template('staff_list.html')
    return HttpResponse(template.render(context, request))


def staff_ngo_list_views(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff
    }
    template = loader.get_template('staff_ngo_list.html')
    return HttpResponse(template.render(context, request))


def ngo_delete_views(request, id):
    pk = User.objects.get(id=id)
    print(pk)
    pk.delete()
    return redirect('/Volunteer/table/')


def volunteer_delete_views(request, id):
    pk = Volunteer.objects.get(id=id)
    print(pk)
    pk.delete()
    return redirect('/ngo/table/')


def donor_delete_views(request, id ):
    pk = Donor.objects.get(id=id)
    pk.delete()
    return redirect('/ngo/table/')


def staff_delete_views(request, id):
    pk = Staff.objects.get(id=id)
    pk.delete()
    return redirect('/ngo/table/')


@login_required(login_url='/donation/')
def donation_delete_views(request, id):
    pk = Donation.objects.get(id=id)
    pk.delete()
    return redirect('/donation/')


@login_required(login_url='/project/')
def project_delete_views(request, id):
    pk = Project.objects.get(id=id)
    pk.delete()
    return redirect('/project/')