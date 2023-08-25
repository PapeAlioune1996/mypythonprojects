class Etudiant :
    def __init__(self,nom, classe) :
        self.nom = nom
        self.classe = classe 

class Classe:
    def __init__(self,nom, niveau):
        self.nom = nom 
        self.niveau = niveau 
        self.etudiants=[]
    
    def ajouetEtudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def supprimerEtudiant(self,etudiant):
        self.etudiants.remove(etudiant)


class Ecole:
    def __init__(self,nom):
        self.nom = nom 
        self.classes=[]

    def ajouterClasse(self, classe):
        self.classes.append(classe)
    
    def supprimerClasse(self,classe):
        self.classes.remove(classe)

    def rechercheEtudiant(self,nom):
        for classe in self.classes:
            for etudiant in classe.etudiants:
                if etudiant.nom == nom:
                    return etudiant


