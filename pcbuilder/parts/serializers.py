from rest_framework import serializers
from .models import Part, PartSpec, PartImage, PartVideo, PartComparison, PartCompatibility, PartRecommendation

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class PartSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartSpec
        fields = '__all__'

class PartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartImage
        fields = '__all__'

class PartVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartVideo
        fields = '__all__'

class PartComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartComparison
        fields = '__all__'

class PartCompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartCompatibility
        fields = '__all__'  

class PartRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRecommendation
        fields = '__all__'



