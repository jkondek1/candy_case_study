from loguru import logger
import openai
import os

from dotenv import load_dotenv

load_dotenv()


def get_gpt_response(prompt: str) -> str:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    from openai import OpenAIError
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        output = response.choices[0].message.content
    except (OpenAIError, TimeoutError) as error:
        logger.error('not successful', error)
        output = "N/A"
    return output
