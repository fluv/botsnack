import torchvision.models as models
import torch
import io
from os import getenv
from PIL import Image

model_name = getenv("CLASSIFIER_MODEL", "resnet50")

weights = models.get_model_weights(model_name).DEFAULT
model = models.get_model(model_name, weights=weights)
labels = weights.meta["categories"]
model.eval()
preprocess = weights.transforms()

def classify(data: bytes, limit: int = 5) -> list[tuple[str, float]]:
    image = Image.open(io.BytesIO(data)).convert("RGB")
    tensor = preprocess(image)
    tensor = tensor.unsqueeze(0) 
    with torch.no_grad():
        output = model(tensor)
    percentages = torch.softmax(output[0], 0).tolist()

    return sorted(zip(labels, percentages), key=lambda x: x[1], reverse=True)[:limit]
