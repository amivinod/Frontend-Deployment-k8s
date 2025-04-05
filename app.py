from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://my-s3-db-ec2.s3-website.ap-south-1.amazonaws.com"}})

BUCKET_NAME = 'my-s3-db-ec2'
s3 = boto3.client('s3', region_name='ap-south-2')
dynamodb = boto3.resource('dynamodb', region_name='ap-south-2')
table = dynamodb.Table('PhotoMetadata')

@app.route('/upload', methods=['POST'])
def upload_photo():
    try:
        print("Received request to upload photo.")
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file provided'}), 400

        filename = f"{int(time.time())}_{file.filename}"
        print(f"Uploading file: {filename} to S3 bucket: {BUCKET_NAME}")
        s3.upload_fileobj(file, BUCKET_NAME, filename)

        print("Saving metadata to DynamoDB.")
	table.put_item(Item={
            'filename': filename,
            'uploaded_at': int(time.time())
        })
        print("Metadata saved successfully.")

        return jsonify({'message': 'Photo uploaded successfully!', 'filename': filename}), 200

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        
