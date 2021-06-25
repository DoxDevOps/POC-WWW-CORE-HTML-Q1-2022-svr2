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
        
        # shipping backup script
        push_backup_script = "rsync " + "-r $WORKSPACE/devops_api_backup.sh " + site['username'] + "@" + site['ip_address'] + ":/var/www"
        os.system(push_backup_script)
        
        # backing up application folder [API]
        backup_script = "ssh " + site['username'] + "@" + site['ip_address'] + " 'cd /var/www && chmod 777 devops_api_backup.sh && ./devops_api_backup.sh'"
        os.system(backup_script)
        
        # ship data to remote site
        push_api = "rsync " + "-r $WORKSPACE/BHT-EMR-API " + site['username'] + "@" + site['ip_address'] + ":/var/www"
        os.system(push_api)
        
        # run setup script
        run_api_script = "ssh " + site['username'] + "@" + site['ip_address'] + " 'cd /var/www/BHT-EMR-API && ./api_setup.sh'"
        os.system(run_api_script)






