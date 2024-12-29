import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        """
        Sync a local folder to an S3 bucket.
        """
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        result = os.system(command)
        if result != 0:
            raise Exception("Error syncing folder to S3")

    def sync_folder_from_s3(self, aws_bucket_url, folder):
        """
        Sync an S3 bucket folder to a local folder.
        """
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        result = os.system(command)
        if result != 0:
            raise Exception("Error syncing folder from S3")
