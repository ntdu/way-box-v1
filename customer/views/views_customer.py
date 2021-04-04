from django.contrib.auth.decorators import login_required, permission_required 
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django import template
import simplejson as json
from datetime import datetime as dt_class
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from apiHelper.apiHelper import ApiHelper
from django.utils import timezone
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import requests

from customer.models import *


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
            'id',
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
        phone_number = form['phone_number']
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
            user_update.phone_number = phone_number
            user_update.email = email
            user_update.password = password
            user_update.date_of_birth = date_of_birth
            user_update.address = address
 
            user_update.save()
        except:
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

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