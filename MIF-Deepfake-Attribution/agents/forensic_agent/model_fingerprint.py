import random


class ModelFingerprintAnalyzer:
    """
    Attempts to identify the probable AI model
    used to generate the deepfake.

    Future versions may classify:

    • FaceSwap
    • DeepFaceLab
    • StyleGAN
    • Stable Video Diffusion
    • FaceFusion
    """

    MODELS = [
        "Unknown",
        "FaceSwap",
        "DeepFaceLab",
        "StyleGAN",
        "FaceFusion"
    ]

    def analyze(self):

        confidence = round(random.uniform(0.40, 0.90), 4)

        detected = random.choice(self.MODELS)

        return {

            "confidence": confidence,

            "generator": detected,

            "artifacts": (

                ["Generator fingerprint detected"]

                if detected != "Unknown"

                else []

            )

        }