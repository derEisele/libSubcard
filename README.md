libsubcard
===========

A unofficial API for (at the moment german) Subcard.
This API is NOT affiliated with Subway IP Inc. or any of it's services. Subcard and Subway are registerd trademarks of Subway IP Inc.

This API is created by reverse engeneering the official Subcard android App.

## Installation

### Pip

`pip install git+https://github.com/derEisele/libSubcard.git`

## Usage
```
>>> from libsubcard import Subcard
>>> s = Subcard("email@example.com", "MySecretPassword")
>>> s.getLoyaltyBalance()
180
>>> s.getCardNumber()
6308750935126253
>>> s.getLast10Transac()
{'transaction0': {'date': '07-10-2017', 'merchant': 'Hamburg [12345]', 'transType': 'Loyalty Allocation', 'value': 0.0, 'points': 180}, 'transaction1': {'date': '07-10-2017', 'merchant': 'Hamburg [12345]', 'transType': 'Purchase', 'value': 27.06, 'points': 0}, 'transaction2': {'date': '07-10-2017', 'merchant': 'Hamburg [12345]', 'transType': 'Balance Enquiry', 'value': 0.0, 'points': 0}} 
```
## Questions
### What is the code in the Subcard App?
A compact Aztec Code containing the card number

## Todo
* Add other countries
* Port this API to Java/Android to create an open source App
