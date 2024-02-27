#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3

# Initialize EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# function to count number of running instances
def count_running_instances():
    # Get information about all EC2 instances
    response = ec2_client.describe_instances()

    running_instances = 0

    # Iterate over reservations and instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Check if the instance is in the running state
            if instance['State']['Name'] == 'running':
                running_instances += 1

    return running_instances


# Initialize list to hold instance details
instance_details = []

# Function to populate instance details list
def generate_instance_details_list(i):
    response = ec2_client.describe_instances()
    instance_id = response['Reservations'][i]['Instances'][0]['InstanceId']
    instance_type = response['Reservations'][i]['Instances'][0]['InstanceType']
    instance_state = response['Reservations'][i]['Instances'][0]['State']['Name']
    instance_launch_time = response['Reservations'][i]['Instances'][0]['LaunchTime'].strftime(
        "%Y-%m-%d %H:%M:%S")
    instance_private_ip = response['Reservations'][i]['Instances'][0][
        'PrivateIpAddress'] if 'PrivateIpAddress' in response['Reservations'][i]['Instances'][0] else 'N/A'
    instance_public_ip = response['Reservations'][i]['Instances'][0][
        'PublicIpAddress'] if 'PublicIpAddress' in response['Reservations'][i]['Instances'][0] else 'N/A'

    # Append instance details to the list
    instance_details.append({
        'InstanceID': instance_id,
        'InstanceType': instance_type,
        'State': instance_state,
        'LaunchTime': instance_launch_time,
        'PrivateIP': instance_private_ip,
        'PublicIP': instance_public_ip
    })
    return instance_details
