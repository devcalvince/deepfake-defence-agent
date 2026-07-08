# orchestrator/agent_manager.py

from agents.visual_agent.detector import VisualAgent
from agents.audio_agent.voice_clone_detector import AudioAgent
from agents.biometric_agent.detector import BiometricAgent
from agents.semantic_agent.contextual_validation import SemanticAgent
from agents.forensic_agent.metadata_analysis import ForensicAgent
from agents.blockchain_agent.detector import BlockchainAgent



class AgentManager:
    """
    Executes every intelligence agent independently and
    aggregates their outputs for the Consensus Engine.
    """

    def __init__(self):

        self.visual = VisualAgent()

        self.audio = AudioAgent()

        self.biometric = BiometricAgent()

        self.semantic = SemanticAgent()

        self.forensic = ForensicAgent()

        self.blockchain = BlockchainAgent()

    def execute_agents(self, media_path: str):

        return {

            "visual_agent":
                self.visual.analyze(media_path),

            "audio_agent":
                self.audio.analyze(media_path),

            "biometric_agent":
                self.biometric.analyze(media_path),

            "semantic_agent":
                self.semantic.analyze(media_path),

            "forensic_agent":
                self.forensic.analyze(media_path)
        }