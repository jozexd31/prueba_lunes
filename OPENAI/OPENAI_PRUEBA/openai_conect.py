import openai
from pydantic import BaseModel



class Document(BaseModel):
  prompt: str = ''

def inference(prompt: str) -> list:
  openai.organization = 'org-DYRwCOZ92Bsf4lIsYceu2SVQ'
  openai.api_key = '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'
  print('[VERIFICAMOS SI INCIA EL PROCESO]'.center, '_')

  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """Eres la mejor maquina de conocimiento y responeras cualquien inquietud
          E.G: Respondo Inquietudes
           -Claro, tu pregunta fue muy buena, y la respuesta que te tengo es mas buena aun"""},
    {"role": "user", "content": prompt}
  ]
  )

  content = completion.choices[0].message.content
  total_tokens = completion.usage.total_tokens
  print('[ACABAS DE TERMINAR EL PROCESO, CONGRATS]'.center, '_')
  return [content, total_tokens]
