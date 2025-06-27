from together import Together
from dotenv import dotenv_values

client = Together(api_key=dotenv_values(".env")['TOGETHER_API_KEY'])

def summarize_req(prompt, text):
  stream = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free", #later add selection or test other models
    messages=[
          {
            "role": "user",
            "content": [
                  {
                      "type": "text",
                      "text": prompt,
                  },
                  {
                      "type": "text",
                      "text": text,
                  },
                ]
          }
      ],
    stream=True,
  )
  output = ""

  for chunk in stream:
    output += chunk.choices[0].delta.content
    print(chunk.choices[0].delta.content, end="", flush=True)

  return output.split('</think>')[1].strip()

def split_text(text, n):
    for start in range(0, len(text), n):
        t = text[start:start+n]
        s = t.rfind('\n')
        if (start + n - s > n / 2):
            s = t.rfind(' ')
        else :
            s = start + n
        yield text[start:start+s]

def summarize(input):
  max_text_len = 6144
  output = ""
  prompt = open('prompt.txt').read()
  
  if len(input) > max_text_len:
    text_parts = list(split_text(input, max_text_len))  
    prompt = open('prompt_long.txt').read()

    last_summary = summarize_req(prompt, text_parts[0])
    output = last_summary
    
    i = 1
    for text_part in text_parts[1:]:
        last_summary = summarize_req(prompt, f"EXISTING_SUMMARY: {last_summary}\nNEW_TEXT_CHUNK: {text_part}")
        output = last_summary
        i += 1
        
  else:
    output = summarize_req(prompt, f"INPUT_TEXT: {input}")
  return output