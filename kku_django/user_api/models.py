from django.db import models



class DefaultSubscription(models.Model):
    dsub_id = models.AutoField(null=False, primary_key=True)
    service_name = models.CharField(max_length=128, null=False)
    image_url = models.CharField(max_length=1024, null=True)
    
    class Meta:
        db_table = 'DefaultSubscription'

class Plan(models.Model):
    plan_name = models.CharField(max_length=128, null=False)
    plan_price = models.IntegerField(null=False)
    cycle = models.CharField(max_length=64, null=False)
    dsub_id = models.ForeignKey(DefaultSubscription, null=False, on_delete=models.CASCADE, db_column='dsub_id',related_name='plans') #related_name 추가, 반드시 관계맺으려는 모델의 필드명과 동일하게 fk 변수명 설정 필요

    class Meta:
        db_table = 'Plan'
