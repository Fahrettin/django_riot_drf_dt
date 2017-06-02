from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Staff
from app.serializers import StaffSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

# Create your views here.
def home(request):
    return render(request, 'app/example.html')


def staff_list(request):
    if request.method == 'GET':
        stf = Staff.objects.all()
        serial = StaffSerializer(stf, many=True)
        return JsonResponse(serial.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serial = StaffSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status=400)


def staff_detail(request, pk):
    try:
        stf = Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serial = StaffSerializer(stf)
        return JsonResponse(serial.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serial = StaffSerializer(stf, data=data)

        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data)
        return JsonResponse(serial.errors, status=400)

    elif request.method == 'DELETE':
        stf.delete()
        return HttpResponse(status=204)

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
