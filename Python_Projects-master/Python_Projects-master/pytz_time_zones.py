import  pytz
from datetime import datetime

country_zones = ['America/New_York', 'Asia/Kolkata', 'Australia/Sydney',
                'Canada/Atlantic', 'Brazil/East','Chile/EasterIsland', 'Cuba', 'Egypt',
                'Europe/Amsterdam', 'Europe/Athens', 'Europe/Berlin', 'Europe/Istanbul',
                'Europe/Jersey', 'Europe/London', 'Europe/Moscow', 'Europe/Paris', 
                'Europe/Rome', 'Hongkong', 'Iceland', 'Indian/Maldives', 'Iran',
                'Israel', 'Japan', 'NZ', 'US/Alaska', 'US/Arizona', 'US/Central', 
                'US/East-Indiana', 'Europe/Istanbul', 'Turkey']

country_time_zones = []

for x in country_zones:
    country_time_zones.append(pytz.timezone(x))
for i in range(len(country_time_zones)):
    country_time = datetime.now(country_time_zones[i])
    print(f"The time of {country_zones[i]} is {country_time.strftime('Date is %d-%m-%y and Time is  %H:%M:%S')}")

