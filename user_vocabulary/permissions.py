# class IsCreationOrIsAuthenticated(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated():
#             if view.action == 'create':
#                 return True
#             else:
#                 return False
#         else:
#             return True
#
#
# class IsEditAction(BasePermission):
#     def has_edit_permission(self, request, view):
#         return bool(request.user and request.user.is_staff)