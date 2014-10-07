from urllib import urlencode
import session
import pycurl
import urllib
import sys
import json
import cStringIO

class ApiCall():

	_API_URL 	= 'https://api.aligncommerce.com/'
	_GRANT_TYPE = 'client_credentials'
	_SCOPE 		= 'products,buyer,invoice'

	def __init__(self, *args):
		self.username = args[0]
		self.password = args[1]

		self.headers = []
		self.options = []
		self.curl 	 = ''

	def call(self, method, url, data=None):
		url = self._API_URL + url

		res = cStringIO.StringIO()
		self.curl = pycurl.Curl()

		self.curl.setopt(pycurl.VERBOSE, 0)
		self.curl.setopt(pycurl.USERPWD, self.username + ':' + self.password)
		self.curl.setopt(pycurl.URL, url)
		self.curl.setopt(pycurl.FOLLOWLOCATION, True)
		self.curl.setopt(self.curl.WRITEFUNCTION, res.write)

		self.setRequestMethod(method, data)

		self.curl.perform()
		self.curl.close()
		return res.getvalue()

	def setRequestMethod(self, method, data=None):
		""" Set request method """
		if( method == 'GET' ):
			self.curl.setopt(pycurl.HTTPGET, True)

		elif( method == 'POST' ):
			data = json.dumps(data)

			self.curl.setopt(pycurl.CUSTOMREQUEST, method)
			self.curl.setopt(pycurl.POST, True)
			self.curl.setopt(pycurl.POSTREDIR,3)
			self.curl.setopt(pycurl.POSTFIELDS, data)
			self.curl.setopt(pycurl.HTTPHEADER, [
				'Accept: application/json',
				'Content-Type: application/json; charset=utf-8',
				'Connection: Keep-Alive'])

		elif( method == 'PUT' ):
			data = json.dumps(data)

			self.curl.setopt(pycurl.CUSTOMREQUEST, method)
			self.curl.setopt(pycurl.POST, True)
			self.curl.setopt(pycurl.POSTFIELDS, data)
			self.curl.setopt(pycurl.HTTPHEADER, [
				'Accept: application/json',
				'Content-Type: application/json; charset=utf-8',
				'Connection: Keep-Alive'])

		elif( method == 'DELETE' ):
			self.curl.setopt(pycurl.CUSTOMREQUEST, method)