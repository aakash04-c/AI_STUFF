from openai import OpenAI
import numpy as num
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def get_embedding( text ) :
    response = client.embeddings.create(
        model=os.getenv("EMBED_MODEL"),
        input=text
    )
    return response.data[0].embedding


def cosine_similarity( A , B):
    dot_prod = num.dot(A,B)
    norm_a = num.linalg.norm(A)
    norm_b = num.linalg.norm(B)
    return dot_prod/(norm_a*norm_b)