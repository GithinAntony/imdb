from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import *
from filim_user.models import *
from filim_pro.models import *
from filim_user.models import registration as user_registration
from filim_pro.models import registration as pro_registration
from django.db.models import Avg, Count
# Create your views here.
def login(request):
    if request.method == 'POST':
            data_record = request.POST
            if data_record['username']=="admin" and data_record['password']=="admin":
                request.session['is_logged_in'] = True
                request.session['email'] = "admin@admin.com"
                request.session['firstname'] = "admin"
                request.session['lastname'] = "admin"
                request.session['user_id'] = 0
                request.session['mobile_number'] = 9999999999
                request.session['usertype'] = 'site_admin'
                return redirect(reverse('site_admin:dashboard'))
            else:
                messages.error(request, 'Invalid credentials!')
                return redirect(reverse('site_admin:login'))
    return render(request, 'site_admin/login.html')

def logout(request):
    del request.session['is_logged_in']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['user_id']
    del request.session['mobile_number']
    del request.session['usertype']
    return redirect(reverse('site_admin:login'))

def dashboard(request):
    return render(request, 'site_admin/dashboard.html')

def list_screens(request):
    data_record = screens.objects.all()
    context = { 'data_record':data_record }
    return render(request, 'site_admin/list-screens.html', context)

def add_screens(request):
    return render(request, 'site_admin/add-screen.html')

def view_screens(request):
    return render(request, 'site_admin/view-screen.html')

def list_movie(request):
    data_list = movie.objects.all()
    rating = movie_rating.objects.values('movie_id').annotate(rating_value=Avg('rating_scale', distinct=True))
    context = { 'data_list': data_list, 'rating': rating }
    return render(request, 'site_admin/list-movie.html', context)

def view_movie(request, id):
    if request.method == 'POST':
        data_record = request.POST
        record = movie_rating(
            user_id=request.session['user_id'],
            movie_id=id,
            review_title=data_record['title'],
            review=data_record['review'],
            rating_scale=data_record['rating'],
            )
        record.save()
        messages.success(request, 'Review added successfully!')
        return redirect(reverse('site_admin:view_movie', args=[id]))

    userdata = movie.objects.get(unique_id=id)
    userdata_photos = movie_photo.objects.filter(movie_id=id)
    userdata_cast = movie_cast_crew.objects.filter(type="cast",movie_id=id)
    userdata_crew = movie_cast_crew.objects.filter(type="crew",movie_id=id)
    userdata_reviews = movie_rating.objects.filter(movie_id=id)
    rating_val = movie_rating.objects.filter(movie_id=id).values('movie_id').annotate(rating_value=Avg('rating_scale', distinct=True),rating_count=Count('rating_scale'))
    context = { 'userdata': userdata, 'userdata_photos':userdata_photos, 'userdata_cast':userdata_cast,'userdata_crew':userdata_crew, 'userdata_rating':rating_val, 'userdata_reviews':userdata_reviews, 'record_id':id }
    return render(request, 'site_admin/view-movie.html', context)

def list_people(request):
    data_list = people.objects.all()
    context = { 'data_list': data_list }
    return render(request, 'site_admin/list-people.html', context)

def view_people(request, id):
    userdata = people.objects.get(unique_id=id)
    userdata_photos = people_photo.objects.filter(people_id=id)
    userdata_filmography = movie_cast_crew.objects.filter(people_id=id)
    context = { 'userdata': userdata, 'userdata_photos':userdata_photos, 'userdata_filmography':userdata_filmography }
    return render(request, 'site_admin/view-people.html', context)

def list_user(request):
    data_list = user_registration.objects.all()
    context = { 'data_list': data_list }
    return render(request, 'site_admin/list-user.html', context)

def list_pro(request):
    data_list = pro_registration.objects.all()
    context = { 'data_list': data_list }
    return render(request, 'site_admin/list-pro.html', context)

def change_pro_status(request, id, status):
    userdata = pro_registration.objects.get(unique_id=id)
    temp_status = "pending"
    if status == "pending":
        temp_status = "active"
    userdata.status = temp_status
    userdata.save()
    messages.success(request, 'Status changed successfully!')
    return redirect(reverse('site_admin:list_pro'))
