from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import userSerializers
from rest_framework.permissions import IsAuthenticated


class registerUser(APIView):
    def post(self, request):
        serializer = userSerializers(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return responses({"Error" : "Error_Msg"}, status=status.HTTP_400_BAD_REQUEST)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        serializer = userSerializers(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class checkAuthentication(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = "This is working"
        return Response(data, status = status.HTTP_200_OK)


class checkAuthentication2(APIView):

    def get(self, request):
        data = "This is working 2"
        return Response(data, status = status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
