from django.contrib.auth.decorators import login_required, permission_required 
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django import template
import simplejson as json
from datetime import timedelta, datetime as dt_class
from rest_framework.decorators import api_view
from apiHelper.apiHelper import ApiHelper
from django.utils import timezone
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Case, When, Count
import requests

from customer.models import *
from biker.models import *


@csrf_exempt
def createCustomer(request):  
    try:
        form =  ApiHelper.getData(request)
        
        username = form['username'] 
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name'] 
        gender = form['gender'] if 'gender' in form else None
        phone_number = form['phone_number']
        date_of_birth = dt_class.strptime(form['date_of_birth'], '%Y-%m-%d') if 'date_of_birth' in form else None
        address = form['address'] if 'address' in form else None

        user_created = User.objects.filter(username="admin").first()
        
        list_customer_invalid = Customer.objects.filter(account=user_created)
        for item in list_customer_invalid:
            item.delete()
        
        try:
            customer = Customer(
                first_name = first_name,
                last_name = last_name,
                gender = gender,
                phone_number = phone_number,
                date_of_birth = date_of_birth,
                address = address,
                account = user_created,
                created_date = timezone.now(),
                created_by = user_created
            )
            customer.save()

            account = createAccount(username, None, password)

            if not account:
                customer.delete()
                return JsonResponse({
                    'code': 100,
                    'data': 'Tên tài khoản đã tồn tại!'
                })
            else:
                customer.account = account
                customer.save()
        except Exception as ex:
            print(ex)
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['GET'])
def getUser(request):
    try:
        token = request.GET.get("token")
        params = {
            "token":token,
        }
        r = requests.post('https://bikepicker-auth.herokuapp.com/verify-token', data=json.dumps(params), headers={'content-type': 'application/json'})
     
        if (not r.text.isnumeric()): return ApiHelper.Response_ok(r.json()['message'])
        
        query = User.objects.filter(is_deleted=False, phone_number=r.text).values(
            'phone_number',
            'email',
            'first_name',
            'last_name',
            'female',
            'date_of_birth',
            'address',
            'is_active'
        )
        return ApiHelper.Response_ok(list(query))
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
def updateUser(request):  
    try:
        form =  ApiHelper.getData(request)
        
        first_name = form['first_name']
        last_name = form['last_name'] 
        female = form['female'] if 'female' in form else None
        email = form['email']
        password = form['password']
        date_of_birth = dt_class.strptime(form['date_of_birth'], '%Y-%m-%d') if 'date_of_birth' in form else None
        address = form['address'] if 'address' in form else None

        token = form['token']
        params = {
            "token":token,
        }
        r = requests.post('https://bikepicker-auth.herokuapp.com/verify-token', data=json.dumps(params), headers={'content-type': 'application/json'})
     
        if (not r.text.isnumeric()): return ApiHelper.Response_ok(r.json()['message'])

        try:
            user_update = User.objects.filter(is_deleted=False, phone_number=r.text).first()
            user_update.first_name = first_name
            user_update.last_name = last_name
            user_update.female = female
            user_update.email = email
            user_update.password = password
            user_update.date_of_birth = date_of_birth
            user_update.address = address
 
            user_update.save()
        except Exception as e:
            return ApiHelper.Response_client_error(e)

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
def updatePassword(request):  
    try:
        form =  ApiHelper.getData(request)

        token = form['token']
        params = {
            "token":token,
        }
        r = requests.post('https://bikepicker-auth.herokuapp.com/verify-token', data=json.dumps(params), headers={'content-type': 'application/json'})
     
        if (not r.text.isnumeric()): return ApiHelper.Response_ok(r.json()['message'])

        password = form['password']
        user_delete = User.objects.filter(is_deleted=False, phone_number=r.text).first()
        user_delete.password = password
        user_delete.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


# def createAccount(username, email, password):
#     try:
#         user = User.objects.create_user(username, email, password)
#         return user
#     except:
#         return None


