from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework import status
from  django.contrib.auth.models import User 
from  .serializers import UserRegistrSerializer , UserSerialzer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class UserRegister(APIView):
    def post(self , request ):
        ser_data=UserRegistrSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data , status=status.HTTP_201_CREATED)
        return Response(ser_data.errors , status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated,]
    queryset = User.objects.all()

    def list(self,request):
        srz_data = UserSerialzer(instance = self.queryset , many=True)
        return Response(data=srz_data.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset , pk=pk )
        srz_data=UserSerialzer(instance=user)
        return Response(data=srz_data.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        srz_data = UserSerialzer(instance=user, data=request.POST , partial =True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset,pk=pk)
        user.is_active =False
        user.save()
        return Response ({'message' : 'user deactivated'})

    # username=ser_data.validated_data['username'],
    # email=ser_data.validated_data['email'],
    # password=ser_data.validated_data['password'])


