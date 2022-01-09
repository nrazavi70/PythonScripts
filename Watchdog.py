import requests
import json
import datetime

# Defining required parameters such as token, target record, target URL and etc.
token="Apikey 66b2bf03-d992-523a-9b7b-e486ad27eb59"
target_record_name="hc"
primary_server_ip="77.238.111.137"
secondary_server_ip="5.6.7.8"
target_url="https://core.gapfilm.ir"
print(open("active_server", "r").read())
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

# Requesting the list of DNS records in Gapfilm.ir domain.
get_dns_list_url="https://napi.arvancloud.com/cdn/4.0/domains/"+"gapfilm.ir"+"/dns-records"
dns_list_response=requests.get(get_dns_list_url,headers={'Authorization':'Apikey '+token})
parsed_dns_list=json.loads(dns_list_response.text)

# Finding the ID of the DNS record we want to change in case of server failure.
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
target_record_id=findRecordID(target_record_name)

# Defining variables to check the target website and applying changes in case of failure.
dns_record_change_url="https://napi.arvancloud.com/cdn/4.0/domains/gapfilm.ir/dns-records/"+target_record_id
target_response=requests.get(target_url)
if target_response.status_code == 200 and open("active_server", "r").read() == "secondary":
  requests.put(dns_record_change_url, headers={'Authorization':token, 'Content-Type':'application/json'}, data=dns_record_change_to_primary_body)
  open("active_server", "w").write("primary")
  print(str(datetime.datetime.now())+" : The active web server for "+target_url+" is now redirected at "+primary_server_ip)

elif target_response.status_code == 200 and open("active_server", "r").read() == "primary":
  print(str(datetime.datetime.now())+" : The primary server is up.")

elif target_response.status_code != 200 and open("active_server", "r").read() == "primary":
  requests.put(dns_record_change_url, headers={'Authorization':token, 'Content-Type':'application/json'}, data=dns_record_change_to_secondary_body)
  open("active_server", "w").write("secondary")
  print(str(datetime.datetime.now())+" : The active web server for "+target_url+" is now redirected at "+secondary_server_ip)

else:
  print(str(str(datetime.datetime.now()))+" : Check servers' statuses!")