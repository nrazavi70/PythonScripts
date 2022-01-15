import requests
import json
import datetime
import os
from time import sleep

#Defining required parameters such as token, target record, target URL and etc.
token=str(os.environ.get('WATCHDOG_TOKEN'))
domain_name=str(os.environ.get('DOMAIN_NAME'))
target_record_name=str(os.environ.get('TARGET_RECORD'))
target_url=str(os.environ.get('TARGET_URL'))
primary_server_ip=str(os.environ.get('PRIMARY_SERVER_IP'))
secondary_server_ip=str(os.environ.get('SECONDARY_SERVER_IP'))

dns_record_change_to_primary_body = json.dumps({
  "type": "a",
  "name": target_record_name,
  "value": [
    {
      "ip": primary_server_ip,
      "port": 1,
      "weight": 0,
      "country": "US"
    }
  ],
  "ttl": 120,
  "cloud": True,
  "upstream_https": "default",
  "ip_filter_mode": {
    "count": "single",
    "order": "none",
    "geo_filter": "none"
  }
})
dns_record_change_to_secondary_body = json.dumps({
  "type": "a",
  "name": target_record_name,
  "value": [
    {
      "ip": secondary_server_ip,
      "port": 1,
      "weight": 0,
      "country": "US"
    }
  ],
  "ttl": 120,
  "cloud": True,
  "upstream_https": "default",
  "ip_filter_mode": {
    "count": "single",
    "order": "none",
    "geo_filter": "none"
  }
})

# Requesting the list of DNS records in set domain.
get_dns_list_url="https://napi.arvancloud.com/cdn/4.0/domains/"+domain_name+"/dns-records"
dns_list_response=requests.get(get_dns_list_url,headers={'Authorization':'Apikey '+token})
parsed_dns_list=json.loads(dns_list_response.text)

# Finding the ID and IP of the DNS record we want to change in case of server failure.
def findRecordID(record_name):
    for i in range(len(parsed_dns_list['data'])):
        if parsed_dns_list['data'][i]['name'] == record_name:
            record_id = parsed_dns_list['data'][i]['id']
            break
        else:
            record_id = 'undefined'        
    if record_id == 'undefined':
        print(str(datetime.datetime.now())+" : No such record exists.")
    else:
        return record_id
def findRecordIP(record_name):
    for i in range(len(parsed_dns_list['data'])):
        if parsed_dns_list['data'][i]['name'] == record_name:
            record_ip = parsed_dns_list['data'][i]['value'][0]['ip']
            break
        else:
            record_ip = 'undefined'        
    if record_ip == 'undefined':
        print(str(datetime.datetime.now())+" : No such record exists.")
    else:
        return record_ip
target_record_id=findRecordID(target_record_name)
target_record_ip=findRecordIP(target_record_name)

# Defining variables to check the target website and applying changes in case of failure.
dns_record_change_url="https://napi.arvancloud.com/cdn/4.0/domains/"+domain_name+"/dns-records/"+target_record_id
target_response=requests.get(target_url)

if target_response.status_code == 200 and target_record_ip == secondary_server_ip:
  failures = 0
  while target_response.status_code == 200:
    failures += 1
    if failures == 3:
      requests.put(dns_record_change_url, headers={'Authorization':token, 'Content-Type':'application/json'}, data=dns_record_change_to_primary_body)
      print(str(datetime.datetime.now())+" : The active web server for "+target_url+" is now redirected to the primary server at "+primary_server_ip+" .")
      break
    sleep(30)

elif target_response.status_code == 200 and target_record_ip == primary_server_ip:
  print(str(datetime.datetime.now())+" : The primary server is up at "+primary_server_ip+" .")

elif target_response.status_code != 200 and target_record_ip == primary_server_ip:
  failures = 0
  while target_response.status_code != 200:
    failures += 1
    if failures == 3:
      requests.put(dns_record_change_url, headers={'Authorization':token, 'Content-Type':'application/json'}, data=dns_record_change_to_secondary_body)
      print(str(datetime.datetime.now())+" : The active web server for "+target_url+" is now redirected to the secondary server at "+secondary_server_ip+" .")
      break
    sleep(30)

else:
  print(str(str(datetime.datetime.now()))+" : Check servers' statuses!")