from django.shortcuts import render
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Review
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# 비밀번호 인증 뷰 함수 작성(FBV)
@api_view(['POST'])
def validate_password(request, pk):
    review = get_object_or_404(Review, pk=pk)
    
    password = request.data['password']

    if password == review.password:
        return Response({"password": True})
    
    return Response({"password": False})