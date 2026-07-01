from typing import Dict, Any

class ConsensusEngine:
    def __init__(self):
        # Scientific weighting factor balancing agent reliability (Must sum to 1.0)
        # Visual and Audio typically hold the highest detection priority
        self.weights = {
            "visual_agent": 0.35,
            "audio_agent": 0.25,
            "biometric_agent": 0.20,
            "forensic_agent": 0.10,
            "semantic_agent": 0.10
        }
        self.suspicious_threshold = 0.65 # Anything above 65% total is flagged

    def calculate_fusion_verdict(self, agent_outputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Applies a weighted consensus fusion algorithm across all processed modalities
        to determine the final deepfake attribution score.
        """
        total_weighted_score = 0.0
        active_weights_sum = 0.0
        collected_artifacts = []

        for agent, payload in agent_outputs.items():
            if agent in self.weights and payload is not None:
                confidence = payload.get("confidence", 0.0)
                weight = self.weights[agent]
                
                # Accumulate the weighted confidence math
                total_weighted_score += (confidence * weight)
                active_weights_sum += weight
                
                # Collect detected forensic fingerprints
                if payload.get("is_fake", False):
                    collected_artifacts.extend(payload.get("artifacts", []))

        # Normalize score if an agent failed to return data during pipeline execution
        final_score = (total_weighted_score / active_weights_sum) if active_weights_sum > 0 else 0.0
        final_score = round(final_score, 4)

        # Classify final system verdict based on mathematical thresholds
        if final_score >= self.suspicious_threshold:
            verdict = "SUSPICIOUS"
        elif final_score >= 0.40:
            verdict = "REVIEWS_NEEDED"
        else:
            verdict = "AUTHENTIC"

        return {
            "overall_verdict": verdict,
            "final_score": final_score,
            "aggregated_artifacts": list(set(collected_artifacts)) # Deduplicate tags
        }
