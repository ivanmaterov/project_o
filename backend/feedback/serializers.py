from rest_framework import serializers

from .models import BookFeedback


class BookFeedbackSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BookFeedback
        fields = "__all__"
