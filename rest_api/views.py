from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Account
from uploading.models import Post
from .serializer import PostSerializer, UserSerializer
from rest_framework import status
# Create your views here.

@api_view()
def routes(request):
    urls = [
        'GET api/projects',
        'GET api/project/<int:product_id>',
        'GET api/users',

        'POST api/register-user/',
    ]
    return Response(urls)

@api_view()
def projects(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def project(request, product_id):
    post = Post.objects.get(id = product_id)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serialzer = PostSerializer(instance = post, data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else :
            return Response(serialzer.errors)

@api_view(['POST'])
def user_registration(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else :
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view()
def users(request):
    users = Account.objects.all()
    serializer = UserSerializer(users , many=True)
    return Response(serializer.data)