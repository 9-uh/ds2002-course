#!/usr/bin/env python3

import boto3
s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-xak2wm'

local_file = 'bear.jpg'
with open(local_file, 'rb') as image:
    s3.put_object(
        Body = image,
        Bucket = bucket,
        Key = local_file
    )

public_file = 'cat.jpg'
with open(public_file, 'rb') as image:
    response = s3.put_object(
        Body = image,
        Bucket = bucket,
        Key = public_file,
        ACL = 'public-read',
    )


