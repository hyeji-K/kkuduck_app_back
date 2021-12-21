from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from user_api import models

#default 랑 plan 이랑 합치려고
from itertools import chain

from user_api.models import DefaultSubscription, Plan
from user_api.serializer import DefaultSerializer, PlanSerializer, DefaultBodySerializer, PlanBodySerializer

#swagger
from drf_yasg.utils import swagger_auto_schema


class DefaultSubView(APIView):
    
    def get(self, request,  **kwargs):
        """
            구독 서비스 리스트를 불러오는 API
            ---
            ### 내용
            - ### service_name : 구독 서비스의 이름
            - ### image_url : 서비스 이미지 
            - ### plans : 서비스의 플랜 종류
                - ### plan_name : 플랜 이름
                - ### plan_price : 플랜 가격
                - ### cycle : 결제 주기
        """
        if kwargs.get('uid') is None:
            dsub_queryset = DefaultSubscription.objects.all()
            dsub_serializer = DefaultSerializer(dsub_queryset, many=True)
            return Response({'count': dsub_queryset.count(), 'data': dsub_serializer.data}, status = status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            dsub_serializer = DefaultSerializer(DefaultSubscription.objects.get(dsub_id=uid))
            # 등록한 plan 종류
            plans = Plan.objects.filter(dsub_id=uid)
            plan_serializer = PlanSerializer(plans, many=True)
            return Response({'service_name':dsub_serializer.data.get('service_name'), 'image_url':dsub_serializer.data.get('image_url'), 'plans':plan_serializer.data}, status=status.HTTP_200_OK)   


    @swagger_auto_schema(request_body=DefaultBodySerializer)
    def post(self, request):
        dsub_serializer = DefaultSerializer(data=request.data)
        if dsub_serializer.is_valid():
            dsub_serializer.save()
            return Response({'result':'success', 'data':dsub_serializer.data}, status=status.HTTP_200_OK)
        else :
            return Response({'result':'fail', 'data':dsub_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DefaultSubViewWithId(APIView):
    
    def get(self, request, **kwargs):
        """
            구독 서비스를 불러오는 API
            ---
            ### 내용
            - ### service_name : 구독 서비스의 이름
            - ### image_url : 서비스 이미지 
            - ### plans : 서비스의 플랜 종류
                - ### plan_name : 플랜 이름
                - ### plan_price : 플랜 가격
                - ### cycle : 결제 주기
        """
        if kwargs.get('uid') is None:
            dsub_queryset = DefaultSubscription.objects.all()
            dsub_serializer = DefaultSerializer(dsub_queryset, many=True)
            return Response({'count': dsub_queryset.count(), 'data': dsub_serializer.data}, status = status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            dsub_serializer = DefaultSerializer(DefaultSubscription.objects.get(dsub_id=uid))
            # 등록한 plan 종류
            plans = Plan.objects.filter(dsub_id=uid)
            plan_serializer = PlanSerializer(plans, many=True)
            return Response({'service_name':dsub_serializer.data.get('service_name'), 'image_url':dsub_serializer.data.get('image_url'), 'plans':plan_serializer.data}, status=status.HTTP_200_OK)   
    
    def put(self, request, **kwargs):
        """
            구독 서비스를 수정하는 API
            ---
            ### 내용
            - ### service_name : 구독 서비스의 이름
            - ### image_url : 서비스 이미지 
            - ### plans : 서비스의 플랜 종류
                - ### plan_name : 플랜 이름
                - ### plan_price : 플랜 가격
                - ### cycle : 결제 주기
        """
        if kwargs.get('uid') is None:
            return Response("uid required", status = status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            dsub_object = DefaultSubscription.objects.get(dsub_id=uid)
            dsub_serializer = DefaultSubscription(dsub_object, data=request.data)
            if dsub_serializer.is_valid():
                dsub_serializer.save()
                return Response({'result':'success', 'data':dsub_serializer.data},status=status.HTTP_200_OK)
            else:
                return Response("error", status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, **kwargs):
        """
            구독 서비스를 삭제하는 API
            ---
            ### 내용
            - ### service_name : 구독 서비스의 이름
            - ### image_url : 서비스 이미지 
            - ### plans : 서비스의 플랜 종류
                - ### plan_name : 플랜 이름
                - ### plan_price : 플랜 가격
                - ### cycle : 결제 주기
        """
        if kwargs.get('uid') is None:
            return Response("uid required", status = status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            sub_object = DefaultSubscription.objects.get(dsub_id=uid)
            sub_object.delete()
            return Response({"result":"success"}, status= status.HTTP_200_OK)

class PlanView(APIView):
    @swagger_auto_schema(request_body=PlanBodySerializer)
    def post(self, request):
        plan_serializer = PlanSerializer(data=request.data)
        if plan_serializer.is_valid():
            plan_serializer.save()
            return Response({'result':'success', 'data':plan_serializer.data}, status=status.HTTP_200_OK)
        else :
            return Response({'result':'fail', 'data':plan_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
