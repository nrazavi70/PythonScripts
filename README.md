# Project Title

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [About <a name = "about"></a>](#about-)
  - [Getting Started <a name = "getting_started"></a>](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)

## About <a name = "about"></a>

The following project simply checks a URL for HTTP 200 response code and changes DNS records when the primary server is down and switches it back when the primary comes back up.

## Getting Started <a name = "getting_started"></a>

To use the project just follow the guide below at [Installing](#installing).

### Prerequisites

You only need python3 on the server you are installing this.


### Installing

There are five simple steps to install this.  
  
  1. Clone the repo and switch to ```SimpleURLWatchdog``` branch :
   ```
   git clone git@github.com:nrazavi70/PythonScripts.git
   cd PythonScripts
   git checkout SimpleURLWatchdog
   ```
  2. Edit ``` watchdog.sh ``` and fill your data in front of the empty environmental variables.
   ```
   nano ./watchdog.sh
   ```
 
 | Variable Key        | Variable Value                                                           |
|---------------------|--------------------------------------------------------------------------|
| WATCHDOG_TOKEN      | A token with DNS record read/write access on the target domain.          |
| DOMAIN_NAME         | The domain name of the record you want to be changed in case of failure. |
| TARGET_RECORD       | The record name of the record you want to be changed in case of failure. |
| TARGET_URL          | The URL of the health check site.                                        |
| PRIMARY_SERVER_IP   | The IP address of your primary server.                                   |
| SECONDARY_SERVER_IP | The IP address of your secondary server.                                 |

  3. Create watchdog directories in ```/etc/``` and ```/var/log/```.
   ```
    sudo mkdir /etc/watchdog
    sudo mkdir /var/log/watchdog
   ```
  4. Make all 3 files executable and then copy ``` watchdog.sh ``` and ``` watchdog.py ``` from git direcrectory to ```/etc/watchdog/```.
  ```
  chmod +x ./watchdog.*
  sudo cp ./watchdog.sh ./watchdog.py /etc/watchdog/
  ```
  5. Copy ```watchdog.service``` to ```/etc/systemd/system/``` and reload systemd daemon then start and enable the service.
  ```
  sudo cp watchdog.service /etc/systemd/system/
  sudo systemctl daemon-reload
  sudo systemctl start watchdog.service
  sudo systemctl enable watchdog.service
  ``` 
