from rest_framework import serializers
from .models import Country, Producer, Auto, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = ["id", "email", "auto", "date_comment", "comment", "user"]

    def validate_comment(self, value):
        # Проверка длины комментария
        if len(value) < 10:
            raise serializers.ValidationError("Комментарий должен содержать не менее 10 символов.")
        return value

class AutoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Auto
        fields = ["id", "name", "producer", "start_year", "end_year", "comments", "comments_count", "user"]

class ProducerSerializer(serializers.ModelSerializer):
    autos = AutoSerializer(many=True, required=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Producer
        fields = ["id", "name", "country", "autos", "user"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Убираем comments из сериализованных данных производителей
        for auto in representation['autos']:
            auto.pop('comments', None)  # Убираем поле 'comments', если оно есть

        return representation

class CountrySerializer(serializers.ModelSerializer):
    producers = ProducerSerializer(many=True, required=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Country
        fields = ["id", "name", "producers", "user"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Убираем autos из сериализованных данных производителей
        for producer in representation['producers']:
            producer.pop('autos', None)  # Убираем поле 'autos', если оно есть

        return representation