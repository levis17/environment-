import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c58885a1045926l6049859t1w975049889106-s3bucket-oyfyhknnqydo"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")