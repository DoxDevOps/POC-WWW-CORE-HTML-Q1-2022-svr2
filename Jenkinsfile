pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing ...'
        sh 'echo "Working from $WORKSPACE"'
      }
    }

    stage('Fetching Repos') {
      parallel {
        stage('Fetching API') {
          steps {
            echo 'Starting to fetch API from GitHub'
            echo 'Checking if BHT-EMR-API exists.'
            sh '[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git'
            echo 'Giving access to all users'
            sh 'cd $WORKSPACE && chmod 777 BHT-EMR-API'
            echo 'Fetching Tags'
            sh 'cd $WORKSPACE/BHT-EMR-API && git fetch --tags -f'
            echo 'Checking out to Latest Tag'
            sh 'cd $WORKSPACE/BHT-EMR-API && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-EMR-API && git describe > HEAD'
          }
        }

        stage('Fetching Core') {
          steps {
            echo 'Starting to fetch Core from GitHub'
            echo 'Checking if BHT-Core exists.'
            sh '[ -d "BHT-Core" ] && echo "Core already cloned." || git clone https://github.com/HISMalawi/BHT-Core.git'
            echo 'Giving access to users'
            sh 'cd $WORKSPACE && chmod 777 BHT-Core'
            echo 'Fetching New Tags'
            sh 'cd $WORKSPACE/BHT-Core && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-Core && git describe $(git describe --tags `git rev-list --tags --max-count=1`)'
          }
        }

        stage('Fetching ART') {
          steps {
            echo 'Starting to fetch ART from GitHub'
            echo 'Checking if BHT-Core-Apps-ART exists.'
            sh '[ -d "ART" ] && echo "ART already cloned." || git clone https://github.com/HISMalawi/BHT-Core-Apps-ART.git ART'
            echo 'Giving access to all user'
            sh 'cd $WORKSPACE && chmod 777 ART'
            echo 'Fetching new tags'
            sh 'cd $WORKSPACE/ART && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/ART && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/ART && git describe > HEAD'
          }
        }

      }
    }

    stage('Remote server backup') {
      steps {
        sh '''#Test Server
#ssh egpaf@10.8.0.50 \'cd /var/www/ && mkdir Apps_Backup\'
#ssh egpaf@10.8.0.50 \'mv /var/www/BHT-Core/apps/ART/ /var/www/Apps_Backup\'
'''
      }
    }

    stage('Remote Server Configation and Shipping') {
      parallel {
        stage('Core') {
          steps {
            echo 'No testing functionality found....'
            sh '''#Opsuser
#BHT-Core
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core && git fetch --tags -f git://10.44.0.51/var/lib/jenkins/workspace/art-setup-no-container_master/BHT-Core\'

#rsync -a --exclude \'config\' $WORKSPACE/BHT-Core opsuser@10.44.0.52:/home/opsuser/poc_test/BHT-Core
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core && git checkout v4.7.8\'
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core && git describe > HEAD\'

#Test Server
#rsync -a --update $WORKSPACE/BHT-Core egpaf@10.8.0.50:/var/www/BHT-Core
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-Core && git checkout v4.7.8\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-Core && git describe > HEAD\''''
          }
        }

        stage('ART') {
          steps {
            echo 'Copying and configuration ART'
            sh '''#Opsuser
#BHT-Core
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core/apps/ART && git fetch --tags -f git://10.44.0.51/var/lib/jenkins/workspace/art-setup-no-container_master/BHT-Core-Apps-ART\'

#rsync -a --exclude \'*.json\' $WORKSPACE/ART opsuser@10.44.0.52:/home/opsuser/poc_test/BHT-Core/apps/ART
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core/apps/ART && git checkout v4.11.3\'
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core/apps/ART && git describe > HEAD\'

#Test Server
rsync -a $WORKSPACE/ART egpaf@10.8.0.50:/var/www/BHT-Core/apps
ssh egpaf@10.8.0.50 \'cp /var/www/Apps_Backup/ART/application.json /var/www/BHT-Core/apps/ART\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-Core/apps/ART && git checkout v4.11.3\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-Core/apps/ART && git describe > HEAD\''''
          }
        }

        stage('API') {
          steps {
            echo 'Copying and configuring API'
            sh '''#Opsuser
#BHT-EMR-API
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-EMR-API && git fetch --tags -f git://10.44.0.51/var/lib/jenkins/workspace/art-setup-no-container_master/BHT-EMR-API\'

#rsync -a --exclude \'config\' $WORKSPACE/BHT-EMR-API opsuser@10.44.0.52:/home/opsuser/poc_test/BHT-EMR-API
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-EMR-API && git checkout v4.10.25\'
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-EMR-API && git describe > HEAD\'

#Test Server
#rsync -a --update $WORKSPACE/BHT-EMR-API/.git egpaf@10.8.0.50:/var/www/BHT-EMR-API
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-EMR-API && git checkout v4.10.25\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-EMR-API && git describe > HEAD\''''
          }
        }

      }
    }

    stage('Loading metada to remote server') {
      steps {
        sh '''#Test Server
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-EMR-API && mysql -uroot -proot openmrs < db/sql/openmrs_metadata_1_7.sql\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-EMR-API && mysql -uroot -proot openmrs < db/sql/moh_regimens_v2020.sql\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-EMR-API && mysql -uroot -proot openmrs < db/sql/bart2_views_schema_additions.sql\'
#ssh egpaf@10.8.0.50 \'cd /var/www/BHT-EMR-API && mysql -uroot -proot openmrs < db/sql/alternative_drug_names.sql\''''
      }
    }

  }
}