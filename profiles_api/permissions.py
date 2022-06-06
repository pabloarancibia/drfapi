from rest_framework import permissions 

class UpdateOwnProfile(permissions.BasePermission):
    ''' permite al usuario editar su perfil '''

    def has_object_permission(self, request, view, obj):
        ''' chequear si el usuario tiene permiso '''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id