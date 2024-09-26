import pytz # To work with time zones especifieds.
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



# strptime()
date_str = '24/09/2024'
date_format = '%d/%m/%Y'
convert_date = datetime.strptime(date_str, date_format)

print('--> Trying the function strptime(): ', convert_date, '\n')

# datetime.now() and pytz lib.

date_now = datetime.now()
timezone_ceara = pytz.timezone('America/Fortaleza')
date_now_tz_ceara = datetime.now(tz=timezone_ceara) 
date_now_tz_ceara = datetime.now().astimezone(timezone_ceara) # Same thing that
# the expression above.


print('--> Trying the function datetime.now() with timezone: ', \
      date_now_tz_ceara, '\n')
print('--> Trying the function datetime.now() without timezone: ', \
      date_now, '\n')


# timedelta

date_tomorrow = date_now + timedelta(days=1)
date_yesterday = date_now - timedelta(days=1)

print(f'--> Operations with timedelta: Tomorrow - {date_tomorrow} | Yesterday: \
{date_yesterday} \n')

# dateutil.relativetimedelta

next_month = date_now + relativedelta(months=1)
passed_month = date_now - relativedelta(month=1)

print(f'--> Operation with dateutil.relativedelta: Next Moth - {next_month} | \
Passed Month - {passed_month} \n')


# .strftime()

brazilian_format_date = '%d/%m/%Y'
brazilian_format_time = '%H:%M:%S'
brazilian_date = datetime.strftime(date_now, brazilian_format_date)
brazilian_time = datetime.strftime(date_now, brazilian_format_time)

print(f'-->Trying the .strformat(): Format brazilian date - {brazilian_date} \
\n')
print(f'-->Trying the .strformat(): Format brazilian time - {brazilian_time} \
\n')