from rest_framework import serializers
from .models import carlist, showroomlist, review



class carserializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = carlist
        fields = '__all__'
        #fields = ['model', 'id', 'description']
        #exclude = ['name']

#FIELD-LEVEL VALIDATION        
    def get_discounted_price(self, object):
        price = object.price
        if price is not None:
            return price - 5000
        return None

#FIELD-LEVEL VALIDATION 
    def validate_price(self, value):
        if value <=20000:
            raise serializers.ValidationError("Price must be greater than 20000")
        return value

#FIELD-LEVEL VALIDATION     
    def validate_chassisnumber(self, value):
        """
        Check if the chassisnumber is alphanumeric.
        """
        if value and not value.isalnum():
            raise serializers.ValidationError("Chassis number must be alphanumeric")
        return value

#OBJECT-LEVEL VALIDATION   
    def validate(self, data):
        if data['model'] == data['description']:
            raise serializers.ValidationError("Name and description can't be same")
        return data

class reviewserializer(serializers.ModelSerializer):
    car = carserializer(read_only=True)
    class Meta:
        model = review
        fields = ['id','rating','car', 'comments','created','updated']

class GETshowroomserializer(serializers.ModelSerializer):
    cars = carserializer(many=True, read_only = True)
    #cars = serializers.StringRelatedField(many = True)
    #showrooms = serializer.PrimaryKeyRelatedField(many = True, read_only = True)
    #showrooms = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = 'car_detail')
    class Meta:
        model = showroomlist
        fields = '__all__'

class POSTshowroomserializer(serializers.ModelSerializer):
    class Meta:
        model = showroomlist
        fields = '__all__'


class ShowroomSerializer(serializers.ModelSerializer):
    reviews = reviewserializer(many=True, read_only=True)

    class Meta:
        model = showroomlist
        fields = '__all__'

