from together import Together
from dotenv import dotenv_values

client = Together(api_key=dotenv_values(".env")['TOGETHER_API_KEY'])

def summarize(input):

  stream = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free", #later add selection or test other models
    messages=[
          {
            "role": "user",
            "content": [
                  {
                      "type": "text",
                      "text": open('prompt.txt').read(),
                  },
                  {
                      "type": "text",
                      "text": input,
                  },
                ]
          }
      ],
    stream=True,
  )
 
  output = ""
  for chunk in stream:
    output += chunk.choices[0].delta.content

  return output.split('</think>')[1].strip()
