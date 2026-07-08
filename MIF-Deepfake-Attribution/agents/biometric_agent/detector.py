# agents/biometric_agent/detector.py

from agents.biometric_agent.blink_analysis import BlinkAnalyzer
from agents.biometric_agent.facial_motion import FacialMotionAnalyzer
from agents.biometric_agent.ppg_detector import PPGDetector


class BiometricAgent:
    """
    Multi-modal biometric verification agent.

    Combines:

    • Blink Analysis
    • Facial Motion
    • Remote PPG

    into one biometric confidence score.
    """

    def __init__(self):

        self.blink = BlinkAnalyzer()

        self.motion = FacialMotionAnalyzer()

        self.ppg = PPGDetector()

    def analyze(self, frame_paths):

        blink = self.blink.analyze(frame_paths)

        motion = self.motion.analyze(frame_paths)

        ppg = self.ppg.analyze(frame_paths)

        confidence = (

            blink["confidence"]

            + motion["confidence"]

            + ppg["confidence"]

        ) / 3

        artifacts = []

        if confidence < 0.60:

            artifacts.extend([

                "Abnormal blink frequency",

                "Facial motion inconsistency",

                "Missing physiological pulse"

            ])

            fake = True

        else:

            artifacts.append(

                "Biometric consistency verified"

            )

            fake = False

        return {

            "agent_name": "Biometric Agent",

            "confidence": round(confidence, 4),

            "is_fake": fake,

            "artifacts": artifacts,

            "telemetry": {

                "blink": blink,

                "motion": motion,

                "ppg": ppg

            }

        }