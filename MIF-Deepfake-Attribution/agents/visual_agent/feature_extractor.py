# agents/visual_agent/feature_extractor.py

import cv2
import numpy as np


class VisualFeatureExtractor:
    """
    Extracts normalized visual features from image frames
    before inference by the deepfake detection model.
    """

    IMAGE_SIZE = (224, 224)

    def preprocess_frame(self, frame):

        # Resize

        frame = cv2.resize(frame, self.IMAGE_SIZE)

        # Convert BGR → RGB

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Normalize

        frame = frame.astype(np.float32) / 255.0

        return np.expand_dims(frame, axis=0)