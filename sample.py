from aligncommerce import api

username 	= ''
password	= ''
client_id  	= ''
secret_key 	= ''

api = api.Api( username, password, client_id, secret_key )

""" BUYER """
# print api.buyerList()
# print api.buyerInfo('<buyer_id>')

""" INVOICE """
create_invoice_data = {
	'currency' : '',
	'checkout_type' : '',
	'products' : [{
		'product_name' 		: '',
		'product_price' 	: '',
		'quantity' 			: '',
		'product_shipping' 	: ''
	}],
	'buyer_info'	: {
		'first_name' : '',
		'last_name'  : '',
		'email'		 : '',
		'address_1'  : '',
		'address_2'  : ''
	}
}
# print api.invoiceList()
# print api.invoiceInfo('<invoice_id>')
# print api.invoiceCreate(create_invoice_data)

""" PRODUCTS """
create_product_data = {
	'product_name' 			: '',
	'product_description'	: '',
	'product_price' 		: ,
	'product_shipping' 		: 
}
# print api.productList()
# print api.productInfo('Zfp4dWqWrFSHBw2rvPmB')
# print api.productCreate(create_product_data)
# print api.productUpdate('Zfp4dWqWrFSHBw2rvPmB',create_product_data)

