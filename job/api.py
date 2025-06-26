from .models import JOB
from .serializers import JobSerializer
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework import generics



## function based views
@api_view(['GET'])
def job_list_api(request):
    all_jobs = JOB.objects.all()
    data = JobSerializer(all_jobs , many = True).data

    return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = JOB.objects.get(id=id)
    data = JobSerializer(job_detail).data

    return Response({'data':data})

## class based views(geniric views)

class JobListApi(generics.ListCreateAPIView):
    queryset = JOB.objects.all()
    serializer_class = JobSerializer

class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = JOB.objects.all()
    lookup_field = 'id'