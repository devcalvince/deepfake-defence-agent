# services/preprocessing/frame_extractor.py

import os
import uuid
import cv2
from typing import List


class FrameExtractor:
    """
    Extracts frames from an uploaded video.

    Frames are stored temporarily and reused by
    multiple intelligence agents.
    """

    def __init__(self):

        self.output_root = "datasets/temp_frames"

        os.makedirs(self.output_root, exist_ok=True)

    def extract_frames(
        self,
        video_path: str,
        sample_rate: int = 10
    ) -> List[str]:
        """
        Parameters
        ----------
        video_path : str

        sample_rate :
            Save one frame every N frames.

        Returns
        -------
        List[str]
        """

        capture = cv2.VideoCapture(video_path)

        frame_paths = []

        frame_index = 0

        session = str(uuid.uuid4())

        session_dir = os.path.join(
            self.output_root,
            session
        )

        os.makedirs(session_dir, exist_ok=True)

        while True:

            success, frame = capture.read()

            if not success:
                break

            if frame_index % sample_rate == 0:

                frame_name = f"frame_{frame_index:05d}.jpg"

                frame_path = os.path.join(
                    session_dir,
                    frame_name
                )

                cv2.imwrite(frame_path, frame)

                frame_paths.append(frame_path)

            frame_index += 1

        capture.release()

        return frame_paths