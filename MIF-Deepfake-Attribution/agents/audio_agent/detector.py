from agents.audio_agent.voice_clone_detector import VoiceCloneDetector
from agents.audio_agent.audio_visual_sync import AudioVisualSyncAnalyzer


class AudioAgent:
    """
    Audio Intelligence Agent

    Performs:

    • Voice clone detection
    • Audio-visual synchronization analysis

    Produces one confidence score for the
    Consensus Engine.
    """

    def __init__(self):

        self.voice_detector = VoiceCloneDetector()

        self.sync_detector = AudioVisualSyncAnalyzer()

    def analyze(self, media_path: str):

        voice = self.voice_detector.analyze(media_path)

        sync = self.sync_detector.analyze(media_path)

        confidence = round(
            (
                voice["confidence"] +
                sync["confidence"]
            ) / 2,
            4
        )

        artifacts = list(
            set(
                voice["artifacts"] +
                sync["artifacts"]
            )
        )

        return {
            "agent_name": "Audio Agent",
            "confidence": confidence,
            "is_fake": confidence >= 0.65,
            "artifacts": artifacts
        }