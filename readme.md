# Helmet Detection Using YOLO

This repository contains a project for detecting helmets using the YOLO object detection model. The setup includes training data, YOLO configuration, custom scripts for training and inference, and example outputs.

## Project Structure

Dataset : https://www.kaggle.com/datasets/aneesarom/rider-with-helmet-without-helmet-number-plate/data

- **`classes.txt`**: Contains the class names used for training (e.g., `helmet`, `no-helmet`).
- **`coco128.yaml`**: Configuration file defining dataset paths and classes for YOLOv3 training.
- **`image_to_text.py`**: Script for converting image-based annotations into YOLO-compatible text format.
- **`main.py`**: Main script to perform object detection on input data using YOLOv3.
- **`training.py`**: Script to train YOLOv3 with the specified dataset and parameters.
- **`4class.py`**: Script specifically for working with a 4-class model setup.
- **`yolo-weights/`**: Directory containing pre trained or custom-trained YOLO weights (should download from kaggle)
- **`runs/`**: Directory where YOLO training and detection results are saved (e.g., logs, model checkpoints).
- **`videos/`**: Contains input video files for detection. (Your own video or refer dataset for other)
- **`train/`**: Training dataset folder containing images and corresponding YOLO annotations. (should download from kaggle)
- **`val/`**: Validation dataset folder containing images and YOLO annotations for model evaluation. (should download from kaggle)


## Features

- **Helmet Detection**: Detect helmets on individuals in images or videos using YOLOv3.
- **Custom Training**: Train the model on custom datasets by modifying the provided training scripts and configurations.
- **Flexible Deployment**: Supports both image and video input for inference.

## Requirements

Install the following dependencies before running the scripts:

- Python 3.7+
- OpenCV
- PyTorch
- NumPy
- Matplotlib

 
## Usage

### Training the Model

1. Prepare your dataset in YOLO format (images and `.txt` annotation files).
2. Update the `coco128.yaml` file with your dataset paths and class names.
3. Run the `training.py` script:

   ```bash
   python training.py
   ```

### Running Inference

To perform inference on an image or video, use the `main.py` script:

```bash
python main.py --source [path to image/video] --weights [path to YOLO weights]
```

### Visualization

The `output.mp4` file demonstrates the detection results on a sample input video.

## Results

we aims to achieve high accuracy in detecting helmets.


ps: 
Here is a fun example of a famous Kollywood actor driving a bike in a movie:
used this as an Example. I own no copyright to the image or so, If it needs to be taken down kindly mail to {bornwin18@gmail.com}
Source:

![image alt](https://github.com/sud0410/Helmet-numberplate-detection-using-Yolo/blob/8a22a0a7c3ee8b688960b4917db2f95e99e0d27a/Ip.jpeg)




Post processed:

![image alt](https://github.com/sud0410/Helmet-numberplate-detection-using-Yolo/blob/8a22a0a7c3ee8b688960b4917db2f95e99e0d27a/Op.jpeg)

ALso kindly check the journal publication if interested:   https://www.ijaresm.com/search?x=0&y=0&keyword2=Sudarsan+S


## Future Improvements

- Enhance the dataset with more diverse examples.
- Experiment with YOLOv5 or YOLOv8 for improved performance.
- Deploy the model using Flask or FastAPI for real-time detection.

## Acknowledgements

Used uses the YOLOv3 model and OpenCV's DNN module for object detection. Pretrained weights and configurations were adapted from [ultralytics/yolov3](https://github.com/ultralytics/yolov3).

---

Feel free to contribute or suggest improvements via pull requests!




