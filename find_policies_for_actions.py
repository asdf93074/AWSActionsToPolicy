import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

path_to_actions_to_policies = 'D:\\scripts\\node_scripts\\python\\actions_to_policies.json'

actions_to_find = [
    "ec2:DescribeInternetGateways",
    "ec2:DescribeNatGateways",
    "ec2:DescribeNetworkAcls",
    "ec2:DescribeVpcs",
    "ec2:DescribeSubnets",
    "ec2:DescribeTags",
    "ec2:DescribeSecurityGroups",
    "ec2:DescribeNetworkInterfaceAttribute",
    "ec2:DescribeNetworkInterfacePermissions",
    "ec2:DescribeNetworkInterfaces",
    "ec2:DescribePrefixLists",
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

actions_to_policies = json.loads(open(path_to_actions_to_policies, 'r').read())

policies_counter = {}

def find_policies_for_actions():
    for action_to_find in actions_to_find:
        for policy in actions_to_policies[action_to_find]:
            if (policy not in policies_counter):
                policies_counter[policy] = 0
            
            policies_counter[policy] = policies_counter[policy] + 1

if __name__ == '__main__':
    print(len(actions_to_find), '\n')

    find_policies_for_actions()

    pp.pprint(policies_counter)

