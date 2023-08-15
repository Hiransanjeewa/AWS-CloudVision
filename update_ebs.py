
import boto3


# Automatically update the type of EBS voulumes to free tier gp3 type


def extractVolumeId (volume_arn):
    #Split arn using the colon (':')
    arn_parts = volume_arn.split(':')
    # tghe volume id is the last part of the volue-name after "voulume/"
    volume_id= arn_parts[-1].split('/')[-1];
    return volume_id;


def lambda_handler(event, context):
    
    print(event);

    


    volume_arn = event['resources'][0]
  
    volume_id = extractVolumeId(volume_arn);
    
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.modify_volume(
         
         VolumeId=volume_id,
         VolumeType='gp3',
       
    )
    
    
    