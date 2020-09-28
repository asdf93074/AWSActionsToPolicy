import boto3
import json
import threading

path_to_policies = 'list_of_all_managed_policies.json'

iam = boto3.resource('iam')

with open(path_to_policies, 'rb') as policies_file:
    policies = json.loads(policies_file.read())

policy_versions = []
actionsToPolicies = {}
insertionLock = threading.Lock()

def create_actions_to_policies(start, offset):
    for i in range(start, len(policies['Policies']), offset):
        policy = policies['Policies'][i]
        
        actions = []
        document = iam.PolicyVersion(policy['Arn'], policy['DefaultVersionId']).document

        if (isinstance(document['Statement'], list)):
            for x in document['Statement']:
                if (isinstance(x['Action'], list)):
                    actions.extend(x['Action'])
                else:
                    actions.append(x['Action'])
        elif (isinstance(document['Statement'], dict)):
            actions.extend(document['Statement']['Action'])

        print(policy['PolicyName'], actions,'\n')

        if (isinstance(actions[0], list)):
            print(document)

        insertionLock.acquire()
        for action in actions:
            action = str(action).lower()
            if (action not in actionsToPolicies):
                actionsToPolicies[action] = set()

            actionsToPolicies[action].add(policy['PolicyName'])

        insertionLock.release()

if __name__ == '__main__':
    threads = []
    threadsCount = 10

    for i in range(threadsCount):
        threads.append(threading.Thread(target=create_actions_to_policies, args=(i,threadsCount)))

    for i in range(threadsCount):
        threads[i].start()

    for i in range(threadsCount):
        threads[i].join()

    for i in actionsToPolicies:
        actionsToPolicies[i] = list(actionsToPolicies[i])

    with open('actions_to_policies.json', 'w+') as a:
        a.write(json.dumps(actionsToPolicies))