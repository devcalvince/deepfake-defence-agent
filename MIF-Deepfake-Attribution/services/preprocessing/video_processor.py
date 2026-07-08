# services/preprocessing/video_processor.py

import os

from services.preprocessing.frame_extractor import FrameExtractor


class VideoProcessor:
    """
    Central preprocessing service.

    Responsible for preparing
    video assets before entering
    the Multi-Agent Intelligence Framework.
    """

    def __init__(self):

        self.frame_extractor = FrameExtractor()

    def prepare_video(self, video_path: str):

        if not os.path.exists(video_path):
            raise FileNotFoundError(video_path)

        frames = self.frame_extractor.extract_frames(
            video_path
        )

        return {
            "video_path": video_path,
            "frames": frames
        }