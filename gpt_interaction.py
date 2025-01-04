import os
from openai import OpenAI

def create_title(base_text):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    content = "Write a title based on this text:"+base_text

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": content
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "\"Guia de Formatação de Texto com Markdown: Estruturas, Listas e Código\""
                    }
                ]
            }
        ],
        response_format={
            "type": "text"
        },
        temperature=1,
        max_completion_tokens=790,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content