from transformers import SegformerImageProcessor, AutoModelForSemanticSegmentation
from PIL import Image
import requests
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import numpy as np

processor = SegformerImageProcessor.from_pretrained("mattmdjaga/segformer_b2_clothes")
model = AutoModelForSemanticSegmentation.from_pretrained("mattmdjaga/segformer_b2_clothes")

first_image_path = "sampleData/first.jpg"
first_image = Image.open(first_image_path)

inputs_first = processor(images=first_image, return_tensors="pt")
outputs_first = model(**inputs_first)
logits_first = outputs_first.logits.cpu()
upsampled_logits_first = nn.functional.interpolate(
    logits_first,
    size=first_image.size[::-1],
    mode="bilinear",
    align_corners=False,
)
pred_upper_clothes_first = (upsampled_logits_first.argmax(dim=1)[0] == 4).float()
pred_upper_clothes_rgb_first = torch.stack([pred_upper_clothes_first] * 3, dim=0)
first_image_tensor = torch.tensor(np.array(first_image)).permute(2, 0, 1).float() / 255.0

second_image_path = "sampleData/second.jpg"
second_image = Image.open(second_image_path)

inputs_second = processor(images=second_image, return_tensors="pt")
outputs_second = model(**inputs_second)
logits_second = outputs_second.logits.cpu()
upsampled_logits_second = nn.functional.interpolate(
    logits_second,
    size=second_image.size[::-1],
    mode="bilinear",
    align_corners=False,
)
pred_upper_clothes_second = (upsampled_logits_second.argmax(dim=1)[0] == 4).float()
pred_upper_clothes_rgb_second = torch.stack([pred_upper_clothes_second] * 3, dim=0)
second_image_tensor = torch.tensor(np.array(second_image)).permute(2, 0, 1).float() / 255.0


resized_second_image = second_image.resize((first_image.width, first_image.height))
resized_second_image_tensor = torch.tensor(np.array(resized_second_image)).permute(2, 0, 1).float() / 255.0


result_image = (pred_upper_clothes_rgb_first[0] * resized_second_image_tensor + (1 - pred_upper_clothes_rgb_first[0]) * first_image_tensor).numpy().transpose(1, 2, 0)


# segmented_color = torch.mean(second_image_tensor[:, pred_upper_clothes_second.bool()], dim=1)

# result_image = (pred_upper_clothes_rgb_first[0] * segmented_color[0] + (1 - pred_upper_clothes_rgb_first[0]) * first_image_tensor).numpy().transpose(1, 2, 0)

fig, axs = plt.subplots(1, 3, figsize=(12, 6))

axs[0].imshow(np.array(first_image))
axs[0].set_title('First Image')

axs[1].imshow(np.array(second_image))
axs[1].set_title('Second Image')

axs[2].imshow(result_image)
axs[2].set_title('Modified Image')

plt.show()