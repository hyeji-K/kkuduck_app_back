from typing_extensions import Required
from rest_framework import fields, serializers
from .models import DefaultSubscription, Plan
from user_api import models

class PlanSerializer(serializers.ModelSerializer): # planserializer 가 반드시 default 보다 위에 있어야함
    class Meta:
        model = Plan 
        fields = (
            'plan_name',
            'plan_price',
            'cycle',
            'dsub_id'
        )

class DefaultSerializer(serializers.ModelSerializer):

    plans = PlanSerializer(many=True, read_only=True) # model 에서 related_named 로 설정했던 거와 같은 이름인 plans 이어야 함
    class Meta:
        model = DefaultSubscription
        fields = (
            'service_name',
            'image_url',
            'plans'
        )

class DefaultBodySerializer(serializers.Serializer):
    service_name = serializers.CharField(help_text="구독 서비스 이름 작성")
    image_url = serializers.CharField(help_text="구독 서비스의 이미지 url 작성")

class PlanBodySerializer(serializers.Serializer):
    dsub_id = serializers.IntegerField(help_text="구독 서비스의 id 작성")
    plan_name = serializers.CharField(help_text="구독 서비스의 플랜 이름 작성")
    plan_price = serializers.IntegerField(help_text="플랜 가격 작성")
    cycle = serializers.CharField(help_text="플랜 주기 작성")