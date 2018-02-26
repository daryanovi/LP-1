price = 100
vat_rate = 18
def get_vat(price):
	try:
		price=float(price)
		vat = price/100*vat_rate
		price_no_vat=price-vat
		return round(price_no_vat, 2)
	except (TypeError, ValueError):
		print('Не могу посчитать')



result=get_vat(453.5)
print("Сумма НДС {}".format(result))

def get_summ(one, two, delimeter=' '):
    result=str(one) + str(delimeter) + str(two)
    return result.upper()
   
print(get_summ('Hello', 'world!', delimeter='&'))
print(get_summ('Hello', 'world!', ' + '))
print(get_summ('Hello', 'world!'))