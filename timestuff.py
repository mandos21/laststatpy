from datetime import date, timedelta,datetime
import time

def yesterday_midnight():
	today = datetime.now()
	yesterday = (today - timedelta(days=1)) - timedelta(hours=today.hour,seconds=today.second,minutes=today.minute)
	midnight = yesterday + timedelta(hours=23,minutes=59,seconds=59)

	p = "%d.%m.%Y %H:%M:%S"
	d = midnight.strftime(p)

	epoch = int(time.mktime(time.strptime(d,p)))
	return epoch

def week_ago():
	today = datetime.now()	
	yesterday = (today - timedelta(days=7)) - timedelta(hours=today.hour,seconds=today.second,minutes=today.minute)
	midnight = yesterday + timedelta(hours=23, minutes=59, seconds=59)

	p =" %d.%m.%Y %H:%M:%S"
	d = midnight.strftime(p)	

	epoch = int(time.mktime(time.strptime(d,p)))
	return epoch
