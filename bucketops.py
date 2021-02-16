import boto3

BUCKET_NAME = 'kunlemybotobucket123321'


def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3"""
    return s3


def create_bucket(bucket_name):
    return s3_client().create_bucket(
        ACL='private',
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'
        }
    )


def create_bucket_policy():
    bucket_policy = {

    }

if __name__ == '__main__':
    print(create_bucket(BUCKET_NAME))
