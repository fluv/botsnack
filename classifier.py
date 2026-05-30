import torchvision.models as models
import torch
import io
from PIL import Image


model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
labels = models.ResNet50_Weights.DEFAULT.meta["categories"]
model.eval()

preprocess = models.ResNet50_Weights.DEFAULT.transforms()

def classify(data: bytes, limit: int = 5) -> list:
    image = Image.open(io.BytesIO(data)).convert("RGB")
    tensor = preprocess(image)
    tensor = tensor.unsqueeze(0) 
    with torch.no_grad():
        output = model(tensor)
    percentages = torch.softmax(output[0], 0).tolist()

    return sorted(zip(labels, percentages), key=lambda x: x[1], reverse=True)[:limit]
