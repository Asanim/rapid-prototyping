import os
import json
import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path
import os
import cv2
import glob
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import torch
from pathlib import Path

import requests
import os

# URL of the YOLO model
model_url = "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11x.pt"
ai_model_path = 'models/yolo11x.pt'

def save_model():
    # Destination directory
    save_dir = "models"
    os.makedirs(save_dir, exist_ok=True)
    model_path = os.path.join(save_dir, "yolo11x.pt")

    # Downloading the model
    print(f"Downloading {model_url} to {model_path}...")
    response = requests.get(model_url, stream=True)

    if response.status_code == 200:
        with open(model_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Download complete!")
    else:
        print(f"Failed to download the model. Status code: {response.status_code}")



def parse_args():
    parser = argparse.ArgumentParser(description="Create annotations using YOLOv5")
    parser.add_argument('--sourceDir', type=str,
                        help='Source directory of annotated images', default="/mnt/d/ai_training_dataset/prm_test_dataset/IMG-TC-ENV-043_PE-SV-1201")
    parser.add_argument('--outputDir', type=str,
                        help='Output directory for processed images', default="/mnt/d/ai_training_dataset/prm_test_dataset_540x540/IMG-TC-ENV-043_PE-SV-1201")
    return parser.parse_args()



def create_pascal_voc_xml(image_path, output_dir, detections, img_width, img_height):
    filename = os.path.basename(image_path)
    xml_filename = os.path.splitext(filename)[0] + ".xml"
    xml_path = os.path.join(output_dir, xml_filename)
    
    annotation = ET.Element("annotation")
    
    ET.SubElement(annotation, "folder").text = "rockhampton_city_council_dataset_raw"
    ET.SubElement(annotation, "filename").text = filename
    ET.SubElement(annotation, "path").text = str(image_path)
    
    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "Unknown"
    
    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = str(img_width)
    ET.SubElement(size, "height").text = str(img_height)
    ET.SubElement(size, "depth").text = "3"
    
    ET.SubElement(annotation, "segmented").text = "0"
    
    for detection in detections:
        obj = ET.SubElement(annotation, "object")
        ET.SubElement(obj, "name").text = detection.class_name  # Change label if needed
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = "0"
        ET.SubElement(obj, "difficult").text = "0"
        
        bndbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(int(detection.box[0]))
        ET.SubElement(bndbox, "ymin").text = str(int(detection.box[1]))
        ET.SubElement(bndbox, "xmax").text = str(int(detection.box[2]))
        ET.SubElement(bndbox, "ymax").text = str(int(detection.box[3]))
    
    xml_str = ET.tostring(annotation, encoding='utf-8')
    xml_pretty = parseString(xml_str).toprettyxml(indent="    ")
    
    with open(xml_path, "w") as f:
        f.write(xml_pretty)
    
    print(f"Saved: {xml_path}")


# Function to generate COCO annotations
def generate_coco_annotations(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(ai_model_path):
        save_model()

    # Load the latest YOLO model
    model = YOLO(ai_model_path)  

    # Process each image in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = cv2.imread(image_path)
        height, width, _ = img.shape
        
        # Perform detection using YOLO
        results = model(image_path)
        detections = []
        # Iterate through detections and create COCO annotations
        for result in results:  # Iterate through the result object for each image
            boxes = result.boxes  # Get the bounding boxes from the result
            for box in boxes:
                xmin, ymin, xmax, ymax = box.xyxy[0].tolist()  # Get the coordinates of the bounding box
                detection = {}
                class_id = int(box.cls[0].item())  # Get the class ID
                conf = box.conf[0].item()  # Get the confidence score

                detection.box = [xmin, ymin, xmax, ymax]
                detection.class_name = model.names[class_id]
                detection.confidence = conf

                detections.append(detection)

        create_pascal_voc_xml(image_path, output_folder, detections, width, height)
        print(f'Annotations saved to {output_folder}')
    

if __name__ == "__main__":
    args = parse_args()

    generate_coco_annotations(args.sourceDir, args.outputDir)