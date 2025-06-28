from together import Together
from dotenv import dotenv_values
from mistralai import Mistral

client_together = Together(api_key=dotenv_values(".env")['TOGETHER_API_KEY'])
client_mistral = Mistral(api_key=dotenv_values(".env")['MISTRAL_API_KEY'])

def summarize_mistral(prompt, text, model):
  stream = client_mistral.chat.stream(
    model=model,
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
    output += chunk.data.choices[0].delta.content
    print(chunk.data.choices[0].delta.content, end="", flush=True)
  print()
  if output.startswith('<think>'): output = output.split('</think>')[1]
  return output.strip()

def summarize_together(prompt, text, model):
  stream = client_together.chat.completions.create(
    model=model,
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
  print()
  if output.startswith('<think>'): output = output.split('</think>')[1]
  return output.strip()

def summarize_req(prompt, text, model):
  output = ""
  print("Using model", model)
  if model in ["mistral-medium-2505", "magistral-medium-2506"]:
    output = summarize_mistral(prompt, text, model)
  elif model in ["meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"]:
    output = summarize_together(prompt, text, model)
  else:
    output = "Unknown model"
  return output


def split_text(text, n):
    for start in range(0, len(text), n):
        t = text[start:start+n]
        s = t.rfind('\n')
        if (start + n - s > n / 2):
            s = t.rfind(' ')
        else :
            s = start + n
        yield text[start:start+s]

def summarize(input, model):
  max_text_len = 6144
  output = ""
  prompt = open('prompt.txt').read()
  print("LENGTH", len(input))
  
  if len(input) > max_text_len:
    text_parts = list(split_text(input, max_text_len))  
    prompt = open('prompt_long.txt').read()

    last_summary = summarize_req(prompt, text_parts[0], model)
    output = last_summary
    
    i = 1
    for text_part in text_parts[1:]:
        last_summary = summarize_req(prompt, f"EXISTING_SUMMARY: {last_summary}\nNEW_TEXT_CHUNK: {text_part}", model)
        output = last_summary
        i += 1
        
  else:
    output = summarize_req(prompt, f"INPUT_TEXT: {input}", model)
  return output