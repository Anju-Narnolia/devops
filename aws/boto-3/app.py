import boto3
from dotenv import load_dotenv
import os

load_dotenv()
aws_access_id=os.getenv('aws_access_id')
aws_access_key=os.getenv('aws_access_key')

#create an s3 client 
# s3 = boto3.resource('s3',aws_access_key_id = aws_access_id ,aws_secret_access_key = aws_access_key)

# call an s3 client to get all bucket
# for bucket in s3.buckets.all():
    # print(bucket.name)

# Bucket_Name='anju-narnolia-1804'

#add bucket
# s3.create_bucket(
#     Bucket=Bucket_Name,
#     CreateBucketConfiguration={'LocationConstraint':'ap-south-1'}
# )

#delete a bucket
# s3.Bucket(Bucket_Name).delete()


# Create SSM client
ssm = boto3.client('ssm')

response = ssm.get_parameter(
    Name='my-password',
    WithDecryption=False
)
print(response['Parameter']['Value'])

