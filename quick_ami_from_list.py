#!/usr/bin/python

import boto3
import datetime

import quick_ami_from_list_config

region = quick_ami_from_list_config.region
profile = quick_ami_from_list_config.profile
no_reboot = quick_ami_from_list_config.no_reboot
instance_list = quick_ami_from_list_config.instances
description = quick_ami_from_list_config.description
time_string = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

try:
    aws = boto3.Session(profile_name=profile, region_name=region)
    ec2_client = aws.client('ec2')
    ec2_resource = aws.resource('ec2')
except:
    raise


for instance in instance_list:
    ami_name = instance + "_" + time_string
    name_filter = [{
        'Name': 'tag:Name',
        'Values': [instance]
    }]
    try:
        res_collection = ec2_resource.instances.filter(Filters=name_filter)
        for res in res_collection:
            instance_id = res.id
        print "Found instance {} with id {}\n".format(instance, instance_id)
        response = ec2_client.create_image(
            InstanceId=instance_id,
            Name=ami_name,
            Description=description,
            NoReboot=no_reboot
        )
        print "Created image for {} with id {}\n".format(instance, response['ImageId'])
    except:
        raise
