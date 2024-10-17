from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):

    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content')
    
    # 기존 comment_set 역참조 데이터를 override
    # related_name 설정 했으면 그 이름으로 해야댐
    comment_set = CommentDetailSerializer(many=True, read_only=True)


    # 댓글 개수 제공을 위한 새로운 필드 생성
    number_of_comments = serializers.IntegerField(source='comment_set.count', read_only=True)



    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    article =  ArticleTitleSerializer(read_only=True)
        
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)



