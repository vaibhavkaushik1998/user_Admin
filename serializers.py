from rest_framework import serializers
from user.models import ResUser

class ResUserSerializer(serializers.ModelSerializer):
    """
    Serializer for ResUser model for basic user details.
    """

    class Meta:
        model = ResUser
        fields = [
            'id', 'profile_picture', 'full_name', 'mobile_no', 'email_id',
            'password', 'role', 'role_name', 'company_name', 'price_slab',
            'country', 'state', 'city', 'pincode', 'status',
            'dob', 'gender', 'view_only', 'copy', 'print_perm', 'download', 
            'share', 'screenshots', 'edit', 'delete', 'manage_roles', 
            'approve', 'reject', 'archive', 'restore', 'transfer', 
            'custom_access', 'full_control', 'view_perm', 'add_perm', 
            'update_perm', 'delete_perm'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Override the create method to create a new ResUser instance.
        """
        password = validated_data.pop('password', None)
        user = ResUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Override the update method to update an existing ResUser instance.
        """
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ResAdminUserSerializer(serializers.ModelSerializer):
    """
    Serializer for ResUser model with admin-level permissions included.
    """

    class Meta:
        model = ResUser
        fields = [
            'id', 'profile_picture', 'full_name', 'mobile_no', 'email_id',
            'password', 'role', 'role_name', 'company_name', 'price_slab',
            'country', 'state', 'city', 'pincode', 'status',
            'dob', 'gender', 'view_only', 'copy', 'print_perm', 'download', 
            'share', 'screenshots', 'edit', 'delete', 'manage_roles', 
            'approve', 'reject', 'archive', 'restore', 'transfer', 
            'custom_access', 'full_control', 'view_perm', 'add_perm', 
            'update_perm', 'delete_perm'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Override the create method for admin-specific user creation.
        """
        password = validated_data.pop('password', None)
        user = ResUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Override the update method for admin-specific user updates.
        """
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
