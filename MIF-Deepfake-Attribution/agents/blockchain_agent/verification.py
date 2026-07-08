import json
import os
from typing import Dict, Any


class BlockchainVerifier:
    """
    Verifies whether forensic evidence has been
    successfully anchored inside the local immutable ledger.

    This implementation currently verifies against a local JSON
    ledger but can later be replaced with Ethereum,
    Hyperledger Fabric, Polygon, Quorum, etc.
    """

    LEDGER_FILE = "logs/audits/blockchain_ledger.json"

    def verify(self, evidence_hash: str) -> Dict[str, Any]:

        if not os.path.exists(self.LEDGER_FILE):
            return {
                "verified": False,
                "anchored": False,
                "transaction_hash": None,
                "block_number": None,
                "timestamp": None,
                "reason": "Ledger file not found."
            }

        try:
            with open(self.LEDGER_FILE, "r") as f:
                ledger = json.load(f)

            for record in ledger:

                if record.get("evidence_hash") == evidence_hash:

                    return {
                        "verified": True,
                        "anchored": True,
                        "transaction_hash": record.get("transaction_hash"),
                        "block_number": record.get("block_number"),
                        "timestamp": record.get("timestamp"),
                        "reason": None
                    }

            return {
                "verified": False,
                "anchored": False,
                "transaction_hash": None,
                "block_number": None,
                "timestamp": None,
                "reason": "Evidence hash not found in ledger."
            }

        except json.JSONDecodeError:
            return {
                "verified": False,
                "anchored": False,
                "transaction_hash": None,
                "block_number": None,
                "timestamp": None,
                "reason": "Ledger file is corrupted."
            }

        except Exception as e:
            return {
                "verified": False,
                "anchored": False,
                "transaction_hash": None,
                "block_number": None,
                "timestamp": None,
                "reason": str(e)
            }