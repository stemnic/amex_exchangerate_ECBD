import os, json
import pandas as pd
import matplotlib.pyplot as plt

path_to_json = '/home/stemnic/scripts/amex_exchange'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

jsons_data_eur = pd.DataFrame(columns=['date', 'percentage'])
jsons_data_usd = pd.DataFrame(columns=['date', 'percentage'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        
        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        date = pd.to_datetime(js.split(".json")[0], format='%Y-%m-%d')
        try:
            currency = json_text["Norway"]
            percentage = json_text["Norway"][32]["Total percentage variance versus ECB Consumer"]
            jsons_data_eur.loc[index] = [date, percentage]

            percentage = json_text["Norway"][0]["Total percentage variance versus ECB Consumer"]
            jsons_data_usd.loc[index] = [date, percentage]
        except:
            try:
                percentage = json_text[0]['consumer'][32]['percentageVariance']
                jsons_data_eur.loc[index] = [date, percentage]

                percentage = json_text[0]['consumer'][0]['percentageVariance']
                jsons_data_usd.loc[index] = [date, percentage]
            except:
                print(json_file.name + "  " + json_text["code"])

jsons_data_eur['percentage'] =jsons_data_eur['percentage'].str.rstrip('%').astype('float') #/ 100.0
jsons_data_usd['percentage'] =jsons_data_usd['percentage'].str.rstrip('%').astype('float') #/ 100.0

start_date  = '2020-01-01'
end_date    = '2030-01-01'

jsons_data_eur = jsons_data_eur.sort_values(by="date")
jsons_data_usd = jsons_data_usd.sort_values(by="date")

mask = (jsons_data_eur['date'] > start_date) & (jsons_data_eur['date'] <= end_date)
jsons_data_eur = jsons_data_eur.loc[mask]

mask = (jsons_data_usd['date'] > start_date) & (jsons_data_usd['date'] <= end_date)
jsons_data_usd = jsons_data_usd.loc[mask]



print("EUR")
#print(jsons_data_eur)
print(jsons_data_eur.describe())

print("USD")
#print(jsons_data_usd)
print(jsons_data_usd.describe())

plt.xticks(rotation=90)
plt.plot(jsons_data_eur['date'], jsons_data_eur['percentage'])
plt.tight_layout()
#plt.xticks(rotation='vertical')
plt.savefig('/home/stemnic/scripts/amex_exchange/data_eur.png')

plt.figure()

plt.xticks(rotation=90)
plt.plot(jsons_data_usd['date'], jsons_data_usd['percentage'])
plt.tight_layout()
#plt.xticks(rotation='vertical')
plt.savefig('/home/stemnic/scripts/amex_exchange/data_usd.png')