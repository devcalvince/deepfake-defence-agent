# orchestrator/workflow.py

class WorkflowController:
    """
    Maintains execution state of the detection workflow.
    """

    def __init__(self):

        self.state = "INITIALIZED"

    def update(self, state: str):

        self.state = state

    def current(self):

        return self.state