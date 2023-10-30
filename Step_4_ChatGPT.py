#Note: The openai-python library support for Azure OpenAI is in preview.


openai.api_type = "azure"
openai.api_base = "endpoint"
openai.api_version = "2023-07-01-preview"
openai.api_key = "key"

print("Welcome to BAM GPT, Please type your question: ")
print("  ")
getinput = input()
conversation= [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":getinput}]

while conversation != 0:

  response = openai.ChatCompletion.create(
    engine="gpt-35-turbo",
    messages = conversation,
    temperature=0.0,
    max_tokens=1000,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

  text = response['choices'][0]['message']['content']
  print("  ")
  print(text)
  print("  ")
  print("..................................")
  print("  ")

  getinput = input()
  if getinput == "exit":
      print("Thank you, this program will end now")
      break  # This will Exit the Loop
  conversation += [{"role":"assistant","content":text},{"role":"assistant","content":getinput}]

