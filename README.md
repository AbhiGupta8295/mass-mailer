# mass-mailer
mass-mailer made using AWS Lambda and SES (in sandbox)
The Lambda function will get triggered as soon as .csv file gets uploaded in the respective S3 bucket.

1. Create Role with SES and CloudWatch Full Access.
2. Create S3 bucket for csv files.
3. Create lambda function in the same region as S3 bucket to avoid extra charges.
4. Drop the .py file in code section.
5. Add trigger as PUT event for S3 bucket as source.
6. Use PUT test template for running code.