@api_view(['GET'])
def getReportBikerLog(request):
    try:
        token = request.GET.get('token')
        to_month = dt_class.strptime(request.GET.get('t_date'), '%Y-%m-%d')
        from_month = dt_class.strptime(request.GET.get('f_date'), '%Y-%m-%d')
        # mode = request.GET.get('mode')

        params = {
            "token":token,
        }
        r = requests.post('https://bikepicker-auth.herokuapp.com/verify-token', data=json.dumps(params), headers={'content-type': 'application/json'})
     
        if (not r.text.isnumeric()): return ApiHelper.Response_ok(r.json()['message'])

        list_result = []
        # if mode == 'month':
        #     for month in monthrange(from_month, to_month):
        #         biker_log = BikerLog.objects.filter(date__month=month.month).values(
        #             'created_date__month'
        #         ).annotate(total_price=Sum('price'), total=Count('id'))

        #         biker_log_cancelled = BikerLog.objects.filter(date__month=month.month, isRideCancelled=True).values(
        #             'created_date__month'
        #         ).annotate(total_price=Sum('price'), total_cancelled=Count('id'))
                
        #         if biker_log:
        #             biker_log[0]['total_price'] -= biker_log_cancelled[0]['total_price'] if biker_log_cancelled else 0
        #             biker_log[0]['total_confirmed'] = biker_log[0]['total'] 
        #             biker_log[0]['total_confirmed'] -= biker_log_cancelled[0]['total_cancelled'] if biker_log_cancelled else 0
        #             biker_log[0]['total_cancelled'] = biker_log_cancelled[0]['total_cancelled'] if biker_log_cancelled else 0

        #         # total_distance: 1000
        #         list_result.append({
        #             'month': month.strftime("%m-%Y"),
        #             'total_price': biker_log[0]['total_price'] if biker_log else 0,
        #             'total': biker_log[0]['total'] if biker_log else 0,
        #             'total_confirm': biker_log[0]['total_confirmed'] if biker_log else 0,
        #             'total_cancelled': biker_log[0]['total_cancelled'] if biker_log else 0,
        #         })
        # elif mode == 'week':
        #     date_start_week = from_month - timedelta(days=from_month.weekday())
            
        #     for i in range(4):
        #         date_end_week = date_start_week + timedelta(days=6)
        #         biker_log = BikerLog.objects.filter(date__gte=date_start_week, date__lte=date_end_week).values(
        #             'created_date__year'
        #         ).annotate(total_price=Sum('price'), total=Count('id'))

        #         biker_log_cancelled = BikerLog.objects.filter(date__gte=date_start_week, date__lte=date_end_week, isRideCancelled=True).values(
        #             'created_date__year'
        #         ).annotate(total_price=Sum('price'), total_cancelled=Count('id'))
                
        #         if biker_log:
        #             biker_log[0]['total_price'] -= biker_log_cancelled[0]['total_price'] if biker_log_cancelled else 0
        #             biker_log[0]['total_confirmed'] = biker_log[0]['total'] 
        #             biker_log[0]['total_confirmed'] -= biker_log_cancelled[0]['total_cancelled'] if biker_log_cancelled else 0
        #             biker_log[0]['total_cancelled'] = biker_log_cancelled[0]['total_cancelled'] if biker_log_cancelled else 0

        #         # total_distance: 1000
        #         list_result.append({
        #             'date_start_week': date_start_week.strftime("%d-%m-%Y"),
        #             'total_price': biker_log[0]['total_price'] if biker_log else 0,
        #             'total': biker_log[0]['total'] if biker_log else 0,
        #             'total_confirm': biker_log[0]['total_confirmed'] if biker_log else 0,
        #             'total_cancelled': biker_log[0]['total_cancelled'] if biker_log else 0,
        #         })
        #         date_start_week = date_end_week + timedelta(days=1)
        for single_date in daterange(from_month, to_month):
            biker_log = BikerLog.objects.filter(date__date=single_date).values(
                'created_date__year'
            ).annotate(total_price=Sum('price'), total=Count('id'))

            biker_log_cancelled = BikerLog.objects.filter(date__date=single_date, is_ride_cancelled=True).values(
                'created_date__year'
            ).annotate(total_price=Sum('price'), total_cancelled=Count('id'))
            
            if biker_log:
                biker_log[0]['total_price'] -= biker_log_cancelled[0]['total_price'] if biker_log_cancelled else 0
                biker_log[0]['total_confirmed'] = biker_log[0]['total'] 
                biker_log[0]['total_confirmed'] -= biker_log_cancelled[0]['total_cancelled'] if biker_log_cancelled else 0
                biker_log[0]['total_cancelled'] = biker_log_cancelled[0]['total_cancelled'] if biker_log_cancelled else 0

            list_result.append({
                # 'f_date': from_month.strftime("%Y-%m-%d"),
                # 't_date': to_month.strftime("%Y-%m-%d"),
                'date': single_date.strftime("%Y-%m-%d"),
                'amt': biker_log[0]['total_price'] if biker_log else 0,
                # 'total': biker_log[0]['total'] if biker_log else 0,
                'count_success': biker_log[0]['total_confirmed'] if biker_log else 0,
                'count_cancel': biker_log[0]['total_cancelled'] if biker_log else 0,
            })

        return ApiHelper.Response_ok(list(list_result))
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days + 1)):
        yield start_date + timedelta(days=n)

def monthrange(start_date, end_date):
    start_date = start_date.replace(day=1)
    end_date = end_date.replace(day=1)
    date = start_date
    r = [ ]
    while date <= end_date:
        r.append(date) 
        date = (date + timedelta(days=31)).replace(day=1)
    return r