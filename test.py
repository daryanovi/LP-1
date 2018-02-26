a=[2,3,4,5,6,7]
print(a)
a.append('PYTHON')
print(a)
print(a[0])
x=len(a)
print(a[x-1])
print(a[2:5])
print(len(a))
print(a.index(6))
a.remove('PYTHON')
print(a)


weather={
	'city': 'Москва', 
	'temperature':20, 
	'wind':'восточный'
}
print(weather['city'])
print(len(weather))
print(weather.get('country'))
weather['date']='21.02.2018'
print(weather)

forecast=[weather]
print(forecast)
forecast.append({
	'city': 'Москва', 
	'temperature':19, 
	'wind':'северо-восточный'
	})
forecast.append({
	'city': 'Москва', 
	'temperature':25, 
	'wind':'южный'
})
forecast.append({
	'city': 'Москва', 
	'temperature':30, 
	'wind':'южный'
})
print(forecast)