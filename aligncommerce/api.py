from datetime import datetime, date
from urllib import urlencode
import apirequest
import session
import sys
import json
import time

class Api():

	_GRANT_TYPE = 'client_credentials'
	_SCOPE 		= 'products,buyer,invoice'

	def __init__(self, *args):
		self.username  	= args[0]
		self.password 	= args[1]
		self.client_id  = args[2]
		self.secret_key = args[3]

		self.session = session.Session(self.client_id)

		res = self.checkSession()
		
		self.access_token 	= res[0]
		self.expiry			= res[2]

		is_expired = self.isTokenExpired()

		""" Request new access token and store it in session """
		if ( is_expired ):
			self.getAccessToken()

	def checkSession(self):
		self.session = session.Session(self.client_id)

		if( self.session.get(self.client_id) ):
			""" Get access token from session """
			res = self.session.get(self.client_id)
		else:
			self.getAccessToken()
			res = self.session.get(self.client_id)

		return res

	def getAccessToken(self):
		""" Request new access token and save in session """
		method	= 'POST'
		url 	= 'oauth/access_token'
		param 	= {
			'client_id' 	: self.client_id,
			'client_secret' : self.secret_key,
			'grant_type' 	: self._GRANT_TYPE,
			'scope' 		: self._SCOPE
		}
		res = apirequest.ApiCall(self.username, self.password).call(method, url, param)
		self.session.create(json.loads(res))

	def isTokenExpired(self):
		""" Check if access token is expired (expiry date is in timestamp format)"""
		expiry  = datetime.fromtimestamp(int(self.expiry))
		now     = datetime.fromtimestamp(int(time.time()))

		return expiry < now

	def buyerList(self):
		data 	= {'access_token' : self.access_token}
		method	= 'GET'
		url 	= 'buyer/?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url)

	def buyerInfo(self, buyer_id):
		data 	= {'access_token' : self.access_token}
		method	= 'GET'
		url 	= 'buyer/' + buyer_id + '?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url)

	def invoiceList(self):
		data 	= {'access_token' : self.access_token}
		method	= 'GET'
		url 	= 'invoice/?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url)

	def invoiceInfo(self, invoice_id):
		data 	= {'access_token' : self.access_token}
		method	= 'GET'
		url 	= 'invoice/' + invoice_id + '?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url)

	def invoiceCreate(self, data):
		data['access_token'] = self.access_token
		method	= 'POST'
		url 	= 'invoice/'
		return apirequest.ApiCall(self.username, self.password).call(method, url, data)

	def productList(self):
		data 	= {'access_token' : self.access_token}
		method	= 'GET'
		url 	= 'products/?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url)

	def productInfo(self, product_id):
		data 	= {'access_token' : self.access_token}
		method	= 'GET'
		url 	= 'products/' + product_id + '?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url)

	def productUpdate(self, product_id, data):
		data['access_token'] = self.access_token
		method	= 'PUT'
		url 	= 'products/' + product_id + '?' + urlencode(data)
		return apirequest.ApiCall(self.username, self.password).call(method, url, data)

	def productCreate(self, data):
		data['access_token'] = self.access_token
		method	= 'POST'
		url 	= 'products/'
		return apirequest.ApiCall(self.username, self.password).call(method, url, data)