from urllib.request import urlopen
import json
import datetime

today = datetime.date.today().strftime('%d-%m-%Y')

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter?center_id=603439&date="+str(today)

response = urlopen(url)

data = json.loads(response.read())

available_dose_count = 0
total_available_dose_count = 0

for session in data['centers']['sessions']:
    total_available_dose_count+=(int(session['available_capacity']))
    if(session['min_age_limit']==18):
        available_dose_count+=int(session['available_capacity_dose1'])

print("18+ Available Doses in Apollo - "+ str(available_dose_count))
print("Total Available Doses in Apollo - "+ str(total_available_dose_count))