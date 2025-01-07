from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ResUser(AbstractUser):
    """
    Custom user model extending AbstractUser.
    """
    Role_Choice = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('craftsman', 'Craftsman'),
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('accountant', 'Accountant'),
    ]
    USER_ROLES = [
        ('internal', 'Internal'),
        ('external', 'External'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    # User details
    role_name = models.CharField(max_length=50, choices=Role_Choice, default='super_admin', verbose_name="Role Name")
    role = models.CharField(max_length=50, choices=USER_ROLES, default='internal', verbose_name="Role Type")
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    mobile_no = models.CharField(max_length=15, verbose_name="Mobile Number")
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Company Name")
    price_slab = models.CharField(max_length=255, blank=True, null=True, verbose_name="Price Slab")
    email_id = models.EmailField(verbose_name="Email ID", unique=True)
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Country")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="State")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="City")
    pincode = models.CharField(max_length=10, blank=True, null=True, verbose_name="Pincode")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Status")
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Gender")
    profile_picture = models.ImageField(upload_to='User/Profile', blank=True, null=True, verbose_name="Profile Picture")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    # Permissions fields
    view_only = models.BooleanField(default=False, verbose_name="View Only")
    copy = models.BooleanField(default=False, verbose_name="Copy")
    print_perm = models.BooleanField(default=False, verbose_name="Print")
    download = models.BooleanField(default=False, verbose_name="Download")
    share = models.BooleanField(default=False, verbose_name="Share")
    screenshots = models.BooleanField(default=False, verbose_name="Screenshots")
    edit = models.BooleanField(default=False, verbose_name="Edit")
    delete = models.BooleanField(default=False, verbose_name="Delete")
    manage_roles = models.BooleanField(default=False, verbose_name="Manage Roles")
    approve = models.BooleanField(default=False, verbose_name="Approve")
    reject = models.BooleanField(default=False, verbose_name="Reject")
    archive = models.BooleanField(default=False, verbose_name="Archive")
    restore = models.BooleanField(default=False, verbose_name="Restore")
    transfer = models.BooleanField(default=False, verbose_name="Transfer")
    custom_access = models.BooleanField(default=False, verbose_name="Custom Access")
    full_control = models.BooleanField(default=False, verbose_name="Full Control")
    view_perm = models.BooleanField(default=False, verbose_name="Can View")
    add_perm = models.BooleanField(default=False, verbose_name="Can Add")
    update_perm = models.BooleanField(default=False, verbose_name="Can Update")
    delete_perm = models.BooleanField(default=False, verbose_name="Can Delete")

    def __str__(self):
        return self.full_name
