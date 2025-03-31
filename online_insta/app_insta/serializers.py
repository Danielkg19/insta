from django.db.migrations.serializer import Serializer
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }



class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class PostCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text', 'created_at', ]



class PostCommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'




class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'



class PostListSerializer(serializers.ModelSerializer):
    post_comment = PostCommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'post_image', 'post_video', 'description', 'hashtag', 'created_at', 'post_comment']



class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class PostLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'



class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class CommentLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'



class StoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'



class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'



class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'



class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'



class SaveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = '__all__'



class UserProfileListSerializer(serializers.ModelSerializer):
    count_following = serializers.SerializerMethodField()
    count_followers = serializers.SerializerMethodField()
    count_posts = serializers.SerializerMethodField()
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'last_name', 'profile_image', 'bio', 'website',
                  'count_following', 'count_followers', 'count_posts', 'posts']

    def get_count_following(self, obj):
        return Follow.objects.filter(follower=obj).count()

    def get_count_followers(self, obj):
        return Follow.objects.filter(following=obj).count()

    def get_count_posts(self, obj):
        return Post.objects.filter(user=obj).count()