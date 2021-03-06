# SSH Tunnel config
REMOTE_SERVER_HOST = "ec2-123-456-789.ca-central-1.compute.amazonaws.com" # AWS EC2 instance = "jumpbox"
REMOTE_SERVER_USERNAME = 'ec2-user'
REMOTE_SERVER_PRIVATE_KEY = r"C:\Users\jdoe\.ssh\jdoe-ca-central-1.pem"

PRIVATE_SERVER_HOST = "jdoe-db.ca-central-1.rds.amazonaws.com" # MySQL db in private AWS subnet
PRIVATE_SERVER_PORT = 3306 # MySQL db port

LOCAL_HOST = '127.0.0.1'
LOCAL_PORT = 3306