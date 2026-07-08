# orchestrator/pipeline.py

import hashlib

from orchestrator.agent_manager import AgentManager
from orchestrator.workflow import WorkflowController

from services.consensus_engine import ConsensusEngine
from services.preprocessing.video_processor import VideoProcessor

from database.crud import update_detection_log


class AgentOrchestratorPipeline:
    """
    Multi-Agent Intelligence Framework (MIF)

    Complete orchestration pipeline responsible for:

    • Video preprocessing
    • Agent execution
    • Consensus fusion
    • Database persistence
    • Workflow state management
    """

    def __init__(self):

        self.manager = AgentManager()

        self.workflow = WorkflowController()

        self.consensus = ConsensusEngine()

        self.video_processor = VideoProcessor()

    def generate_sha256(self, filepath: str) -> str:
        """
        Generates a SHA-256 fingerprint of the uploaded media.
        """

        sha = hashlib.sha256()

        with open(filepath, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()

    def process_forensic_pipeline(
        self,
        db,
        log_id: int,
        file_path: str
    ):
        """
        Executes the complete forensic detection pipeline.
        """

        try:

            ####################################################
            # Workflow State
            ####################################################

            self.workflow.update("PREPROCESSING")

            ####################################################
            # Generate Media Hash
            ####################################################

            media_hash = self.generate_sha256(file_path)

            ####################################################
            # Video Preprocessing
            ####################################################

            prepared = self.video_processor.prepare_video(file_path)

            frame_paths = prepared["frames"]

            ####################################################
            # Execute Intelligence Agents
            ####################################################

            self.workflow.update("ANALYZING")

            agent_outputs = {

                "visual_agent":
                    self.manager.visual.analyze(frame_paths),

                "audio_agent":
                    self.manager.audio.analyze(file_path),

                "biometric_agent":
                    self.manager.biometric.analyze(frame_paths),

                "semantic_agent":
                    self.manager.semantic.analyze(frame_paths),

                "forensic_agent":
                    self.manager.forensic.analyze(file_paths)

            }

            ####################################################
            # Consensus Engine
            ####################################################

            consensus = self.consensus.calculate_fusion_verdict(
                agent_outputs
            )

            blockchain = self.manager.blockchain.analyze(consensus)

            ####################################################
            # Save Results
            ####################################################

            update_detection_log(

                db=db,

                log_id=log_id,

                media_sha256=media_hash,

                blockchain_tx_hash=blockchain["transaction_hash"],

                blockchain_block_number=str(blockchain["block_number"]),

                ledger_is_anchored=blockchain["anchored"],

                visual_score=agent_outputs["visual_agent"]["confidence"],

                audio_score=agent_outputs["audio_agent"]["confidence"],

                biometric_score=agent_outputs["biometric_agent"]["confidence"],

                forensic_score=agent_outputs["forensic_agent"]["confidence"],

                semantic_score=agent_outputs["semantic_agent"]["confidence"],

                global_risk_score=consensus["final_score"],

                detection_confidence=consensus["final_score"],

                final_verdict=consensus["overall_verdict"],

                raw_agent_telemetry=agent_outputs,

                record_status="COMPLETED"

            )

            ####################################################
            # Future Blockchain Anchor
            ####################################################
            # blockchain_receipt = blockchain_agent.anchor(...)
            # update blockchain fields here

            ####################################################
            # Finish Workflow
            ####################################################

            self.workflow.update("COMPLETED")

            return consensus

        except Exception as e:

            self.workflow.update("FAILED")

            raise RuntimeError(
                f"Pipeline execution failed: {str(e)}"
            )