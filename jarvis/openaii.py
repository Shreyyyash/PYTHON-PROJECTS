import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a letter to a boss for resignation",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
) 
print(response)

'''{
  "id": "cmpl-7QaqHBbh9gROCQsZK5CULALOFFYZ4",
  "object": "text_completion",
  "created": 1686572505,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nDear [Manager],\n\nThis letter is to inform you of my decision to tender my resignation from my position at [company name] effective [date].\n\nI am grateful to have had the opportunity to be a part of this team and grow as an employee. I've taken away only the best of memories and lessons from my tenure here, which have helped me become a more successful professional.\n\nI understand the responsibility of ensuring the smooth retransition of my role upon my departure and I am committed to providing all assistance needed to ensure it goes as smoothly as possible. I will work with you to ens  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 169,
    "total_tokens": 177
  }
}
'''