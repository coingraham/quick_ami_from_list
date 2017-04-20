#!/usr/bin/python

# Whether you want the AMI creation to reboot or not.
# no_reboot = False  # This will cause instances to reboot.
no_reboot = True  # This will cause instance to NOT reboot.

# Profile you are referencing for authentication
# profile = "firstwatch"  # for local testing
profile = "CCNA_BI_NONPROD_Admin"

# Region you want to run in.
# region = "us-east-1"  # for local testing
region = "us-west-2"

# Description that you want for each AMI
description = "Backup for migration image"

# Comma delimited array of quoted instance names to take AMI images.
instances = ["CWDJDEA5001","CWDJDEA5011","CWDJDEA5012","CWDJDEA5013","CWDJDEA5014","CWDJDEA5015"]