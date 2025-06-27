from together import Together
from dotenv import dotenv_values

client = Together(api_key=dotenv_values(".env")['TOGETHER_API_KEY'])

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
                    "text": open('texts/1.txt').read(),
                },
              ]
        }
    ],
  stream=True,
)
#make file empty if exists
f = open('sums/1.txt', 'w+')
f = open('sums/1.txt', 'a')

for chunk in stream:
    f.write(chunk.choices[0].delta.content)
    print(chunk.choices[0].delta.content or "", end="", flush=True)

#for prettier output
print()

f.close()