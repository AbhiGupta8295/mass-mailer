# mass-mailer
mass-mailer made using AWS Lambda and SES (in sandbox)
The Lambda function will get triggered as soon as .csv file gets uploaded in the respective S3 bucket.

1. Create Role with SES and CloudWatch Full Access.
2. Create Security Group as per the requirement.
3. Create S3 bucket for csv files.
4. Create lambda function in the same region as S3 bucket to avoid extra charges.
5. Drop the .py file in code section.
6. Add trigger as PUT event for S3 bucket as source.
7. Use PUT test template for running code.
