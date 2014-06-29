import MySQLdb as mdb

def addVoteToDb(vote):
    con = mdb.connect('localhost', 'testuser', 'test', 'VotingSystemDb')
    insert = ("INSERT INTO Votes VALUES (%s, %s, %s, %s, %s, %s)")
    data = (vote.voteId, vote.candidateId, vote.timestamp, vote.kioskId, vote.voterId, vote.electionId)
    cur = con.cursor()
    cur.execute(insert, data)
    con.commit()
    if con:
        con.close()
