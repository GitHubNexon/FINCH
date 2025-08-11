import replicate
import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME")

client = replicate.Client(api_token=REPLICATE_API_TOKEN)

def send_message(prompt):
    output = client.run(
        f"{MODEL_NAME}",
        input={"prompt": prompt}
    )
    # replicate returns a generator sometimes, join if needed
    if isinstance(output, list):
        return "".join(output)
    return output
