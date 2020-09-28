import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

path_to_actions_to_policies = 'actions_to_policies.json'

# example actions that you're looking for
actions_to_find = [
    "ec2:DescribeInternetGateways",
    "ec2:DescribeNetworkAcls",
    "ec2:DescribeVpcs",
    "ec2:DescribeSubnets",
    "ec2:DescribeTags",
    "ec2:DescribeSecurityGroups",
    "ec2:DescribeNetworkInterfaces",
    "ec2:DescribeRouteTables",
    "ec2:CreateRoute",
    "ec2:DetachInternetGateway",
    "ec2:CreateTags",
    "ec2:AuthorizeSecurityGroupIngress",
    "ec2:AuthorizeSecurityGroupEgress",
    "ec2:DeleteKeyPair",
    "ec2:AttachInternetGateway",
    "ec2:CreateKeyPair",
    "ec2:RunInstances",
    "ec2:DescribeInstanceStatus",
    "ec2:TerminateInstances",
    "ec2:StopInstances",
    "ec2:StartInstances"
]

for i in range(len(actions_to_find)):
    actions_to_find[i] = str(actions_to_find[i]).lower()

actions_to_find.sort()

actions_to_policies = json.loads(open(path_to_actions_to_policies, 'r').read())

policies_counter = {}
actions_counter = {}

def find_policies_for_actions():
    for action_to_find in actions_to_find:
        for policy in actions_to_policies[action_to_find]:
            if (policy not in policies_counter):
                policies_counter[policy] = {
                    'Counter': 0,
                    'Actions': [],
                }
            
            policies_counter[policy]['Counter'] = policies_counter[policy]['Counter'] + 1
            policies_counter[policy]['Actions'].append(action_to_find)
            
            if (action_to_find not in actions_counter):
                actions_counter[action_to_find] = 0
            
            actions_counter[action_to_find] = actions_counter[action_to_find] + 1

def find_sets_with_all_actions():
    solutions = set()

    for x in policies_counter:
        for y in policies_counter:
            actionsSet = set()

            actionsSet.update(policies_counter[x]['Actions'])
            actionsSet.update(policies_counter[y]['Actions'])

            if (len(actionsSet) == len(actions_to_find)):
                if ({x,y} not in solutions):
                    solutions.add(frozenset((x,y)))

    print(len(solutions), solutions)

if __name__ == '__main__':
    print('Number of actions to find: ', len(actions_to_find), '\n')

    find_policies_for_actions()
    find_sets_with_all_actions()

