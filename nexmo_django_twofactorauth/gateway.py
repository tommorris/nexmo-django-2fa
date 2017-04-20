from __future__ import absolute_import

from django.conf import settings
from django.utils import translation
from django.utils.translation import pgettext, ugettext
from nexmo import Client

from two_factor.middleware.threadlocals import get_current_request

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse  # < django 1.10

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Nexmo(object):
    """
    Gateway for sending text messages and making phone calls using Nexmo_.

    You need your Nexmo account credentials, and a registered app 
    account dashboard.

    ``NEXMO_API_KEY``
      Should be set to your account's API key from the Dashboard.

    ``NEXMO_API_SECRET``
      Should be set to your account's authorization token.

    ``NEXMO_CALLER_ID``
      The name of the service to text through.

    .. _Nexmo: https://www.nexmo.com/
    """
    def __init__(self):
        self.client = Client(getattr(settings, 'NEXMO_API_KEY'),
                             getattr(settings, 'NEXMO_API_SECRET'))

    # def make_call(self, device, token):

    def send_sms(self, device, token):
        body = ugettext('Your authentication token is %s') % token
        opts = {}
        opts['to'] = device.number.as_e164,
        opts['from'] = getattr(settings, 'NEXMO_CALLER_ID') or 'DjangoApp'
        opts['body'] = body
        self.client.send_message(opts)
