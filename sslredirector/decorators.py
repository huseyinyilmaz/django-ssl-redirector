from middleware import FORCE_SECURE, FORCE_UNSECURE


def secure_required(view_func):
    """
    Sets ssl_behiviour attribute of view_function.
    This attribute will be used in SSL middleware to
    decide if request should be redirected to https
    if it is on http.

    Note:

    This decorator must be on top of all other
    decorators in order to work.
    
    Usage:
    
    @secure_required
    def viewmethod(request):
        ....
        return response
    """
    view_func.ssl_behiviour = FORCE_SECURE
    return view_func


def unsecure_required(view_func):
    """
    Sets ssl_behiviour attribute of view_function.
    This attribute will be used in SSL middleware to
    decide if request should be redirected to http
    if it is on https.

    Note:

    This decorator must be on top of all other
    decorators in order to work.

    Usage:
    
    @unsecure_required
    def viewmethod(request):
        ....
        return response
    """
    view_func.ssl_behiviour = FORCE_UNSECURE
    return view_func



