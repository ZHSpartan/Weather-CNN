import torch
from torchvision import models, transforms, datasets
from PIL import Image

PATH = "clima.pth"
class_names = ['Rocio', 'Niebla', 'Nieve', 'Vidriado', 'Granizo', 'Tormenta', 'Lluvia',
 'Arcoiris', 'Escarcha', 'Tormenta de arena', 'Nieve']

model = models.resnet18(pretrained=True)
n_model = model
n_model.load_state_dict(torch.load(PATH))
n_model.eval()

transform = transforms.Compose([
    transforms.Resize((244, 244)),
    transforms.ToTensor()
    ])

def prediction(img):
    if isinstance(img, str):
        image = Image.open(img).convert("RGB")
    else:
        image = img.convert("RGB")

    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)
        predicted_idx = output.argmax(dim=1).item()
        predicted_class = class_names[predicted_idx]

    return predicted_class
