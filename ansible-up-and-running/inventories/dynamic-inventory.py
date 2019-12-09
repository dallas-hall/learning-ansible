#!/usr/bin/env python
import argparse
import json
import subprocess
import sys
import paramiko
import re


debugging = False


def parse_args():
    parser = argparse.ArgumentParser(description="Dynamic Vagrant inventory script.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list",action='store_true')
    group.add_argument("--host")
    return parser.parse_args()


def list_running_hosts():
    cmd = "vagrant status --machine-readable"
    status = subprocess.check_output(cmd.split()).rstrip()
    hosts = []
    if debugging:
        print(status)
        print()
        print(status.decode("utf-8"))
        print()
        print(status.decode("utf-8").split("\n"))

    regex = re.compile(r"File exists.*")
    for line in status.decode("utf-8").split("\n"):
        # Skip the vagrant debug line
        vagrant_debug_line = regex.search(line)
        if vagrant_debug_line:
            continue
        (_, host, key, value) = line.split(',')[:4]
        if key == "state" and value == "running":
            hosts.append(host)
    return hosts


def get_host_details(host):
    if debugging:
        print(host)
    cmd = "vagrant ssh-config {}".format(host)
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    config = paramiko.SSHConfig()
    config.parse(p.stdout)
    c = config.lookup(host)
    return {
        "ansible_host": c["hostname"],
        "ansible_port": c["port"],
        "ansible_user": c["user"],
        "ansible_private_key_file": c["identityfile"][0]
    }


def main():
    args = parse_args()
    if args.list:
        hosts = list_running_hosts()
        json.dump({"vagrant": hosts}, sys.stdout)
    elif args.host:
        details = get_host_details(args.host)
        json.dump(details, sys.stdout)


if __name__ == "__main__":
    main()
