import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda v3!')
    }

# no-op change to test GHA workflow
# yet another change