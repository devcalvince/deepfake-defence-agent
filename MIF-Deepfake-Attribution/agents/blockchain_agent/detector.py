from agents.blockchain_agent.hash_generator import HashGenerator
from agents.blockchain_agent.ledger_connector import LedgerConnector
from agents.blockchain_agent.verification import BlockchainVerifier


class BlockchainAgent:
    """
    Blockchain Intelligence Agent

    Responsibilities
    ----------------
    • Generate forensic evidence hash
    • Anchor evidence into the immutable ledger
    • Verify ledger integrity
    """

    def __init__(self):

        self.hasher = HashGenerator()
        self.ledger = LedgerConnector()
        self.verifier = BlockchainVerifier()

    def analyze(self, consensus_result: dict):
        """
        Anchors the final consensus result into the forensic ledger.
        """

        # Build a deterministic fingerprint from the consensus result
        fingerprint = (
            f"{consensus_result['overall_verdict']}"
            f"{consensus_result['final_score']}"
            f"{sorted(consensus_result['aggregated_artifacts'])}"
        )

        # Generate SHA-256 evidence hash
        evidence_hash = self.hasher.generate(fingerprint)

        # Store inside ledger
        receipt = self.ledger.anchor(evidence_hash)

        # Verify successful anchoring
        verification = self.verifier.verify(evidence_hash)

        return {

            "agent_name": "Blockchain Agent",

            "evidence_hash": evidence_hash,

            "transaction_hash": receipt["transaction_hash"],

            "block_number": receipt["block_number"],

            "timestamp": receipt.get("timestamp"),

            "anchored": verification["anchored"],

            "verified": verification["verified"],

            "reason": verification["reason"]

        }