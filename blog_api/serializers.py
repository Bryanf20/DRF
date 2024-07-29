# Used to format the data that is going to be returned to app(json/xml)
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category','id', 'title', 'slug', 'author', 'excerpt', 'content', 'status') #remember to add time