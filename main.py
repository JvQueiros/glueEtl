import os
import json
import boto3


with open('config.json') as config:
    conf = json.load(config)

s3 = boto3.client('s3',region_name = 'us-east-2',
                   aws_access_key_id = conf['aws_access_key_id'], 
                   aws_secret_access_key = conf['aws_secret_access_key'])


buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]


if 'jv-glue-proj' not in buckets:
    s3.create_bucket(Bucket='jv-glue-proj', 
                     CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})



for file in os.listdir(conf['uri']):
    s3.upload_file(
        Filename = f'{os.path.join(conf['uri'], file)}',
        Bucket = 'jv-glue-proj',
        Key = f'{file}')