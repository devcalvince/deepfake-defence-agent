from agents.semantic_agent.contextual_validation import ContextualValidator
from agents.semantic_agent.scene_analysis import SceneAnalyzer
from agents.semantic_agent.weather_checker import WeatherConsistencyChecker


class SemanticAgent:
    """
    Semantic Intelligence Agent

    Performs:

    • Context validation

    • Scene analysis

    • Environmental consistency analysis

    Produces one semantic confidence score
    for the Consensus Engine.
    """

    def __init__(self):

        self.context_validator = ContextualValidator()

        self.scene_analyzer = SceneAnalyzer()

        self.weather_checker = WeatherConsistencyChecker()

    def analyze(self, frame_paths: list[str]):

        context = self.context_validator.analyze(frame_paths)

        scene = self.scene_analyzer.analyze(frame_paths)

        weather = self.weather_checker.analyze(frame_paths)

        confidence = round(

            (

                context["confidence"]

                + scene["confidence"]

                + weather["confidence"]

            )

            / 3,

            4

        )

        artifacts = list(

            set(

                context["artifacts"]

                + scene["artifacts"]

                + weather["artifacts"]

            )

        )

        return {

            "agent_name": "Semantic Agent",

            "confidence": confidence,

            "is_fake": confidence >= 0.65,

            "artifacts": artifacts

        }