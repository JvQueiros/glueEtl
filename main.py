import os
import json
import boto3 as b3


with open('config.json') as conf:
    config = json.load(conf)

uri = config['uri']

s3 = b3.connect('s3',
                region_name = 'code_region',
                aws_access_key_id = key723474r
                aws_secret_access_key = asdfasdf

)


for file in uri:
