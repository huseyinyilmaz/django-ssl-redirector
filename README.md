# django-sslredirector
A simple django application that manages http/https statuses of different views.  

## Installation

1. Add "sslredirector.middleware.SSLMiddleware" middleware on top of setttings.MIDDLEWARE_CLASSES.
2. set settings.DEFAULT_SSL_BEHIVIOUR variable with one of the following values sslredirector.middleware.NATURAL, sslredirector.middleware.FORCE\_SECURE
sslredirector.middleware.FORCE\_UNSECURE.  Default value will be FORCE\_UNSECURE
3. if you need to disable ssl redirection ( you might want to disable it for local development.), set settings.SSL\_ENABLED variable to False. Default value will be True.

## Usage

After installation, You can force views to use ssl by decorating them with  sslredirector.decorators.secure_required decorator, if you need views to use http, use sslredirector.decorators.unsecure_required decorator.
