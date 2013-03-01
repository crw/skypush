import sys
import json
import time

import requests

import config

app_key = config.app_key
master_secret = config.master_secret
alias = 'crw'
uri = 'https://go.urbanairship.com/api/push/'

log_file = 'C:\Users\crw\Documents\My Games\Skyrim\Logs\Script\User\PushLog.0.log'

push_message = 'Skyrim: Craig checked in to {}.'


def send_push(message, alias=None, dryrun=False):
    content = {}
    if alias:
        content['aliases'] = [alias]
    content['aps'] = {
        "badge": "+1",
        "alert": message,
        "sounds": "cat.caf",
    }
    headers = {'Content-type': 'application/json'}
    if not dryrun:
        resp = requests.post(
            uri, 
            auth=(app_key, master_secret), 
            data=json.dumps(content),
            headers=headers
        )
    if alias is None:
        alias = 'everybody'

    print 'Sent push "{}" to {}.'.format(message, alias)
    if not dryrun:
        print "{} {}".format(resp.status_code, resp.text)


def watch_log_file(log_file, dryrun=False):
    last_line = ''
    cur_line = ''

    while True:
        logFile = open(log_file, 'r')
        for line in logFile:
            cur_line = line.strip()
        logFile.close()

        if last_line != cur_line:
            last_line = cur_line
            print "Sending {}".format(cur_line)
            if cur_line[26:45] == '[SkyPush][Location]':
                message = push_message.format(cur_line[46:])
                send_push(message, alias, dryrun=dryrun)
        cur_line = ''
        time.sleep(5)


if __name__ == '__main__':
    dryrun = False
    if len(sys.argv) > 1:
        dryrun = sys.argv[1] == 'dryrun'
    watch_log_file(log_file, dryrun)
