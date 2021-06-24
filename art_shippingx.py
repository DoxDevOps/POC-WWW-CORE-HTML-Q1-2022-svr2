import requests
import json
import platform
import subprocess
import os

def get_xi_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    data = data[0]['fields']
    return data

cluster = get_xi_data('http://10.44.0.52/sites/api/v1/get_single_cluster/3')

for site_id in cluster['site']:
    site = get_xi_data('http://10.44.0.52/sites/api/v1/get_single_site/' + str(site_id))

    # lets check if the site is available
    param = '-n' if platform.system().lower()=='windows' else '-c'
    if subprocess.call(['ping', param, '1', site['ip_address']]) == 0:
        
        # ship data to remote site
        push_art = "rsync " + "-r $WORKSPACE/BHT-Core/apps/ART/ " + site['username'] + "@" + site['ip_address'] + ":/var/www/BHT-Core/apps"
        os.system(push_art)

        # run setup script
        run_api_script = "ssh " + site['username'] + "@" + site['ip_address'] + " 'cd /var/www/BHT-Core && ./core_art_setup.sh'"
        os.system(run_api_script)




