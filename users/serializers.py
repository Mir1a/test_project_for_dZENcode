from rest_framework import serializers
from .models import User


class CommentSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    homepage = serializers.URLField(allow_blank=True, required=False)
    text = serializers.CharField(max_length=1000)
    created_at = serializers.DateTimeField()
    parent = serializers.PrimaryKeyRelatedField(read_only=True)


class UserSerializer(serializers.ModelSerializer):
    homepage = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['name', 'email', 'homepage', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['homepage'] = instance.homepage
        return representation
