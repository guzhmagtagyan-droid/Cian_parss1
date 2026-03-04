import torch
from lama import LaMa
import cv2

class WatermarkRemover:
    def __init__(self):
        self.lama = LaMa().to('cuda')  # Load model on GPU

    def remove_watermark(self, image_path, mask_path):
        # Load the image and the mask
        image = cv2.imread(image_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

        # Ensure the mask is binary
        _, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)

        # Run inpainting
        results = self.lama.inpaint(image, mask)

        return results

if __name__ == '__main__':
    remover = WatermarkRemover()
    result = remover.remove_watermark('input_image.jpg', 'mask_image.jpg')
    cv2.imwrite('output_image.jpg', result)