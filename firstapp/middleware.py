from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

class BlackListMiddleware(MiddlewareMixin):

    IP_BLACK_LIST = [
        '127.0.0.2',
    ]

    def process_view(self,request,*args, **kwargs):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        if ip in self.IP_BLACK_LIST:
            raise PermissionDenied()