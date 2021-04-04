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

from biker.models import *


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getVehicle(request):
    try:
        vehicle = Vehicle.objects.filter(is_deleted=False, biker = Biker.objects.filter(is_deleted=False, account=request.user).first()).values(
            'biker__id',
            'verify_status',
            'verify_vehicle__id',
            'route__id',
            'short_name',
            'plate_number',
            'capacity'
        )

        return ApiHelper.Response_ok(list(vehicle))
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def createVehicle(request):
    try:
        form =  ApiHelper.getData(request)
        short_name = form['short_name']
        plate_number = form['plate_number']
        
        try:
            vehicle_create = Vehicle(
                biker = Biker.objects.filter(is_deleted=False, account=request.user).first(),
                short_name = short_name,
                plate_number = plate_number
            )
            vehicle_create.save()
        except Exception as e:
            print(e)
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

        return ApiHelper.Response_ok(vehicle_create.id)
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateVehicle(request):
    try:
        form =  ApiHelper.getData(request)
        id = form['id']
        short_name = form['short_name']
        plate_number = form['plate_number']
        
        try:
            vehicle = Vehicle.objects.filter(is_deleted=False, id=id, biker=Biker.objects.filter(is_deleted=False, account=request.user).first()).first()
            vehicle.short_name = short_name
            vehicle.plate_number = plate_number
            vehicle.save()
        except:
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

        return ApiHelper.Response_ok()
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteVehicle(request):
    try:
        form =  ApiHelper.getData(request)
        id = form['id']
        
        vehicle = Vehicle.objects.filter(is_deleted=False, id=id, biker = Biker.objects.filter(is_deleted=False, account=request.user).first()).first()
        vehicle.is_deleted = True
        vehicle.save()

        return ApiHelper.Response_ok("Success")
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()


@permission_classes([IsAuthenticated])
def createVerifyVehicle(request):
    try:
        form =  ApiHelper.getData(request)
        short_name = form['short_name']
        plate_number = form['plate_number']
        
        try:
            vehicle_create = Vehicle(
                biker = Biker.objects.filter(is_deleted=False, account=request.user).first(),
                short_name = short_name,
                plate_number = plate_number
            )
            vehicle_create.save()
        except:
            return ApiHelper.Response_client_error("Sai kiểu dữ liệu")

        return ApiHelper.Response_ok()
    except Exception as e:
        print(e)
        return ApiHelper.Response_error()