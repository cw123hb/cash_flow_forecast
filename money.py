import datetime
import cashflow
# A=Annualy M=Monthly Q=Quarterly W=Weekly D=Daily

cf = cashflow.CashFlow('Cash flow forecast')

#Generate data
cf.add_event('Original balance', 50000, datetime.date(2022, 4, 15))

cf.generate_series('Monthly salary', 13360, frequency='M', start=datetime.date(2022, 6, 1), end=datetime.date(2022,12,31))
cf.generate_series('Monthly rent', -5400, frequency='M', start=datetime.date(2022, 6, 1), end=datetime.date(2022,12,31))
cf.generate_series('Monthly insurance', -400, frequency='M', start=datetime.date(2022, 8, 1), end=datetime.date(2022,12,31))  
cf.generate_series('Food', -1500, frequency='W', start=datetime.date(2022, 5, 21), end=datetime.date(2022,12,31)) 
cf.add_event('One off payment', -3000, datetime.date(2022, 8, 20))   
cf.generate_series('Food', -1500, frequency='W', start=datetime.date(2022, 5, 21), end=datetime.date(2022,12,31))
# 
#Show the data
print(cf.series)
cf.export_to_csv('', '2022.csv')
cf.export_to_png('', '2022.png')
