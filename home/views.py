from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import PersonSerializer
from home.models import Person

@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'topics' : ['flask', 'Django', 'Tornado', 'FastApi'],
        'course_provider' : 'Scaler'
    }

    if request.method == "GET":
        print("You hit the 'GET' method.")

    elif request.method == "POST":
        print("You hit the 'POST' method.")
        data = request.data
        print("---------------------------")
        print(data)
        print("---------------------------")

    elif request.method == "PUT":
        print("You hit the 'PUT' method.")

    return Response(courses)



@api_view(["GEt", "POST", "PUT", "PATCH", "DELETE"])
def person(request):
    if request.method == "GET":
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method =="PUT":
        data = request.data
        obj = Person.objects.get(id = data["id"])
        serializer = PersonSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         
    elif request.method =="PATCH":
        data = request.data
        obj = Person.objects.get(id = data["id"])
        serializer = PersonSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    else:
        data = request.data
        obj = Person.objects.get(id = data["id"])
        obj.delete()
        return Response({f"message" : "Person deleted"})