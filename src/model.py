from PIL import Image
import requests
import io
from io import BytesIO
import numpy as np

from transformers import CLIPProcessor, CLIPModel


model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def infer(input_text, image):

    #url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    #image = Image.open(requests.get(url, stream=True).raw)
    input_text = input_text.split(',')

    inputs = processor(text=input_text, images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
    return str(np.array(probs.detach())[0])