Plant Disease Detection using YOLOv8.

This repository contains code for an API built with Flask and the final weights of a fine-tuned YOLOv8 model on the PlantVillage dataset for detecting diseases in tomato, potato, and pepperbell plants. The primary goal of this project is to provide an effective solution for early detection of plant diseases, enabling farmers and researchers to take timely preventive measures.

Introduction:

Early detection of plant diseases is crucial for maintaining healthy crops and maximizing yield. This project uses the YOLOv8 (You Only Look Once, Version 8) object detection algorithm to identify diseases in tomato, potato, and pepperbell plants. The model is fine-tuned on the PlantVillage dataset, which contains images of various plant diseases.

Dataset:

The model is trained on the PlantVillage dataset, which is a large, publicly available collection of high-quality images of healthy and diseased plant leaves. The dataset includes different types of diseases for crops such as tomato, potato, and pepperbell, making it ideal for training robust deep learning models for disease detection.

Model:

The YOLOv8 model is a state-of-the-art deep learning architecture for object detection tasks. It is fine-tuned on the PlantVillage dataset for detecting plant diseases in real-time.

Advantages of YOLOv8:

High Accuracy: YOLOv8, with its latest architecture improvements, delivers high detection accuracy. It can effectively distinguish between different types of diseases and healthy plant leaves.

Real-Time Detection: YOLOv8 is optimized for speed and can perform real-time detection on edge devices like mobile phones, drones, or IoT devices, making it practical for use in agricultural fields.

Lightweight Model: YOLOv8 provides a balance between speed and accuracy, making it suitable for deployment on resource-constrained devices. This characteristic is particularly advantageous in remote agricultural areas where computational resources may be limited.

Versatility: YOLOv8 supports a wide range of object detection tasks, including single and multi-class detection. This versatility is valuable when expanding the model to detect more plant diseases or integrating additional features.

Ease of Use: The architecture of YOLOv8 is user-friendly, making it easy to fine-tune on custom datasets like PlantVillage. This reduces the time and effort needed to build and deploy a robust model for disease detection.

Results:

Below are some sample results of the YOLOv8 model's performance on the PlantVillage dataset:
![Picture2](https://github.com/user-attachments/assets/1eaa09cf-e15d-4d98-bff0-6f814e17bd39)

![Picture1](https://github.com/user-attachments/assets/f50ce288-7c36-4b5c-aec2-cf608de10fbb)

The images show the model's ability to detect various plant diseases accurately and quickly.
