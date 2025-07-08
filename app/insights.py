import boto3

def get_insights_from_bedrock(text: str) -> str:
    bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
    response = bedrock.invoke_model(
        modelId='anthropic.claude-v2',
        contentType='application/json',
        accept='application/json',
        body=f'{{"prompt": "Dê sugestões com base nessa fala: {text}"}}'
    )
    return response['body'].read().decode()
