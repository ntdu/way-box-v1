import math
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
import requests

from biker.models import *
from customer.models import *


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def activateCustomer(request):
    try:
        form = ApiHelper.getData(request)
        customer_id = form['id']

        customer = Customer.objects.filter(
            is_deleted=False, id=customer_id).first()

        if not customer:
            return ApiHelper.Response_info("Không tìm thấy tài khoản")

        customer.is_active = True
        customer.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deactivateCustomer(request):
    try:
        form = ApiHelper.getData(request)
        customer_id = form['id']

        customer = Customer.objects.filter(
            is_deleted=False, id=customer_id).first()

        if not customer:
            return ApiHelper.Response_info("Không tìm thấy tài khoản")

        customer.is_active = False
        customer.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteCustomer(request):
    try:
        form = ApiHelper.getData(request)
        customer_id = form['id']

        customer = Customer.objects.filter(
            is_deleted=False, id=customer_id).first()

        if not customer:
            return ApiHelper.Response_info("Không tìm thấy tài khoản")

        customer.is_deleted = True
        customer.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def activateBiker(request):
    try:
        form = ApiHelper.getData(request)
        biker_id = form['id']

        biker = Biker.objects.filter(is_deleted=False, id=biker_id).first()

        if not biker:
            return ApiHelper.Response_info("Không tìm thấy tài khoản")

        biker.is_active = True
        biker.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deactivateBiker(request):
    try:
        form = ApiHelper.getData(request)
        biker_id = form['id']
        print(biker_id)

        biker = Biker.objects.filter(is_deleted=False, id=biker_id).first()
        print(biker)
        # print(Biker.objects.filter(is_deleted=False).values('id'))


        print(biker.first_name)
        if not biker:
            return ApiHelper.Response_info("Không tìm thấy tài khoản")

        biker.is_active = False
        biker.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteBiker(request):
    try:
        form = ApiHelper.getData(request)
        biker_id = form['id']

        biker = Biker.objects.filter(is_deleted=False, id=biker_id).first()
        if not biker:
            return ApiHelper.Response_info("Không tìm thấy tài khoản")
        biker.is_deleted = True
        biker.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def listCustomer(request):
    try:
        offset = int(request.GET.get('offset'))
        limit = int(request.GET.get('limit'))

        query = Customer.objects.filter(is_deleted=False).values(
            'id',
            'account__username',
            'first_name',
            'last_name',
            'is_active',
            'gender',
            'phone_number',
            'date_of_birth',
            'address',
            'is_deleted',
            'created_date',
            'created_by__username',
            'last_updated_date',
            'last_updated_by__username'
        )

        if offset > query.count():
            return ApiHelper.Response_ok("")

        to_end = offset + limit

        if to_end > query.count():
            to_end = query.count()

        list_index = createList(offset, to_end)

        result = {
            'list_customer': [query[i] for i in list_index],
            'num_customer': query.count()
        }

        return ApiHelper.Response_ok(result)
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def listBiker(request):
    try:
        offset = int(request.GET.get('offset'))
        limit = int(request.GET.get('limit'))

        query = Biker.objects.filter(is_deleted=False).values(
            'id',
            'account__username',
            'first_name',
            'last_name',
            'is_active',
            'gender',
            'phone_number',
            'date_of_birth',
            'address',
            'is_deleted',
            'created_date',
            'created_by__username',
            'last_updated_date',
            'last_updated_by__username'
        )

        if offset > query.count():
            return ApiHelper.Response_ok("")

        to_end = offset + limit

        if to_end > query.count():
            to_end = query.count()

        list_index = createList(offset, to_end)

        result = {
            'list_biker': [query[i] for i in list_index],
            'num_biker': query.count()
        }

        return ApiHelper.Response_ok(result)
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


