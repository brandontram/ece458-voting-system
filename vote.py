class Vote:
    def __init__(self, voteId, candidateId, timestamp, kioskId, voterId, electionId):
        self.voteId = voteId
        self.candidateId = candidateId
        self.timestamp = timestamp
        self.kioskId = kioskId
        self.voterId = voterId
        self.electionId = electionId
