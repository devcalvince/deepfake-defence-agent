# orchestrator/scheduler.py

class PipelineScheduler:
    """
    Controls execution order of every intelligence module.
    """

    def __init__(self):

        self.pipeline = [

            "visual_agent",

            "audio_agent",

            "biometric_agent",

            "semantic_agent",

            "forensic_agent",

            "consensus_engine",

            "blockchain"
        ]

    def execution_order(self):

        return self.pipeline