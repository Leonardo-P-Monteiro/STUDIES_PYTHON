from datetime import datetime
from dateutil.relativedelta import relativedelta


value_loan = 1_000_000
date_loan = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
date_final_loan = date_loan + delta_years


list_date_instalment = []
date_instalment = date_loan

while date_instalment < date_final_loan:
    list_date_instalment.append(date_instalment.strftime('%d/%m/%Y'))
    date_instalment += relativedelta(months= 1)


len_date_instalment = len(list_date_instalment)
value_instalment = value_loan / len_date_instalment


for i, j in enumerate(list_date_instalment, start=1):
    print(f'Nº Instalment: {i} |  Date: {j} - Vlaue instalment R${\
value_instalment:,.2f} ')


