import boto3
import json

path_to_policies = 'D:/Scripts/node_scripts/python/list_of_all_managed_policies.json'

iam = boto3.resource('iam')
policies = json.load(path_to_policies)
print(len(policies))

policy_version = iam.PolicyVersion()