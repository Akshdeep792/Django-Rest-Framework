from .permissions import IsStaffEditorPermission
from rest_framework import permissions
class StaffEditorPermissionMixix():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]