#!/usr/bin/env python3
'''Lab 3 Part 2 script - free disk space'''
# Author ID: ssuresh14

import subprocess

def free_space():
    # Run the disk free command
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = process.communicate()
    # Decode and strip newlines
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
