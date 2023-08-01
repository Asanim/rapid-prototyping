In TensorFlow 1.x, when annotating images for object detection tasks, the typical format used is **Pascal VOC** or **COCO** format.

### 1. **Pascal VOC Format**
Pascal VOC is a popular annotation format for image classification, object detection, and segmentation. It uses XML files to store annotation information such as class labels, bounding boxes, and object attributes.

**Structure:**
- **Folder**: The folder containing the images.
- **Image file**: Each image has an associated XML annotation file.
- **XML file**: The XML file contains metadata for each object in the image, such as:
  - Image size (height, width, depth)
  - Bounding box coordinates (xmin, ymin, xmax, ymax)
  - Object class label

**Example of a Pascal VOC XML file**:
```xml
<annotation>
    <folder>images</folder>
    <filename>image1.jpg</filename>
    <path>/path/to/image1.jpg</path>
    <size>
        <width>500</width>
        <height>375</height>
        <depth>3</depth>
    </size>
    <object>
        <name>cat</name>
        <pose>Unspecified</pose>
        <truncated>1</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>100</xmin>
            <ymin>50</ymin>
            <xmax>400</xmax>
            <ymax>300</ymax>
        </bndbox>
    </object>
</annotation>
```

In this format:
- **xmin, ymin, xmax, ymax** are the coordinates of the bounding box around the object.
- **name** is the class label (e.g., "cat").

### 2. **COCO Format**
For TensorFlow Object Detection API, you might also use the **COCO format** for annotations. This format is more complex but is widely used and supported.

COCO annotations are stored in a JSON file, which contains:
- **images**: Contains image metadata (id, file name, width, height).
- **annotations**: Contains annotations for each image (id, image_id, category_id, bbox).
- **categories**: Contains category details (id, name, supercategory).

**Example of a COCO format annotation JSON**:
```json
{
    "images": [
        {
            "id": 1,
            "file_name": "image1.jpg",
            "width": 500,
            "height": 375
        }
    ],
    "annotations": [
        {
            "id": 1,
            "image_id": 1,
            "category_id": 1,
            "bbox": [100, 50, 300, 250],
            "area": 75000,
            "iscrowd": 0
        }
    ],
    "categories": [
        {
            "id": 1,
            "name": "cat",
            "supercategory": "animal"
        }
    ]
}
```

Here:
- **bbox**: The bounding box is in the format `[xmin, ymin, width, height]`.
- **category_id**: This corresponds to a category in the `categories` section.
  
### TensorFlow 1.x Object Detection API
When using TensorFlow 1.x with the **Object Detection API**, the preferred format for annotations is usually **TFRecord**, which is a binary file format used for storing dataset information efficiently.

To convert Pascal VOC or COCO annotations to TFRecord format, you can use conversion scripts provided by the TensorFlow Object Detection API. These scripts process annotation files (XML for Pascal VOC or JSON for COCO) and convert them into the TFRecord format, which is then used for training.

### Conclusion
- **Pascal VOC format**: Use XML files with object annotations.
- **COCO format**: Use JSON files with annotations.
- **TFRecord**: Preferred for TensorFlow 1.x during the training phase, but requires conversion from Pascal VOC or COCO format.

For object detection in TensorFlow 1.x, using Pascal VOC or COCO annotations and converting them to TFRecord is a common workflow.