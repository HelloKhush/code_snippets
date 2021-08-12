import requests
import pandas as pd
import csv
url = "https://api.covid19api.com/summary"
def Get_Json(url):
    response_info = requests.get(url).json()
    
    country_list = []
    for country_info in response_info['Countries']:
        country_list.append([country_info['Country'], country_info['TotalConfirmed']])
        
        
    header = ['Country', 'Total_Confirmed']
    #country_df = pd.DataFrame(data=country_list, columns=['Country', 'Total_Confirmed'])
    #print(country_df.head(10))
    
    with open('output.csv', 'w') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(country_list)

if __name__ == "__main__":
    Get_Json(url)
