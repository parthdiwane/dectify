import openai 
from ocr_conversion.image_to_text_detection import *

openai.api_key = ''

model_engine = 'gpt-3.5-turbo'

input_text = "Find harmful ingredients in the following and state why they are harmful for you: " + str(displayIngredients(img))

response = openai.ChatCompletion.create(
   model=model_engine,
   messages=[{"role": "user", "content": input_text }]
)

output_text =  response['choices'][0]['message']['content']
print(output_text)
