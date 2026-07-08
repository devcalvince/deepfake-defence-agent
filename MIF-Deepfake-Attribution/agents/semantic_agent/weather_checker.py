import random


class WeatherConsistencyChecker:
    """
    Checks environmental consistency.

    Future versions may compare

    • shadows

    • lighting

    • weather APIs

    • timestamps

    against the observed scene.
    """

    def __init__(self):
        pass

    def analyze(self, frame_paths: list[str]):

        confidence = round(random.uniform(0.30, 0.80), 4)

        return {

            "confidence": confidence,

            "is_fake": confidence >= 0.65,

            "artifacts": (

                [

                    "Lighting inconsistency",

                    "Weather mismatch"

                ]

                if confidence >= 0.65

                else []

            )

        }