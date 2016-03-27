import time, cPickle, requests, ConfigParser

import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

from publicAPIs import getLatLon, getWeather
from database.postgres import getQuery

#Skip loading the data below by setting use_API = False in settings.cfg
config = ConfigParser.RawConfigParser()
config.read('settings.cfg')
use_API = config.getboolean('Main', 'use_API')

if use_API:
    invoices = getQuery('select * from "Invoice"')


    invoices_supp = []
    for index, invoice in enumerate(invoices):
        if index%25==0:
            print index
        location = str(invoice[4])+', '+str(invoice[6])+' '+str(invoice[7])
        new_row = list(invoice)
        new_row.append(getLatLon(location))
        invoices_supp.append(new_row)
        time.sleep(1)

    del invoices

    for index, row in enumerate(invoices_supp):
        if index%25==0:
            print index
        app = getWeather(row[2], row[-1])
        row.append(app)
        time.sleep(1)

else:
    with open('./weather_data.cpickle') as infile:
        invoices_supp = cPickle.load(infile)

column_names = ['invoice_id', 'customer_id', 'invoice_date', 'billing_address', 'billing_city', 'billing_state',
                'billing_country', 'billing_postal_code', 'total', 'latlon', 'weather_json'
               ]

def weather_states(weather_desc):
    if 'rain' in weather_desc.lower():
        return 'Rain'
    elif 'snow' in weather_desc.lower() or 'sleet' in weather_desc.lower():
        return 'Snow'
    elif 'sun' in weather_desc.lower():
        return 'Sun'
    else:
        return 'Clouds'

df = pd.DataFrame(invoices_supp, columns=column_names)
df.total = df.total.astype(float)
df['weather_desc'] = df.weather_json.apply(lambda x: x['data']['weather'][0]['hourly'][0]['weatherDesc'][0]['value'])
df['weather_state'] = df.weather_desc.apply(lambda x: weather_states(x))
df['precipitation'] = df.weather_json.apply(lambda x: float(x['data']['weather'][0]['hourly'][0]['precipMM']))
df['FeelsLikeF'] = df.weather_json.apply(lambda x: float(x['data']['weather'][0]['hourly'][0]['FeelsLikeF']))

print "Count of Each Weather State:"
print pd.value_counts(df.weather_state)

fig, ax = plt.subplots(figsize=(8, 8))
plot = sb.violinplot(x='weather_state', y='total', data=df, ax=ax)
fig.savefig('mean_diff.png')

df[['total', 'precipitation', 'FeelsLikeF']].corr()

gb = df.groupby(['invoice_date', 'latlon']).agg({'total': sum, 'precipitation': np.mean, 'FeelsLikeF': np.mean})
g = sb.PairGrid(gb, diag_sharey=False)
g.map_lower(sb.kdeplot, cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sb.kdeplot, lw=3)
g.savefig('correlations.png')

df.to_csv('final_data.csv')

print 'Plots exported to root directory as mean_diff.png and correlations.png'
print 'Data exported to root directory as final_data.csv'
