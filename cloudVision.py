import boto3

# Replace these with your own values
aws_access_key_id = 'AKIATKG46K3LF6B6HIO2'
aws_secret_access_key = 'NorN4qkxdD4Cf6Y6/5yigFRB0Zt59nA8erTvHZCv'
aws_account_id='228096628438'
bucket_name = 'kops-hiran-storage'
client = boto3.client('ce', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')
start_date = '2023-08-01'  # Replace with your desired start date
end_date = '2023-08-14' 

service="Amazon Elastic Compute Cloud - Compute"

region_name = 'us-east-1'  # Replace with your desired region

# Create a Boto3 EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Describe instances and filter by the "running" state
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Get the count of running instances
#running_instance_count = sum(len(reservation['Instances']) for reservation in response['Reservations'])


for reservation in response['Reservations']:
    #print(reservation['Instances'])
    print( ' Instance type : '+reservation['Instances'][0]['InstanceType'] )
    
#print(f"Number of running EC2 instances: {running_instance_count}")
#print(response)



























#print(response)







# session = boto3.Session(
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key
# )

# services = session.get_available_services() 
# print(services)










# # Create a Boto3 S3 client
# s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# # Get bucket information
# try:
#     response = s3.head_bucket(Bucket=bucket_name)
#     print(f"Bucket '{bucket_name}' exists with the following metadata:")
#     print(response)
# except Exception as e:
#     print(f"Bucket '{bucket_name}' does not exist or encountered an error: {e}")
    
    