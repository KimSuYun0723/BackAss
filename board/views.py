from django.shortcuts import get_object_or_404
from .models import Board
from .serializers import *
#from rest_framework.decorators import api_view, authentication_classes, permission_classes
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from .permissions import IsOwnerOrReadOnly
#from rest_framework_simplejwt.authentication import JWTAuthentication

#get, post 게시글 (/blog/)
class BoardList(ListCreateAPIView): 
    queryset = Board.objects.all() 
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user) #override

#게시글 상세 페이지 불러오기(/blog/id/)
class BoardId(RetrieveAPIView): 
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

# 게시글 수정(/blog/id/update)
class BoardFix(UpdateAPIView): 
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

# 게시글 삭제(/blog/id/destroy)
class BoardDestroy(RetrieveDestroyAPIView): 
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

#get, post 댓글 (id/comment)_로그인한 유저
class BoardComment(ListCreateAPIView): 
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        board_id = self.kwargs['pk']
        queryset = Comment.objects.filter(post_id = board_id)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

