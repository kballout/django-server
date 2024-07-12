from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer, PostTitleSerializer

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostTitleSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'title': request.data.get('title'), 
            'post': request.data.get('post'), 
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailView(APIView):
    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None
        
    def get(self, request, post_id):
        result = self.get_object(post_id)
        if not result:
            return Response(
                {"res": "Post does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)