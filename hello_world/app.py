import boto3
import requests
import json
import base64

# session = boto3.session.Session(profile_name = 'default')
client = boto3.client('rekognition', 'ap-southeast-2')

def compare_faces(source, target):
    res = client.compare_faces(
        SourceImage={
            'Bytes': source,
        },
        TargetImage={
            'Bytes': target,
        },
        SimilarityThreshold=80
    )
    result = {
        'similarity': res['FaceMatches'][0]['Similarity'],
        'confidence': res['FaceMatches'][0]['Face']['Confidence'],
    }
    return result


# img1 = get_image_from_file('./azad1.jpeg')
# img2 = get_image_from_file('./azad2.jpeg')
# img1 = get_image_from_url('https://imgur.com/a/xoeR3xp')
# img2 = get_image_from_url('https://imgur.com/a/yorKwzk')
# print(img1)

def lambda_handler(event, context):
    # body = json.loads(event['body'])
    # img1 = body['source']
    # img2 = body['target']
    # result = compare_faces(img1, img2)
    result = {
        'source': "event",
        # 'target': img2
        'event': event
    }
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(result)
    }
