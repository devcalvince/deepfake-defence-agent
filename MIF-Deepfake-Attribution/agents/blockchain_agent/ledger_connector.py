import json
import os
import uuid
from datetime import datetime
from typing import Dict


class LedgerConnector:
    """
    Local immutable ledger simulator.

    This simulates blockchain anchoring for the MIF project.
    It can later be replaced with:

    - Ethereum
    - Hyperledger Fabric
    - Polygon
    - Quorum
    """

    LEDGER_DIRECTORY = "logs/audits"
    LEDGER_FILE = os.path.join(
        LEDGER_DIRECTORY,
        "blockchain_ledger.json"
    )

    def __init__(self):

        os.makedirs(self.LEDGER_DIRECTORY, exist_ok=True)

        if not os.path.exists(self.LEDGER_FILE):
            with open(self.LEDGER_FILE, "w") as f:
                json.dump([], f)

    def anchor(self, evidence_hash: str) -> Dict:

        transaction_hash = str(uuid.uuid4())

        block_number = int(datetime.utcnow().timestamp())

        record = {
            "transaction_hash": transaction_hash,
            "block_number": block_number,
            "timestamp": datetime.utcnow().isoformat(),
            "evidence_hash": evidence_hash
        }

        with open(self.LEDGER_FILE, "r") as f:
            ledger = json.load(f)

        ledger.append(record)

        with open(self.LEDGER_FILE, "w") as f:
            json.dump(ledger, f, indent=4)

        return {
            "transaction_hash": transaction_hash,
            "block_number": block_number,
            "anchored": True
        }