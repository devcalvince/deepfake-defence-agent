import hashlib
import os


class HashGenerator:
    """
    Generates SHA-256 cryptographic hashes for forensic evidence.

    Supports hashing:
    - Text
    - Files (videos, images, audio)
    """

    @staticmethod
    def generate(text: str) -> str:
        """
        Generate SHA-256 hash from a string.
        """
        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def generate_file_hash(file_path: str) -> str:
        """
        Generate SHA-256 hash from a file.

        Reads the file in chunks to support very large
        video files without excessive memory usage.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()