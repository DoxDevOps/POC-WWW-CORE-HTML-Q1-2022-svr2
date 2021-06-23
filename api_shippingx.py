import os
import urllib.request
import json
import platform
import subprocess

# define URL to capture data
url = 'http://10.44.0.52/sites/api/v1/get_single_cluster/3'
req = urllib.request.Request(url)

# parsing response
r = urllib.request.urlopen(req).read()
xi_api = json.loads(r.decode('utf-8'))

for site_id in all_sites_in_cluster:
    site_endpoint = "http://10.44.0.52/sites/api/v1/get_single_site/" + str(site_id)
    site_req = urllib.request.Request(site_endpoint)
    site_r = urllib.request.urlopen(site_req).read()
    site_details = json.loads(site_r.decode('utf-8'))

    sitex = site_details[0]['fields']
    for sitex in xi_api['cluster']:
        param = '-n' if platform.system().lower()=='windows' else '-c'
        if subprocess.call(['ping', param, '1', sitex['ip']]) == 0:
            push_api = "rsync " + "-r ssh $WORKSPACE/BHT-EMR-API/ " + sitex['user'] + "@" + sitex['ip'] + ":~/var/www/BHT-EMR-API"
            os.system(push_api)
            run_api_script = "ssh " + sitex['user'] + "@" + sitex['ip'] + " 'cd /var/www/BHT-EMR-API && ./api_setup.sh"
            os.system(run_api_script)
