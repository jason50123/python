"""Sample prediction script for TensorFlow 2.x."""
import sys
import tensorflow as tf
import numpy as np
from PIL import Image
from object_detection import ObjectDetection
import cv2

MODEL_FILENAME = 'model.pb'
LABELS_FILENAME = 'labels.txt'


class TFObjectDetection(ObjectDetection):
    """Object Detection class for TensorFlow"""
    def __init__(self, graph_def, labels):
        super(TFObjectDetection, self).__init__(labels)
        self.graph = tf.compat.v1.Graph()
        with self.graph.as_default():
            input_data = tf.compat.v1.placeholder(tf.float32, [1, None, None, 3],name='Placeholder')
            tf.import_graph_def(graph_def, input_map={"Placeholder:0":input_data}, name="")
    def predict(self, preprocessed_image):
        inputs = np.array(preprocessed_image, dtype=np.float)[:, :, (2, 1, 0)] #RGB -> BGR
        with tf.compat.v1.Session(graph=self.graph) as sess:
            output_tensor = sess.graph.get_tensor_by_name('model_outputs:0')
            outputs = sess.run(output_tensor, {'Placeholder:0': inputs[np.newaxis,...]})
            return outputs[0]
def main():
# Load a TensorFlow model
    graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(MODEL_FILENAME, 'rb') as f:
        graph_def.ParseFromString(f.read())
    # Load labels
    with open(LABELS_FILENAME, 'r') as f:
        labels = [l.strip() for l in f.readlines()]
    od_model = TFObjectDetection(graph_def, labels)
    cv2.namedWindow("home", cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        sys.exit("Failed to open camera!")
    count = 0 # used to control frame
    while True:
        if cv2.getWindowProperty("home", 0) < 0:
            print("Display window closed by user, Exiting...")
            break
        ret_val, img = cap.read()
        if not ret_val:
            print("VideoCapture.read() failed, Exiting...")
            break
#image = Image.open(image_filename)
#predictions = od_model.predict_image(image)
#print(predictions)
        if count % 10 == 0 :
            image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            predictions = od_model.predict_image(image)
            print(predictions)
            h, w, c = img.shape
            for ret in predictions:
                prob = ret['probability']
                tagID = ret['tagId']
                tagName = ret['tagName']
                bbox = ret['boundingBox']
                left = bbox['left']
                top = bbox['top']
                width = bbox['width']
                height = bbox['height']
                x1 = int(left*w)
                y1 = int(top*h)
                x2 = x1 + int(width*w)
                y2 = y1 + int(height*h)
                p0 = (max(x1, 15), max(y1, 15))
                prob = round(prob,2)
                print(f"probability is {prob}, tag id is {tagID}, tag name is{tagName}")
                if prob < 0.5:
                    continue
                info = "{:.2f}:-{}".format(prob, tagName)
                cv2.rectangle(img, (x1, y1) , (x2, y2), (0, 0, 255), 2)
                cv2.putText(img,info, p0, cv2.FONT_ITALIC, 0.6, (0, 255, 0), 2)
        count += 1
        if count > 30:
            count = 0
        cv2.imshow("home", img)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
