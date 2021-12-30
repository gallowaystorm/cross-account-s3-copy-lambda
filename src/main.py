import boto3
import config
import logging
import urllib.parse

def lambda_handler(event, context):
    logger = logging.getLogger()

    # Set up source S3 credentials
    source_client = boto3.resource(
      service_name='s3',
      aws_access_key_id = config.SOURCE_AWS_ACCESS_KEY,
      aws_secret_access_key = config.SOURCE_AWS_SECRET_KEY
    )
    #Create source bucket object
    source_bucket = source_client.Bucket(event['Records'][0]['s3']['bucket']['name'])
    uploaded_object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # Set up destination S3 credentials
    destination_client = boto3.resource(
      service_name='s3',
      aws_access_key_id = config.DESTINATION_AWS_ACCESS_KEY,
      aws_secret_access_key = config.DESTINATION_AWS_SECRET_KEY
    )

    #Create destination bucket object
    destination_bucket = destination_client.Bucket(config.DESTINATION_S3_BUCKET)

    destination_bucket_object_key = config.DESTINATION_S3_BUCKET_PREFIX + uploaded_object_key
    destination_object = list(destination_bucket.objects.filter(Prefix=destination_bucket_object_key))
    # if list is bigger than 0, item already exists at destination
    if len(destination_object) > 0:
      logger.debug("Object already exists in destination bucket.  Skipping upload.")
      print("Object already exists in destination bucket.  Skipping upload.")
    else:
      logger.debug("Object does not exist.  Uploading to destination bucket now.")
      print("Object does not exist.  Uploading to destination bucket now.")
      #Copy object from source to destination
      try:
        source_client.Object(
          destination_bucket.name,
          destination_bucket_object_key
          ).copy_from(
            CopySource = {'Bucket': source_bucket.name, 'Key': uploaded_object_key},
            ACL = "bucket-owner-full-control"
            )
      except Exception as err:
        logger.error(err)

