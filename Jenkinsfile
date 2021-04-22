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

    stage('Remote Server Backup') {
      steps {
        sh '''#Mzuzu Macro
#ssh linserver@10.40.30.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.30.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.30.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Chitipa DHO
#ssh linserver@10.40.22.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.22.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.22.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Karonga DHO
#ssh linserver@10.40.26.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.26.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.26.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Dowa DHO
#ssh meduser@10.41.172.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.41.172.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.41.172.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Rumphi DHO
#ssh linserver@10.2.12.10 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.2.12.10 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.2.12.10 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Chintheche Rural Hospital
#ssh linserver@10.40.51.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.51.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.51.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Kasungu DHO
#ssh meduser@10.41.156.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.41.156.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.41.156.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Nkhotakota DHO
#ssh meduser@10.40.8.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.40.8.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.40.8.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Salima DHO
#ssh meduser@10.41.154.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.41.154.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.41.154.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Mzuzu Central
#ssh linserver@10.40.11.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.11.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.11.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\''''
      }
    }

    stage('Shipping') {
      parallel {
        stage('API') {
          steps {
            echo 'Copying & configuring ART'
          }
        }

        stage('Core') {
          steps {
            echo 'Checking if OPD is deployed on new architecture'
          }
        }

      }
    }

    stage('New Architecture Apps') {
      parallel {
        stage('ART') {
          steps {
            echo 'Shiping ART'
          }
        }

        stage('ANC') {
          steps {
            echo 'Configuring ANC'
          }
        }

        stage('HTS') {
          steps {
            echo 'Configuring HTS '
          }
        }

        stage('TB') {
          steps {
            echo 'Configaring TB'
          }
        }

        stage('OPD') {
          steps {
            echo 'Configuring OPD'
          }
        }

      }
    }

    stage('Loading Metadata') {
      steps {
        echo 'Loading Metadata'
      }
    }

  }
}