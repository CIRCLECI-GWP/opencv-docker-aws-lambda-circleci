import json
from process_task import convert_image_to_grayscale

def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])
    
        image_url = request_body['imageUrl']
        
        gray_image_path = convert_image_to_grayscale(image_url)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'grayImagePath': gray_image_path
            })
        }   
    
    except Exception as e:
        print("Error: ", e)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }

if __name__ == "__main__":
    import os
    
    event = {
        'body': json.dumps({
            'imageUrl': 'https://picsum.photos/id/237/536/354'
        })
    }
    
    context = {}
    
    lambda_handler(event, context)