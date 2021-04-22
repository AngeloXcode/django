from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserAccessSerializer
from .models import UserAccess
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        User = UserAccess.objects.all()
        serializer = UserAccessSerializer(User, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserAccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(dict(error=serializer.errors),status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def user_detial(request, pk):
    try:
        user = UserAccess.objects.get (pk=pk)
        #return Response(status=status.HTTP_200_OK)
    except UserAccess.DoesNotExist:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = UserAccessSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserAccessSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = UserAccess.objects.get(pk=pk)
            serializer = UserAccessSerializer(user)
            return Response({"status" : "1","message":"Updated was successfully.","data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response("Error in Post",status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response("Error in Post", status=status.HTTP_400_BAD_REQUEST)


