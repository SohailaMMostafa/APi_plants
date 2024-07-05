from flask import Flask, request, jsonify, send_file
from ultralytics import YOLO
import os
import uuid


app = Flask(__name__)


model = YOLO("best.tflite")


def predict_image(image_path, img_size=256, save=True, save_dir="prediction_results", conf_threshold=0.30):
    # Perform prediction
    results = model.predict(image_path, imgsz=img_size, save=save, name=save_dir, conf=conf_threshold)
    return results


def predict_video(video_path, img_size=256, save=True, save_dir="prediction_results", conf_threshold=0.30, stream=True):
    # suffix, fourcc = '.mp4', 'avc1'
    results = model.predict(video_path, imgsz=img_size, save=save, name=save_dir, conf=conf_threshold, stream=stream)
    results_list = list(results)  # Convert generator to list
    for fram in results_list:
        print(fram.names)
    return results_list


@app.route("/api/predict/video", methods=["POST"])
def predict_video_endpoint():
    if 'file' not in request.files:
        return jsonify({'status': "fail", 'message': "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': "fail", 'message': "No selected file"}), 400

    if file:
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        video_path = os.path.join("uploads", filename)
        print(f"Saving uploaded file to {video_path}")  # Debug print
        file.save(video_path)
        results = predict_video(video_path)
        video_save_dir = results[0].save_dir
        print(f"Video save directory: {video_save_dir}")  # Debug print

        # List files in the save directory
        files_in_save_dir = os.listdir(video_save_dir)
        print(f"Files in save directory: {files_in_save_dir}")  # Debug print

        # Find the predicted video file by checking for a video file in the directory
        predicted_video_file = None
        for f in files_in_save_dir:
            if f.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv')):
                predicted_video_file = f
                break

        if predicted_video_file is None:
            return jsonify({'status': "fail", 'message': "Predicted video file not found"}), 500

        predicted_video_path = os.path.join(video_save_dir, predicted_video_file)
        print(f"Predicted video path: {predicted_video_path}")  # Debug print

        if not os.path.exists(predicted_video_path):
            return jsonify({'status': "fail", 'message': f"File not found: {predicted_video_path}"}), 500

        return send_file(predicted_video_path, mimetype='video/mp4', as_attachment=True)


@app.route("/api/predict/image", methods=["POST"])
def predict_image_endpoint():
    if 'file' not in request.files:
        return jsonify({'status': "fail", 'message': "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': "fail", 'message': "No selected file"}), 400

    if file:
        # Save the uploaded file
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        image_path = os.path.join("uploads", filename)
        file.save(image_path)

        # Predict the image
        results = predict_image(image_path)
        image_save_dir = results[0].save_dir

        predicted_image_path = os.path.join(image_save_dir, filename)

        if not os.path.exists(predicted_image_path):
            return jsonify({'status': "fail", 'message': "Predicted image file not found"}), 500

        return send_file(predicted_image_path, mimetype='image/jpeg', as_attachment=True)


if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
