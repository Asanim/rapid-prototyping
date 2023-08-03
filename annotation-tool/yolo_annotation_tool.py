import os
import json
import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path

# Path to your images
image_folder = 'test-data/images'
output_folder = 'test-data/annotations'

# Load the latest YOLO model
model = YOLO('yolo11l.pt')  # You can specify the model size here ('yolov5l' for large model)

# Function to generate COCO annotations
def generate_coco_annotations(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Prepare the COCO structure
    coco_data = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    category_id = 1
    annotation_id = 1
    categories = set()

    # Process each image in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = cv2.imread(image_path)
        height, width, _ = img.shape
        
        # Add image information to COCO format
        image_info = {
            "id": len(coco_data['images']) + 1,
            "file_name": image_file,
            "width": width,
            "height": height
        }
        coco_data['images'].append(image_info)

        # Perform detection using YOLO
        results = model(image_path)
        
        # Iterate through detections and create COCO annotations
        for result in results:  # Iterate through the result object for each image
            boxes = result.boxes  # Get the bounding boxes from the result
            for box in boxes:
                xmin, ymin, xmax, ymax = box.xyxy[0].tolist()  # Get the coordinates of the bounding box
                conf = box.conf[0].item()  # Get the confidence score
                class_id = int(box.cls[0].item())  # Get the class ID
                
                category_name = model.names[class_id]
                categories.add(category_name)
                
                # Create annotation in COCO format
                annotation = {
                    "id": annotation_id,
                    "image_id": len(coco_data['images']),
                    "category_id": category_id,
                    "bbox": [xmin, ymin, xmax - xmin, ymax - ymin],
                    "area": (xmax - xmin) * (ymax - ymin),
                    "iscrowd": 0
                }

                # Add to the annotations
                coco_data['annotations'].append(annotation)
                annotation_id += 1
        
        # Add categories to the COCO structure
        for category_name in categories:
            category = {
                "id": category_id,
                "name": category_name,
                "supercategory": "none"
            }
            coco_data['categories'].append(category)
            category_id += 1
    
    # Save COCO annotations to a JSON file
    output_json_path = os.path.join(output_folder, 'annotations.json')
    with open(output_json_path, 'w') as json_file:
        json.dump(coco_data, json_file, indent=4)

    print(f'Annotations saved to {output_json_path}')


if __name__ == '__main__':
    generate_coco_annotations(image_folder, output_folder)
