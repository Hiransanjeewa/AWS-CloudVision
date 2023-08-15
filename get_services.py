import boto3

# Replace these with your own values
aws_access_key_id = 'AKIATKG46K3LF6B6HIO2'
aws_secret_access_key = 'NorN4qkxdD4Cf6Y6/5yigFRB0Zt59nA8erTvHZCv'
aws_account_id='228096628438'
bucket_name = 'kops-hiran-storage'
client = boto3.client('ce', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')
start_date = '2023-08-01'  # Replace with your desired start date
end_date = '2023-08-14' 





# Retriving activated Services
dimension_name = 'SERVICE'
 #Get valid values for the specified dimension
response = client.get_dimension_values(
    TimePeriod={
        'Start': '2023-08-01',
        'End': '2023-08-14'
    },
    Dimension=dimension_name
)

# Print dimension values
for value in response['DimensionValues']:
    print(value['Value'])
