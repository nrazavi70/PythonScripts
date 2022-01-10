export WATCHDOG_TOKEN=
export DOMAIN_NAME=
export TARGET_RECORD=
export TARGET_URL=
export PRIMARY_SERVER_IP=
export SECONDARY_SERVER_IP=

while (true)
do
        python3.8 /etc/watchdog/watchdog.py
        echo ---------------------------
        sleep 300
done