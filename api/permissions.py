from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message="You are not the owner or a Staff Member"
	def has_object_permission(self, request, view, obj):
		if request.user == obj.owner or request.user.is_staff:
			return True
		return False