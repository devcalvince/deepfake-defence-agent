import os
from datetime import datetime


class MetadataAnalyzer:
    """
    Examines metadata for evidence of tampering or
    suspicious characteristics.

    Future versions may use ExifTool or FFprobe.
    """

    def analyze(self, media_path: str):

        if not os.path.exists(media_path):
            return {
                "confidence": 0.0,
                "metadata_tampered": False,
                "artifacts": ["Media not found"]
            }

        file_size = os.path.getsize(media_path)

        modified_time = datetime.fromtimestamp(
            os.path.getmtime(media_path)
        )

        suspicious = file_size == 0

        confidence = 0.80 if suspicious else 0.25

        return {
            "confidence": confidence,
            "metadata_tampered": suspicious,
            "modified_time": modified_time.isoformat(),
            "artifacts": (
                ["Metadata inconsistency"]
                if suspicious
                else []
            )
        }