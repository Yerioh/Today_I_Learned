from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 조회 => 타입 : 쿼리셋 => django에서 사용하는 데이터 타입
        articles = Article.objects.all()
        # 변환하기 쉬운 포맷으로 전환 => 직렬화
        # 쿼리셋이기 때문에 many 속성 사용
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 저장 성공 후 201 응답 상태코드를 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 후 400 응답 상태코드를 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # 단일 데이터이기 때문에 many 속성 사용 X
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)