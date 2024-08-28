# Plant Disease Detection using YOLOv8

This repository contains code for an API built with Flask and the final weights of a fine-tuned YOLOv8 model on the PlantVillage dataset for detecting diseases in plants like tomato, potato, and bell pepper. The model's classes are labeled in Arabic, making it easier for users familiar with the language to understand and work with the results.

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Model](#model)
4. [Advantages of YOLOv8](#advantages-of-yolov8)
5. [Results](#results)
6. [Contributing](#contributing)

## Introduction

Early detection of plant diseases is crucial for maintaining healthy crops and maximizing yield. This project uses the YOLOv8 (You Only Look Once, Version 8) object detection algorithm to identify diseases in plants such as tomatoes, potatoes, and bell peppers. The model is fine-tuned on the PlantVillage dataset, which contains images of various plant diseases, and the classes are labeled in Arabic for easier understanding.

## Dataset

The model is trained on the PlantVillage dataset, a large, publicly available collection of high-quality images of healthy and diseased plant leaves. The dataset includes different types of diseases for crops such as الطماطم (Tomato), البطاطس (Potato), and الفلفل (Bell Pepper), making it ideal for training robust deep learning models for disease detection.

## Model

The YOLOv8 model is a state-of-the-art deep learning architecture for object detection tasks. It is fine-tuned on the PlantVillage dataset for detecting plant diseases in real-time. The classes in the model are labeled in Arabic as follows:

- **طماطم** (Tomato)
- **بطاطس** (Potato)
- **فلفل** (Bell Pepper)

## Advantages of YOLOv8

1. **High Accuracy**: YOLOv8, with its latest architecture improvements, delivers high detection accuracy. It can effectively distinguish between different types of diseases and healthy plant leaves.

2. **Real-Time Detection**: YOLOv8 is optimized for speed and can perform real-time detection on edge devices like mobile phones, drones, or IoT devices, making it practical for use in agricultural fields.

3. **Lightweight Model**: YOLOv8 provides a balance between speed and accuracy, making it suitable for deployment on resource-constrained devices. This characteristic is particularly advantageous in remote agricultural areas where computational resources may be limited.

4. **Versatility**: YOLOv8 supports a wide range of object detection tasks, including single and multi-class detection. This versatility is valuable when expanding the model to detect more plant diseases or integrating additional features.

5. **Ease of Use**: The architecture of YOLOv8 is user-friendly, making it easy to fine-tune on custom datasets like PlantVillage. This reduces the time and effort needed to build and deploy a robust model for disease detection.


## Results
Below are some sample results of the YOLOv8 model's performance on the PlantVillage dataset, with disease names displayed in Arabic:
![Picture1](https://github.com/user-attachments/assets/2dd2fcdf-0330-407a-8918-522dedc6e4ff)
![Picture2](https://github.com/user-attachments/assets/083c863a-16ed-43c2-a80b-3c6b363a125a)


## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
