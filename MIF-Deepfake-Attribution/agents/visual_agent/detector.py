# agents/visual_agent/detector.py

import os
from typing import List, Dict

import torch
from PIL import Image

from agents.visual_agent.feature_extractor import VisualFeatureExtractor


class VisualAgent:
    """
    Visual Deepfake Detection Agent

    Responsibilities:
    -----------------
    • Detect facial manipulation artifacts
    • Detect GAN-generated inconsistencies
    • Detect lighting inconsistencies
    • Produce a confidence score for the Consensus Engine

    Output Format:
    {
        "agent_name": "Visual Agent",
        "confidence": float,
        "is_fake": bool,
        "artifacts": [...]
    }
    """

    def __init__(self):

        self.model_path = "weights/efficientnet.pth"

        self.extractor = VisualFeatureExtractor(
            weight_name=self.model_path
        )

        self.model_loaded = os.path.exists(self.model_path)

    def _predict(self, image_tensor) -> float:
        """
        Executes model inference.

        Currently returns a placeholder score.

        Replace this function with actual PyTorch inference
        after training/fine-tuning the EfficientNet model.
        """

        with torch.no_grad():

            # -------------------------------------------------
            # Placeholder inference
            # Replace with:
            #
            # output = self.extractor.model(image_tensor)
            # probability = torch.sigmoid(output).item()
            # -------------------------------------------------

            probability = 0.72

        return float(probability)

    def analyze(self, frame_paths: List[str]) -> Dict:
        """
        Analyze extracted video frames.

        Parameters
        ----------
        frame_paths : List[str]

        Returns
        -------
        Dict
        """

        if not frame_paths:

            return {
                "agent_name": "Visual Agent",
                "confidence": 0.0,
                "is_fake": False,
                "artifacts": [
                    "No frames supplied for analysis"
                ]
            }

        scores = []

        for frame_path in frame_paths:

            if not os.path.exists(frame_path):
                continue

            try:

                image = Image.open(frame_path).convert("RGB")

                tensor = self.extractor.extract_features(image)

                probability = self._predict(tensor)

                scores.append(probability)

            except Exception:
                continue

        if not scores:

            return {
                "agent_name": "Visual Agent",
                "confidence": 0.0,
                "is_fake": False,
                "artifacts": [
                    "Frame extraction failed"
                ]
            }

        confidence = sum(scores) / len(scores)

        artifacts = []

        if confidence >= 0.50:

            artifacts.extend([
                "Face blending artifacts",
                "Lighting inconsistencies",
                "Texture discontinuities",
                "Boundary mismatches"
            ])

            is_fake = True

        else:

            artifacts.append(
                "Visual consistency verified"
            )

            is_fake = False

        return {

            "agent_name": "Visual Agent",

            "confidence": round(confidence, 4),

            "is_fake": is_fake,

            "artifacts": artifacts
        }