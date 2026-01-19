import json

def lambda_handler(event, context):
    # TODO implement
    name = event.get('name')
    if not name:
        parems = event.get('queryStringParameters',{})
        name = parems.get('name','world')

    return {
        'statusCode': 200,
        'body': f"Hello {name}"
    }
