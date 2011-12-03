from django.conf import settings
from django.http import get_host,HttpResponsePermanentRedirect

"""
This middleware can be enabled by settings variable
SSL_ENABLED variable.

In settings.py file default behivour can be set
with DEFAULT_SSL_BEHIVIOUR variable. Value of this variable
can be one of the following

Default way of finding out if connection is secure is using
SERVER_PORT header. if your server does not use default port 443
for ssl, or if your server does not somehow has SERVER_PORT header.
user settings.SSL_HEADER and settings.SSL_HEADER_VALUE variables to
set which header shows if we are on secure connection
"""


###################################
# DEFAULT SSL BEHIVIOUR CONSTANTS #
###################################


NATURAL = 0
"""
Undecorated views will not be redirected
"""

FORCE_SECURE = 1
"""
Undecorated views will be redirect to https
if they are not on https already
"""


FORCE_UNSECURE = 2
"""
Undecorated views will be redirect to http
if they are not on http already
This is the default behivour
"""


class SSLMiddleware(object):

    def __init__(self):
        self.DEFAULT_SSL_BEHIVIOUR = getattr(settings,'DEFAULT_SSL_BEHIVIOUR',FORCE_UNSECURE)
        self.SSL_ENABLED = getattr(settings,'SSL_ENABLED',True)
        self.SSL_HEADER = getattr(settings,'SSL_HEADER','SERVER_PORT')
        self.SSL_HEADER_VALUE = getattr(settings,'SSL_HEADER_VALUE','443')

        
    def _redirect(self, request, is_secure):
        """
        Gets request and is_secure parameters. if is_secure
        parameter is True, returns redirection to https version of
        same url. If is_secure is false returns a redirection to http version
        of same url
        (I took this method from http://djangosnippets.org/snippets/240/)
        """
        protocol = is_secure and "https" or "http"
        url = "%s://%s%s" % (protocol,get_host(request),request.get_full_path())
        if settings.DEBUG and request.method == 'POST':
            raise RuntimeError, \
"""Django can't perform a SSL redirect while maintaining POST data.
Please structure your views so that redirects only occur during GETs."""
        return HttpResponsePermanentRedirect(url)
    
                                                                                                                                                                                                                     
    def process_view(self, request, view_func, view_args, view_kwargs):
        # if ssl is not enabled do not run this middleware
        if not  self.SSL_ENABLED:
            return None
            
        # decide what view behivour should be
        view_behiviour = getattr(view_func,'ssl_behiviour',self.DEFAULT_SSL_BEHIVIOUR)
        # if view_behiviour is truthy value (which means it is not 0-NATURAL)
        if view_behiviour:
            """
            Our request can be secure if request.is_secure is True or SSL_HEADER is equal to SSL_HEADER_VALUE.
            Default SSL_HEADER is "SERVER_PORT" and default SSL_HEADER_VALUE = 443. So if request is on port 443
            we can say that our request is on secure connection. You can use different header for your system. For
            instance, if you are on Webfaction you might want to use "HTTP_X_FORWARDED_SSL" as SSL_HEADER and "on" as SSL_HEADER_VALUE
            If none of those methods work for you, set a header from your web server and use that custom header for those values.
            """
            is_ssl_request = request.is_secure() or request.META[self.SSL_HEADER] == str(self.SSL_HEADER_VALUE)

            """
            At this point view_behiviour can be FORCE_SECURE or FORCE_UNSECURE.
            we already eliminated NATURAL value by if statement.
            So if it is FORCE_SECURE, our view demanding connection to be secure.
            """
            is_ssl_view = view_behiviour == FORCE_SECURE

            #if view and request security does not match redirect response
            if is_ssl_request != is_ssl_view:
                return self._redirect(request,is_ssl_view)
            
            