def createList(r1, r2):
    return [item for item in range(r1, r2)]


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateBiker(request):
    try:
        form = ApiHelper.getData(request)

        biker_id = form['biker_id'] if 'biker_id' in form else 0
        first_name = form['first_name']
        last_name = form['last_name']
        gender = form['gender'] if 'gender' in form else None
        phone_number = form['phone_number']
        date_of_birth = dt_class.strptime(
            form['date_of_birth'], '%Y-%m-%d') if 'date_of_birth' in form else None
        address = form['address'] if 'address' in form else None

        try:
            biker_update = Biker.objects.filter(
                is_deleted=False, id=biker_id).first()
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
def updateCustomer(request):
    try:
        form = ApiHelper.getData(request)

        customer_id = form['customer_id'] if 'customer_id' in form else 0
        first_name = form['first_name']
        last_name = form['last_name']
        gender = form['gender'] if 'gender' in form else None
        phone_number = form['phone_number']
        date_of_birth = dt_class.strptime(
            form['date_of_birth'], '%Y-%m-%d') if 'date_of_birth' in form else None
        address = form['address'] if 'address' in form else None

        try:
            customer_update = Customer.objects.filter(
                is_deleted=False, id=customer_id).first()
            customer_update.first_name = first_name
            customer_update.last_name = last_name
            customer_update.gender = gender
            customer_update.phone_number = phone_number
            customer_update.date_of_birth = date_of_birth
            customer_update.address = address
            customer_update.last_updated_date = timezone.now()
            customer_update.last_updated_by = request.user
            customer_update.save()
        except:
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


# @api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def getUser(request):
#     try:
#         phone_number = request.GET.get('phone')
#         query = Customer.objects.filter(is_deleted=False, phone_number=phone_number).values(
#             'id',
#             'account__username',
#             'first_name',
#             'last_name',
#             'is_active',
#             'gender',
#             'phone_number',
#             'date_of_birth',
#             'address'
#         )
#         if len(list(query)) is 0:
#             query = Biker.objects.filter(is_deleted=False, phone_number=phone_number).values(
#                 'id',
#                 'account__username',
#                 'first_name',
#                 'last_name',
#                 'is_active',
#                 'gender',
#                 'phone_number',
#                 'date_of_birth',
#                 'address'
#             )
#         return ApiHelper.Response_ok(list(query))
#     except Exception as e:
#         print(e)
#         return ApiHelper.Response_error()


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


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getBiker(request):
    try:
        id = request.GET.get('id')
        query = Biker.objects.filter(is_deleted=False, id=id).values(
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


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getCustomer(request):
    try:
        id = request.GET.get('id')
        query = Customer.objects.filter(is_deleted=False, id=id).values(
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


from django.db import connections
from django.db.utils import OperationalError
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def testConnection(request):
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
        return ApiHelper.Response_ok("fail")


    else:
        connected = True
        return ApiHelper.Response_ok("list")

from django.db.models import Sum, Case, When, Count

@api_view(['POST'])
def createBikerLog(request):
    try:
        form =  ApiHelper.getData(request)
        
        # token = form['token'] 

        # params = {
        #     "token":token,
        # }
        # r = requests.post('https://bikepicker-auth.herokuapp.com/verify-token', data=json.dumps(params), headers={'content-type': 'application/json'})
     
        # if (not r.text.isnumeric()): return ApiHelper.Response_ok(r.json()['message'])
        try:
            biker = form['biker'] 
            customer = form['customer']
            
            coordinates = form['coordinates'] 
            origin_lng = coordinates['origin']['lng']
            origin_lat = coordinates['origin']['lat']
            destination_lng = coordinates['destination']['lng']
            destination_lat = coordinates['destination']['lat']

            address = form['address']
            address_origin = address['origin']
            address_destination = address['destination']

            isRideConfirmed = form['isRideConfirmed']
            isRideCancelled = form['isRideCancelled']
            _id = form['_id'] if 'date_of_birth' in form else None
            _v = form['__v'] if 'date_of_birth' in form else None
            price = form['price']
            rideHash = form['rideHash']
            date = form['date']
            print("ok")
            # user_created = User.objects.filter(is_deleted=False, phone_number=r.text).first()
            biker = User.objects.filter(is_deleted=False, phone_number=biker).first()
            customer = User.objects.filter(is_deleted=False, phone_number=customer).first()
            
            biker_log = BikerLog(
                biker = biker,
                customer = customer,
                origin_lng = origin_lng,
                origin_lat = origin_lat,
                destination_lng = destination_lng,
                destination_lat = destination_lat,
                address_origin = address_origin,
                address_destination = address_destination,
                
                is_ride_confirmed = isRideConfirmed,
                is_ride_cancelled = isRideCancelled,
                _id = _id,
                _v = _v,
                price = price,
                ride_hash = rideHash,
                date = date,

                created_date = timezone.now()
            )
            biker_log.save()
        except Exception as e:
            print(e)
            return ApiHelper.Response_client_error(e)

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()

