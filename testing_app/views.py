from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TestingSerializer, CompanySerializer
from .models import Testing, Company
from rest_framework import status
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



# Create your views here.
# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == "GET":

#         query = request.GET.get('query')
#         if query == None:
#             query = ''
        
#         tests = Testing.objects.filter(Q(name__icontains=query) | Q(title__icontains=query))
        
#         serializer = TestingSerializer(tests, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         # test = Testing.objects.create(
#         #     name = re
#         #     title = 
#         #     description = 
#         # )
#         test = request.data
#         serializer = TestingSerializer(data=test)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


class TestingList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        testing = Testing.objects.all()
        serializer = TestingSerializer(testing, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TestingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class TestingDetails(APIView):

    def get_object(self, pk):
        try:
            return Testing.objects.get(id=pk)
        except Testing.DoesNotExist:
            raise Http404
        
    
    def get(self, request, pk, format=None):
        testing = self.get_object(pk)
        serializer = TestingSerializer(testing)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        testing = self.get_object(pk)
        serializer = TestingSerializer(testing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'PUT', 'DELETE'])
# def test(request, username):
#     each_test = Testing.objects.get(name=username)

#     if request.method == "GET":
#         serializer = TestingSerializer(each_test, many=False)
#         return Response(serializer.data)
    
#     if request.method == "PUT":
#         each_test.name = request.data['name']
#         each_test.title = request.data['title']
#         each_test.description = request.data['description']

#         each_test.save()

#         serializer = TestingSerializer(each_test, many=False)
#         return Response(serializer.data)
    
#     if request.method == "DELETE":
#         each_test.delete()
#         return Response('user was deleted')




# @api_view(['GET'])
# def access(request, username):
#     test = Testing.objects.get(name=username)
#     serializer = TestingSerializer(test, many=False)
#     return Response(serializer.data)








class CompanyList(APIView):


    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)