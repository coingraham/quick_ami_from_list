#!/usr/bin/python

# Whether you want the AMI creation to reboot or not.
# no_reboot = False  # This will cause instances to reboot.
no_reboot = True  # This will cause instance to NOT reboot.

# Profile you are referencing for authentication
# profile = "firstwatch"  # for local testing
profile = "008733_USEECTest_MSP"

# Region you want to run in.
# region = "us-east-1"  # for local testing
region = "us-east-1"

# Description that you want for each AMI
description = "Backup for migration image"

# Tag to use for identification
tag = "host_name"

# Comma delimited array of quoted instance names to take AMI images.
instances = ["cwdhaxw0003"]