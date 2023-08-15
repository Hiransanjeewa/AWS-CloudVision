import boto3

# Replace these with your own values
aws_access_key_id = 'AKIATKG46K3LF6B6HIO2'
aws_secret_access_key = 'NorN4qkxdD4Cf6Y6/5yigFRB0Zt59nA8erTvHZCv'
bucket_name = 'kops-hiran-storage'
client = boto3.client('ce', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')
start_date = '2023-08-01'  # Replace with your desired start date
end_date = '2023-08-14' 




# Get all created ec2 instances with cost 
ce = boto3.client('ce', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')

# Define the filter for your query (optional)
filter = {
    "And": [
             {
            "Dimensions": {
                "Key": "LINKED_ACCOUNT",
                "Values": ["228096628438"]  # Replace with your AWS account ID
            }
        },
        {
            "Dimensions": {
                "Key": "SERVICE",
                "Values": ["Amazon Elastic Compute Cloud - Compute"]  # Add specific service values here
            }
        }
    ]
}

# Get cost and usage data
response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost', 'UsageQuantity'],  # Add more metrics as needed
    Filter=filter
)

# Print cost and usage data
for result_by_time in response['ResultsByTime']:
    print(f"Date: {result_by_time['TimePeriod']['Start']} - {result_by_time['TimePeriod']['End']}")
    print(f"Unblended Cost: {result_by_time['Total']['UnblendedCost']['Amount']} {result_by_time['Total']['UnblendedCost']['Unit']}")
    print(f"Usage Quantity: {result_by_time['Total']['UsageQuantity']['Amount']} {result_by_time['Total']['UsageQuantity']['Unit']}")
    print()























# Retriving Services
# dimension_name = 'SERVICE'
#  #Get valid values for the specified dimension
# response = client.get_dimension_values(
#     TimePeriod={
#         'Start': '2023-08-01',
#         'End': '2023-08-14'
#     },
#     Dimension=dimension_name
# )

# # Print dimension values
# for value in response['DimensionValues']:
#     print(value['Value'])

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
    
    