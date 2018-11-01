"""A unofficial lib for subcard data"""

import requests
from uuid import uuid4
from time import strftime, gmtime


class Subcard(object):
    """Request subcard data."""

    _BASE_URL = "https://subcard{}.altaineapps.com/gateway2/api/Gateway/"

    def __init__(self, email, password, country_code="de"):
        """Request subcard data for an account.

        It's apparently not necessary to change the country code to match the account, but hey it's only 2 letters...
        Tested country codes are:
        - de
        - uk
        - at
        - nl
        """
        self._UUID = str(uuid4())
        self._data = self._requestData(email, password, country_code)

    def _requestData(self, email, password, country_code):
        """Request account data. Returns as a dict."""
        t = strftime("%Y%m%d%H%M%S", gmtime())
        self._TOKEN = t + "ASDadb6233"  # Some sort of magic, but it works.

        payload = {"Password": password,
                   "ProgramId": "6",
                   "EmailAddress": email,
                   "Udid": self._UUID,
                   "Platform": "Android",
                   "Version": "5.1",
                   "Token": self._TOKEN}

        r = requests.post(self._BASE_URL.format(country_code) + "GetCardDetails", json=payload)

        return r.json()

    def getLoyaltyBalance(self):
        """Return Subcard points."""
        points = self._data.get('TraderEnquiryResponse')\
                           .get('traderBalances')\
                           .get('loyaltyBalance')
        return int(points)

    def getLast10Transac(self):
        """Return last 10 transactions."""
        return self._data.get('TraderEnquiryResponse')\
                         .get('traderLast10Transac')

    def getCardNumber(self):
        """Return virtual card number."""
        card = self._data.get('TraderEnquiryResponse')\
                         .get('virtualCard')
        return int(card)
