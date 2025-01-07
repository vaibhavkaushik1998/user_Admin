from django.shortcuts import get_object_or_404
from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from user.models import ResUser
from user.serializers import ResUserSerializer, ResAdminUserSerializer
import random


class ResUserRegistrationAPI(generics.GenericAPIView):
    serializer_class = ResUserSerializer
    queryset = ResUser.objects.all()

    def post(self, request):
        """
        Create a new user.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if ResUser.objects.filter(email_id=serializer.validated_data['email_id']).exists():
            return response.Response({"error": "Email is already taken"}, status=status.HTTP_400_BAD_REQUEST)
        if ResUser.objects.filter(mobile_no=serializer.validated_data['mobile_no']).exists():
            return response.Response({"error": "Mobile number is already taken"}, status=status.HTTP_400_BAD_REQUEST)

        username = f"User{random.randint(1000, 9999)}"
        user = serializer.save(username=username)
        user.set_password(serializer.validated_data['password'])
        user.save()

        return response.Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)

    def get(self, request, id=None):
        """
        Retrieve user(s).
        """
        if id:
            user = get_object_or_404(ResUser, id=id)
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            users = ResUser.objects.all()
            serializer = self.serializer_class(users, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """
        Update user details.
        """
        user = get_object_or_404(ResUser, id=id)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        """
        Delete a user.
        """
        user = get_object_or_404(ResUser, id=id)
        user.delete()
        return response.Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class ResAdminAPI(generics.GenericAPIView):
    serializer_class = ResAdminUserSerializer
    queryset = ResUser.objects.all()
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a new admin.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if ResUser.objects.filter(email_id=serializer.validated_data['email_id']).exists():
            return response.Response({"error": "Email is already taken"}, status=status.HTTP_400_BAD_REQUEST)
        if ResUser.objects.filter(mobile_no=serializer.validated_data['mobile_no']).exists():
            return response.Response({"error": "Mobile number is already taken"}, status=status.HTTP_400_BAD_REQUEST)

        username = f"Admin{random.randint(1000, 9999)}"
        admin = serializer.save(username=username)
        admin.set_password(serializer.validated_data['password'])
        admin.save()

        return response.Response(self.serializer_class(admin).data, status=status.HTTP_201_CREATED)

    def get(self, request, id=None):
        """
        Retrieve admin(s).
        """
        if id:
            admin = get_object_or_404(ResUser, id=id)
            serializer = self.serializer_class(admin)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            admins = ResUser.objects.all()
            serializer = self.serializer_class(admins, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """
        Update admin details.
        """
        admin = get_object_or_404(ResUser, id=id)
        serializer = self.serializer_class(admin, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        """
        Delete an admin.
        """
        admin = get_object_or_404(ResUser, id=id)
        admin.delete()
        return response.Response({"message": "Admin deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
