align-python-library
====================

## Align Commerce Python Library ##

### Usage ###
```python
> from aligncommerce import api
```
###### Retrieve list ######
```
> print api.invoiceList()
```
###### Get info ######
```
> print api.invoiceInfo('<invoice id>')
```
###### Create ######
```
> create_invoice_data = {
	'currency' : '<currency>',
	'checkout_type' : '<btc/bank_transfer>',
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

> print api.invoiceCreate(create_invoice_data)
```
