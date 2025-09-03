from google import genai
from google.genai.types import GenerateContentConfig

client = genai.Client(api_key='your-gemini-api-key')

model_id = "gemini-2.5-flash"

tools = [
    {"url_context": {}}
    
]

url = "https://www.gov.br/inss/pt-br/direitos-e-deveres/inscricao-e-contribuicao/tabela-de-contribuicao-mensal"
    
prompt = f"""Extract the salary and rate values for INSS contributions from this page {url}.
    Return only the values for Employees.
    Return ONLY the result in JSON with the following structure {{"salario": "De xxxxx a xxxxx", "aliquota": "x%"}}
    **Important**
    Provide the answer directly and objectively, without introductions or additional comments.
    """
        
response = client.models.generate_content(
    model=model_id,
    contents=prompt,
    config=GenerateContentConfig(tools=tools)
)

for each in response.candidates[0].content.parts:
  print(each.text)