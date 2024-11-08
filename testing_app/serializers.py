from .models import Testing
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Testing, Company



class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'
    

    def get_employee_count(self, obj):
        count = obj.testing_set.count()
        return count





class TestingSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Testing
        fields = ['name', 'title', 'description', 'company']


