import boto3
import json

path_to_policies = 'D:\\scripts\\node_scripts\\python\\list_of_all_managed_policies.json'

iam = boto3.resource('iam')

with open(path_to_policies, 'rb') as policies_file:
    policies = json.loads(policies_file.read())

policy_versions = []
actionsToPolicies = {}

for policy in policies['Policies']:
    print(policy['PolicyName'], '\n')

    actions = []
    document = iam.PolicyVersion(policy['Arn'], policy['DefaultVersionId']).document

    try:
        if (len(document['Statement']) == 1):
            actions = document['Statement'][0]['Action']
        elif (len(document['Statement']) > 1):
            for i in document['Statement']:
                if ('Action' in i.keys()):
                    actions.extend(i['Action'])
    except:
        actions = document['Statement']['Action']

    for action in actions:
        if (action not in actionsToPolicies):
            actionsToPolicies[action] = []
        
        actionsToPolicies[action].append(policy['PolicyName'])

print(actionsToPolicies)

with open('actions_to_policies.json', 'w+') as a:
    a.write(json.dumps(actionsToPolicies))
    