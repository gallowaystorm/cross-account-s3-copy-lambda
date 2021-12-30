"""Global variables definitions."""
import os
import logging

logger = logging.getLogger()

SOURCE_AWS_ACCESS_KEY = os.environ.get("SOURCE_AWS_ACCESS_KEY")
if SOURCE_AWS_ACCESS_KEY is None:
  logger.warning("Environment variable not set: SOURCE_AWS_ACCESS_KEY")

SOURCE_AWS_SECRET_KEY = os.environ.get("SOURCE_AWS_SECRET_KEY")
if SOURCE_AWS_SECRET_KEY is None:
  logger.warning("Environment variable not set: SOURCE_AWS_SECRET_KEY")

DESTINATION_AWS_ACCESS_KEY = os.environ.get("DESTINATION_AWS_ACCESS_KEY")
if DESTINATION_AWS_ACCESS_KEY is None:
  logger.warning("Environment variable not set: DESTINATION_AWS_ACCESS_KEY")

DESTINATION_AWS_SECRET_KEY = os.environ.get("DESTINATION_AWS_SECRET_KEY")
if DESTINATION_AWS_SECRET_KEY is None:
  logger.warning("Environment variable not set: DESTINATION_AWS_SECRET_KEY")

DESTINATION_S3_BUCKET = os.environ.get("DESTINATION_S3_BUCKET")
if DESTINATION_S3_BUCKET is None:
  logger.warning("Environment variable not set: DESTINATION_S3_BUCKET")

DESTINATION_S3_BUCKET_PREFIX = os.environ.get("DESTINATION_S3_BUCKET_PREFIX")
if DESTINATION_S3_BUCKET_PREFIX is None:
  DESTINATION_S3_BUCKET_PREFIX = None
  logger.warning("Environment variable not set: DESTINATION_S3_BUCKET_PREFIX.  Default prefix is null.")


__all__ = [
    "SOURCE_AWS_ACCESS_KEY",
    "SOURCE_AWS_SECRET_KEY",
    "DESTINATION_AWS_ACCESS_KEY",
    "DESTINATION_AWS_SECRET_KEY",
    "DESTINATION_S3_BUCKET",
    "DESTINATION_S3_BUCKET_PREFIX"
]
