#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils
import logging

# Get the number of running instances
num_running_instances = utils.count_running_instances()

# Function to get running instance detaila
def get_ec2_instance_details():
    # Get information about all EC2 instances
    response = utils.ec2_client.describe_instances()

    if num_running_instances > 10:
        for i in range(10):
            utils.generate_instance_details_list(i)
    else:
        for i in range(0, len(response['Reservations'])):
            utils.generate_instance_details_list(i)


def main():
    """
    Main function.
    """

    try:
        get_ec2_instance_details()

      # Print instance details
        for instance in utils.instance_details:
            print("Instance ID:", instance['InstanceID'])
            print("Instance Type:", instance['InstanceType'])
            print("State:", instance['State'])
            print("Launch Time:", instance['LaunchTime'])
            print("Private IP:", instance['PrivateIP'])
            print("Public IP:", instance['PublicIP'])
            print()
    except:
        logging.exception('')


if __name__ == '__main__':
    main()
