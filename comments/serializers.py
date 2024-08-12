from lxml import etree
from lxml.etree import HTMLParser
import bleach
from rest_framework import serializers

from .models import Comment

ALLOWED_TAGS = ['a', 'code', 'i', 'strong']
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
}

class RelatedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    related_comments = RelatedCommentSerializer(many=True, read_only=True, source='replies')
    user_name = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    homepage = serializers.ReadOnlyField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        ref_name = 'CommentSerializer'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        validated_data['user_name'] = user.name
        validated_data['email'] = user.email
        validated_data['homepage'] = user.homepage
        validated_data['user'] = user

        return super().create(validated_data)

    def validate_text(self, value):
        print("Валидируем текст:", value)

        cleaned_value = bleach.clean(
            value,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=False
        )

        if cleaned_value != value:
            raise serializers.ValidationError("Сообщение содержит недопустимые HTML теги или атрибуты.")

        return cleaned_value

