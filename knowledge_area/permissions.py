from rest_framework import permissions


class Knowledge_areaPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('Knowledge_areas.view_Knowledge_area')

        if request.method == 'POST':
            return request.user.has_perm('Knowledge_areas.add_Knowledge_area')

        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('Knowledge_areas.change_Knowledge_area')

        if request.method == 'DELETE':
            return request.user.has_perm('Knowledge_areas.delete_Knowledge_area')

        return False