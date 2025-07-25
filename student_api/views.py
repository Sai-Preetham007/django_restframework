from student_api import models, serializers
from rest_framework.generics import (
    ListAPIView,                              # get
    RetrieveAPIView,                          # get single object by id
    UpdateAPIView,                            # put/patch
    DestroyAPIView,                           # delete
    ListCreateAPIView,                        # get, post
    RetrieveUpdateAPIView,                    # get a single object by id and then u can update by put/patch method
    RetrieveDestroyAPIView,                   # get a single object by id and then u can delete
    RetrieveUpdateDestroyAPIView              # get a single object by id and u can update and also delete
)

class Students_List(ListAPIView):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentSerializer

class Student_by_id(RetrieveAPIView):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentSerializer

class Institute_List_Create(ListCreateAPIView):
    queryset = models.Institute.objects.all()
    serializer_class = serializers.InstituteSerializer

class Institute_Retrieve_Update(RetrieveUpdateAPIView):
    queryset = models.Institute.objects.all()
    serializer_class = serializers.InstituteSerializer

class Institute_Destroy(DestroyAPIView):
    queryset = models.Institute.objects.all()
    serializer_class = serializers.InstituteSerializer