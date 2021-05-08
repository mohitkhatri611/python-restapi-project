from rest_framework import serializers
from hrm.models import Users

class UsersSerializer(serializers.ModelSerializer):
#serializer get data from database and send as to api.

    #2 ways to control null fields 1. serialzer level(used here) 2. Model Level (required migrations again)
    name= serializers.CharField(required = False)
    employee_id= serializers.CharField(required = False)
    ranking= serializers.FloatField(required = False)

    class Meta:
        model = Users
        #fields= ('name','employee_id')
        fields = '__all__' #use this to allow all fields.