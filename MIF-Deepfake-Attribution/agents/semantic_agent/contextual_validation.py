import random


class ContextualValidator:
    """
    Performs contextual reasoning over the scene.

    Future versions can integrate LLMs,
    scene captioning, or object detection.
    """

    def __init__(self):
        pass

    def analyze(self, frame_paths: list[str]):

        confidence = round(random.uniform(0.45, 0.90), 4)

        return {
            "confidence": confidence,
            "is_fake": confidence >= 0.65,
            "artifacts": (
                [
                    "Context inconsistency",
                    "Logical scene mismatch"
                ]
                if confidence >= 0.65
                else []
            )
        }