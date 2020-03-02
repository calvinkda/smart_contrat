class Groupe(object):

    status = {
        'open': 0,
        'semi_open': 0.5,
        'close': 1
    }

    def __init__(self, *args, **kwargs):
        self.type_groupe = kwargs.get('type', 'default')
        #la matrice represente celle de l'utilisateur et de leurs relations
        self.matrice = kwargs.get('matrice')
        #le nombre de messages reçu par le groupe
        self.transactions = 1
        self.accepted_msg = 0
        self.rho = 0
        self.status_groupe = kwargs.get('status')

    #calcul de la densite
    def __str__(self):
        return self.accepted_msg

    def dencity(self, *args, **kwargs):
        n = len(self.matrice)
        m = 0
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] == 1:
                    m += 1
        n = n*n   
        dencity = 2*m/(n * (n - 1))
        
        return dencity

    #la valeur associée au type de status

    def get_status_value(self):
        return self.status[self.status_groupe]
        
    #calcul du degré moyen de la communauté
    def community_degre(self, *args, **kwargs):
        
        degres = [ 0 for _ in range(len(self.matrice))]
        n = 0
        for i in range(0, len(self.matrice)):
            for j in range(0, len(self.matrice[i])):
                if self.matrice[i][j] == 1:
                    n += 1
            degres[i] = n
        
        i = (i+1)**2
        
        return sum(degres)/(i*i)

    def acceptation_capacity(self, *args, **kwargs):
        return self.accepted_msg / self.transactions

    def type_subject(self, type_message, *args, **kwargs):
        if type_message != self.type_groupe:
            return 0
        return 1
