import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
ddb_table = dynamodb.Table('usersTable')

def trigger(event, context):
    for record in event['Records']:
        for key in record:
            if key == 'awsRegion':
                awsRegion = record[key]
            if key == 'eventTime':
                eventTime = record[key]                
            if key == 's3':
                for i in record[key]:
                    if i == 'bucket':
                        bucketname = record[key][i]['name']
                    if i == 'object':
                        objectkey =  record[key][i]['key']
            print("%s:%s"%(key,record[key]))
    ddb_table.put_item( Item={ 'bucketname' : bucketname, 'objectkey' : objectkey, 'awsRegion' : awsRegion, 'eventTime' : eventTime} )
    return "%s,%s,%s,%s"%(bucketname,objectkey,awsRegion,eventTime)