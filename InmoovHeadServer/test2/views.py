import time
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from test2.models import Robot
from test2.serializer import RobotSerializer

from test2.term import SerialCom


def home(request):
	bonjour = "BONJOUR"
	listUser = ["pierre", "paul", "jean", "blabla"]
	"""robot = Robot()
	robot.name = "test"
	robot.serialNumer = "12345"
	robot.save()"""
	robots = Robot.objects.all()
	return render(request, 'index.html', locals())


"""class RobotList(APIView):
	def get(self, request, format=None):
		robots = Robot.objects.all()
		serializer = RobotSerializer(robots, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = RobotSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

class RobotViewSet(viewsets.ModelViewSet):
	queryset = Robot.objects.all()
	serializer_class = RobotSerializer

@api_view(['POST'])
def apiArduino(request):
	print(request.data)

	command = request.POST.get("command", "error")

	print(command)

	if str(command) != "error":
		serialCom = SerialCom(1, "serialThread")

		serialCom.daemon = True
		serialCom.start()

		time.sleep(3)

		serialCom.write(bytes(command, "utf-8"))

		time.sleep(1)

		serialCom.closeSerial()

		return Response(status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)