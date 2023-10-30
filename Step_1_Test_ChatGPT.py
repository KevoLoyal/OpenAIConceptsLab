#Note: The openai-python library support for Azure OpenAI is in preview.

import os

openai.api_type = "azure"
openai.api_base = "Endpoint"
openai.api_version = "2023-07-01-preview"
openai.api_key = "API-KEY"

response = openai.ChatCompletion.create(
  engine="gpt-35-turbo",
  messages = [{"role":"user","content":"Tell me about Cerro Chirripo in Costa Rica"}],
  temperature=0.0,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)



