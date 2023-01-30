import boto3
from botocore.exceptions import ClientError
import csv


def send_email(RECIPIENT):
    
    SENDER = "xyz@example.com" # must be verified in AWS SES Email
    rECIPIENT = RECIPIENT

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "This is test email for testing purpose..!!"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Hello there,\r\n"
                "This is a test email, sent with Amazon SES using the "
                "AWS SDK for Python (Boto)."
                )
                
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Hi there,</h1>
    <p>This test email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES CQPOCS</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
        AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    rECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
        
                        'Data': BODY_HTML
                    },
                    'Text': {
        
                        'Data': BODY_TEXT
                    },
                },
                'Subject': {

                    'Data': SUBJECT
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def lambda_handler(event, context):
    # TODO implement
    # bucket = event['Records'][0]['s3']['mailer-2023']['name']
    # csv_file_name = event['Records'][0]['s3']['emails.csv']['key']
    # RECIPIENT = s3.get_object(Bucket=bucket,Key=csv_file_name) # must be verified in AWS SES Email
  
    send_email("abc@example.com") #since it is in sandbox environment, must be verified in AWS SES Email.
    #When outside sandbox, the recipient list can be read from the uploaded .csv file in S3 bucket.
    
