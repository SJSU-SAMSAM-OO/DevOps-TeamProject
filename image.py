import openai

openai.api_key = 'sk-proj-hvNsbYsSpZSTE02rQU5zT3BlbkFJPSemFNjQ7UspOmKjz7tc'

response = openai.Image.create(
  model="dall-e-3",
  prompt="A cute cat",
  size="1024x1024",
  n=1
)

image_url = response['data'][0]['url']
print(image_url)
