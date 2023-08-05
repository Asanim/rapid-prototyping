import os
import argparse
import xml.etree.ElementTree as ET
from PIL import Image
import shutil
import random
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser(description="Process annotated images.")
    parser.add_argument('--sourceDir', type=str,
                        help='Source directory of annotated images', default="/mnt/d/ai_training_dataset/prm_test_dataset/IMG-TC-ENV-043_PE-SV-1201")
    parser.add_argument('--outputDir', type=str,
                        help='Output directory for processed images', default="/mnt/d/ai_training_dataset/prm_test_dataset_540x540/IMG-TC-ENV-043_PE-SV-1201")
    parser.add_argument('--filter', type=str,
                        help='Filter annotations by class', default=None)
    parser.add_argument('--split', type=float,
                        help='Train/test split ratio', default=0.8)
    parser.add_argument('--maxNum', type=int,
                        help='Maximum number of images to process', default=None)
    parser.add_argument('--splitImages', action='store_true',
                        help='Flag to split images into left/right')
    return parser.parse_args()

import os
import cv2
import glob
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import torch
from pathlib import Path

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
        ET.SubElement(obj, "name").text = "shadow"  # Change label if needed
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = "0"
        ET.SubElement(obj, "difficult").text = "0"
        
        bndbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(int(detection[0]))
        ET.SubElement(bndbox, "ymin").text = str(int(detection[1]))
        ET.SubElement(bndbox, "xmax").text = str(int(detection[2]))
        ET.SubElement(bndbox, "ymax").text = str(int(detection[3]))
    
    xml_str = ET.tostring(annotation, encoding='utf-8')
    xml_pretty = parseString(xml_str).toprettyxml(indent="    ")
    
    with open(xml_path, "w") as f:
        f.write(xml_pretty)
    
    print(f"Saved: {xml_path}")

def detect_and_annotate(image_dir, xml_output_dir, model_path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
    
    image_paths = glob.glob(os.path.join(image_dir, "*.jpg"))
    os.makedirs(xml_output_dir, exist_ok=True)
    
    for image_path in image_paths:
        img = cv2.imread(image_path)
        if img is None:
            continue
        height, width, _ = img.shape
        
        results = model(img)
        detections = results.xyxy[0].cpu().numpy()
        
        filtered_detections = [det[:4] for det in detections]  # Extract bounding box coords
        
        create_pascal_voc_xml(image_path, xml_output_dir, filtered_detections, width, height)

if __name__ == "__main__":
    args = parse_args()
    detect_and_annotate(args.image_dir, args.xml_output_dir, args.model_path)
