from utils.classes import Groupe


message = {
        'type': 'football',
        'recipient': [
            Groupe(type='football', status='open', matrice=[[0,1,1,1,1],[1,0,1,0,1],[1,1,0,1,0],[1,0,1,0,1],[0,0,1,1,0]]),
            Groupe(type='handball', status='close', matrice=[[0,0,1,1,0],[1,0,1,1,1],[0,1,0,1,1],[0,0,0,0,1],[1,0,1,1,0]]),
            Groupe(type='politique', status='semi_open', matrice=[[0,1,0,1,1],[1,0,1,1,1],[0,1,0,1,1],[1,1,1,0,1],[0,1,1,1,0]]),
            Groupe(type='informatique', status='open', matrice=[[0,0,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,0,1,1,0]]),
            Groupe(type='biologie', status='close', matrice=[[0,1,0,1,1],[1,0,0,1,1],[0,1,0,1,1],[0,1,1,0,1],[1,0,1,0,0]]),
            Groupe(type='physique', status='open', matrice=[[0,1,0,1,1],[1,0,0,1,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,1,0,0]])
        ]
    }