from rest_framework import serializers
from home.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    
    def validate(self, data):
        spl_char = "!@#$%^&*()_-+=~`{[]}:;',.?/\|<>"

        if any(i in spl_char for i in data["name"]):
            raise serializers.ValidationError("'Name' should not contain any special characters.")
        
        if data["age"] < 18:
            raise serializers.ValidationError("'Age' must be greater than 18.")

        return data