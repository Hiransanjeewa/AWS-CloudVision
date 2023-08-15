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















# Get all created ec2 instances with cost 
ce = boto3.client('ce', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')

# Define the filter for your query (optional)
filter = {
    "And": [
             {
            "Dimensions": {
                "Key": "LINKED_ACCOUNT",
                "Values": [aws_account_id]  # Replace with your AWS account ID
            }
        },
        {
            "Dimensions": {
                "Key": "SERVICE",
                "Values": [service]  # Add specific service values here
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
    Granularity='HOURLY',
    Metrics=['UnblendedCost', 'UsageQuantity'],  # Add more metrics as needed
    Filter=filter
)

# Print cost and usage data
for result_by_time in response['ResultsByTime']:
    cost = result_by_time['Total']['UnblendedCost']['Amount']
    if cost!= '0' :
       print(f"Date: {result_by_time['TimePeriod']['Start']} - {result_by_time['TimePeriod']['End']}")
       print(f"Allocated Cost: {result_by_time['Total']['UnblendedCost']['Amount']} {result_by_time['Total']['UnblendedCost']['Unit']}")
    # print(f"Usage Quantity: {result_by_time['Total']['UsageQuantity']['Amount']} {result_by_time['Total']['UsageQuantity']['Unit']}")
       print()
       print()
       print(result_by_time)












