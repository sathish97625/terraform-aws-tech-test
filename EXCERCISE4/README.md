# AWS Terraform Exercise 4

We are looking for a Python3 Lambda function which writes the state of the instance(s) from the previous solution to a DynamoDB table every hour, and nothing on the table should be older than a day.

Instance-state-lambda.py has been written for the above requirement.
A dynamodb table has been created to insert every hour data.

