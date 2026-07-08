from agents.forensic_agent.metadata_analysis import MetadataAnalyzer
from agents.forensic_agent.model_fingerprint import ModelFingerprintAnalyzer
from agents.forensic_agent.source_tracing import SourceTracer


class ForensicAgent:
    """
    Performs forensic attribution.

    Responsibilities

    • Metadata inspection

    • Generator fingerprinting

    • Source tracing

    Produces evidence for attribution.
    """

    def __init__(self):

        self.metadata = MetadataAnalyzer()

        self.fingerprint = ModelFingerprintAnalyzer()

        self.tracer = SourceTracer()

    def analyze(self, media_path: str):

        metadata = self.metadata.analyze(media_path)

        fingerprint = self.fingerprint.analyze()

        source = self.tracer.analyze()

        confidence = round(

            (

                metadata["confidence"]

                + fingerprint["confidence"]

                + source["confidence"]

            )

            / 3,

            4

        )

        artifacts = list(

            set(

                metadata["artifacts"]

                + fingerprint["artifacts"]

                + source["artifacts"]

            )

        )

        return {

            "agent_name": "Forensic Agent",

            "confidence": confidence,

            "is_fake": confidence >= 0.65,

            "artifacts": artifacts,

            "generator": fingerprint["generator"],

            "source": source["source"],

            "metadata_tampered": metadata["metadata_tampered"]

        }