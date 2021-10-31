import os
import argparse
import boto3

"""
Script to create AWS resources, can be made more generalised by adding more resources, currently limited to demo
"""


def s3_creator(name):
	# creates S3 bucket with specified name
	# for this instance keeping all configs default
	# can also add regex check for name
	s3 = boto3.resource('s3')
	s3.create_bucket(Bucket=name, CreateBucketConfiguration={
		'LocationConstraint': 'ap-south-1'})


def dynamo_creator(name):
	# creates dynamodb table with specified name
	# for this instance keeping opting for on demand type with PK and SK as partition key and sort key resp
	# can also add regex check for name
	dynamodb = boto3.resource('dynamodb')
	_table = dynamodb.create_table(
		TableName=name,
		KeySchema=[
			{
				'AttributeName': 'PK',
				'KeyType': 'HASH'  # Partition key
			},
			{
				'AttributeName': 'SK',
				'KeyType': 'RANGE'  # Sort key
			}
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'PK',
				'AttributeType': 'S'
			},
			{
				'AttributeName': 'SK',
				'AttributeType': 'S'
			},
		],
		BillingMode='PAY_PER_REQUEST',
	)


def main():
	parser = argparse.ArgumentParser(description='Command line client for generating resources')
	parser.add_argument('-s', '--s3', default=None, dest="s3_bucket_name", help="S3 Bucket Name")
	parser.add_argument('-d', '--dynamodb', default=None, dest="dynamodb_table_name", help="DynamoDB Table Name")
	args = parser.parse_args()

	if args.s3_bucket_name is None and args.dynamodb_table_name is None:
		require_ = """Please provide either or both parameters -
-s <s3-bucket-name>
-d <dynamodb-table-name>"""
		print(require_)

	if args.s3_bucket_name:
		try:
			s3_creator(args.s3_bucket_name)
		except Exception as e:
			print("[ERROR] Creating S3 Bucket - " + str(e))
	if args.dynamodb_table_name:
		try:
			dynamo_creator(args.dynamodb_table_name)
		except Exception as e:
			print("[ERROR] Creating DynamoDB Table - " + str(e))


if __name__ == "__main__":
	main()
