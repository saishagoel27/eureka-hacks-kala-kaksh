import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

vertexai.init(project="dark-geography-472317-i7", location="asia-south1")

model=ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

prompt="A cozy indian aesthetic room"


images= model.generate_images(prompt=prompt, number_of_images=1)

for i, img in enumerate(images):
    img.save(f"living_room_{i}.png")

print("Image generated and saved as png file")