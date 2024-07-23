
# YOLOv8n model for fish counting 


This repository provides a detailed analysis and implementation of a fish detection model designed for use in aquaculture environments. The model is based on the Detectron2 architecture and is intended to enhance the accuracy and efficiency of fish detection in various aquatic settings.

## Project Objective
 The main objective of this project is to provide a robust fish detection solution that can be used in real-world scenarios for:

- Counting fish
- Monitoring fish populations
- Detecting anomalies
- Improving pond management
## Model Architecture

The fish detection model utilizes advanced object detection frameworks to identify and localize fish in images of ponds. The architecture typically includes:

- Backbone: The neural network used to extract features from images. Common backbones include ResNet, MobileNet, and EfficientNet, which impact the model's accuracy and speed.
- Neck: The intermediate component that combines and adjusts features extracted by the backbone. Common neck structures include Feature Pyramid Network (FPN) and PANet.
- Head: The detection component that generates final predictions. This includes R-CNN, Faster R-CNN, and newer versions like YOLO.
## Packages Used

The project relies on several packages and libraries for training and evaluating the detection model:

- Detectron2: Developed by Facebook AI Research (FAIR), Detectron2 is a PyTorch-based object detection library known for its modularity and flexibility. Key features include:

    -  Modularity: Allows easy modification and extension of model components.
    - Support for modern architectures: Compatible with Faster R-CNN, Mask R-CNN, and RetinaNet.
    - Easy integration: Supports pretrained backbones and evaluation tools.

- YOLOv8: YOLO (You Only Look Once) is a family of object detection models known for speed and efficiency. YOLOv8, the latest version, offers:

    - Improved accuracy: Enhancements in object detection and head layers.
    - Performance optimization: High performance on modern hardware, balancing speed and accuracy.
    - Scalability: Flexible and adaptable for specific tasks.
    
## Data Preparation

The model was trained on the DePondFi dataset, which includes images of fish in ponds with annotations for each fish instance. Data preparation involved:

 - Image Annotation: Images were annotated with bounding boxes and class labels.
 - Preprocessing: Images were resized and normalized to meet model requirements.
## Model Training

Training was conducted using supervised learning techniques with the following steps:

- Hyperparameter Configuration: Adjusted parameters like learning rate, epochs, and batch size to optimize model performance.
- Training: Executed on a GPU to accelerate the learning process.
- Evaluation: Assessed using metrics such as precision, recall, and F-measure.
## Performance

The model demonstrates robust performance in detecting fish in pond images. Key performance metrics include:

- Precision: The proportion of correct detections relative to total detections.
- Recall: The proportion of detected fish relative to the total number of fish present.
- F-measure: The harmonic mean of precision and recall, providing an overall performance indicator.
## Usage

To run the model on a video, follow these steps:

```console
cd path_to_yout_project_directory

```

```console
pip install -r requirements.txt

```

```console
cd Demo_script

```

```console
python demo_script.py --in_video_path [INPUT_VIDEO_PATH]

```