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
# import requests
from biker.models import *


@csrf_exempt
def createBiker(request):  
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

        list_biker_invalid = Biker.objects.filter(account=user_created)
        for item in list_biker_invalid:
            item.delete()
            
        try:
            biker = Biker(
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
            biker.save()

            account = createAccount(username, None, password)

            if not account:
                biker.delete()
                return JsonResponse({
                    'code': 100,
                    'data': 'Tên tài khoản đã tồn tại!'
                })
            else:
                biker.account = account
                biker.save()

        except:
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

        return ApiHelper.Response_ok("Success")

        # params = {
        #     "firstName": first_name,
        #     "lastName": last_name,
        #     "female": gender,
        #     "phoneNumber": phone_number,
        #     "dateOfBirth": form['date_of_birth'],
        #     "address": address,
        #     "email": "123@1",
        #     "ssn": "0123",
        #     "plateNumber": "123A",
        #     "capacity": "3",
        #     "password": password,
        # }

        # params = {
        #     "firstName":"abca",
        #     "lastName":"xyz",
        #     "female":"false",
        #     "phoneNumber":"12345",
        #     "dateOfBirth":"1999-12-31",
        #     "address":"123 abc",
        #     "email":"123@1",
        #     "ssn":"0123",
        #     "plateNumber":"123A",
        #     "capacity":"3",
        #     "password":"Nguyentrongdu1@"
        # }

        # r = requests.post('https://bikepicker-auth.herokuapp.com/register', data=json.dumps(params), headers={'content-type': 'application/json'})

        # return ApiHelper.Response_ok(r.json())
        
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getBiker(request):
    try:
        query = Biker.objects.filter(is_deleted=False, account=request.user).values(
            'id',
            'account__username',
            'first_name',
            'last_name',
            'is_active',
            'gender',
            'phone_number',
            'date_of_birth',
            'address'
        )

        return ApiHelper.Response_ok(list(query))
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateBiker(request):  
    try:
        form =  ApiHelper.getData(request)
        
        first_name = form['first_name']
        last_name = form['last_name'] 
        gender = form['gender'] if 'gender' in form else None
        phone_number = form['phone_number']
        date_of_birth = dt_class.strptime(form['date_of_birth'], '%Y-%m-%d') if 'date_of_birth' in form else None
        address = form['address'] if 'address' in form else None

        try:
            biker_update = Biker.objects.filter(is_deleted=False, account=request.user).first()
            biker_update.first_name = first_name
            biker_update.last_name = last_name
            biker_update.gender = gender
            biker_update.phone_number = phone_number
            biker_update.date_of_birth = date_of_birth
            biker_update.address = address
            biker_update.last_updated_date = timezone.now()
            biker_update.last_updated_by = request.user
            biker_update.save()
        except:
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")
            
        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updatePassword(request):  
    try:
        form =  ApiHelper.getData(request)
        
        password = form['password']
        
        user = User.objects.filter(username=request.user.username).first()
        user.set_password(password)   
        user.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


def createAccount(username, email, password):
    try:
        user = User.objects.create_user(username, email, password)
        return user
    except:
        return None