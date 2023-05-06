from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,response
# Create your views here.

class MyView(APIView):
    
    def get(self,request):
        
        return response.Response(data={
            "msg":"OK"
            },status=status.HTTP_200_OK)