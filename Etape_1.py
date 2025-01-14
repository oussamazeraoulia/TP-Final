import string
import re
# 
def Pretraitement(corpus):

    # Lecture du document 
    # --------------------------------------------------------------------------------------------------
    def lire_fichier(fichier):
        with open(fichier, 'r') as fichier:
            texte = fichier.read()
        return texte
    
    doc = lire_fichier(corpus) 
    
    # Détecter les phrases et les stocker dans une liste
    # -------------------------------------------------------------------------------------------------

    def stocker_liste(corpus):
        phrases = re.split(r'[.?!]\s*', corpus.strip())  # Séparation avec . ? ou !
        phrases = [phrase for phrase in phrases if phrase]  # Filtrer les phrases vides
        return phrases
    
    doc_liste = stocker_liste(doc)
    
    # Conversion en minuscules
    # ----------------------------------------------------------------------------------------------------

    def minuscules(phrases):
        phrases_minuscules = [phrase.lower() for phrase in phrases]
        return phrases_minuscules

    phrases = minuscules(doc_liste) 
    

    # Tokenisation
    # --------------------------------------------------------------------------------------------------

    def token(phrases_minuscules):
        tokens = [phrase.split() for phrase in phrases_minuscules]
        return tokens
    
    tokens = token(phrases)
    
    # Suppression de la ponctuation
    # ---------------------------------------------------------------------------------------------------
    def supprimer_ponctuation(liste_tokens):
        return [[mot.translate(str.maketrans('', '', string.punctuation)) for mot in phrase] for phrase in liste_tokens]

    supprimer_p = supprimer_ponctuation(tokens)
    # Regroupement des mots
    # -------------------------------------------------------------------------------------------------
    def regroupement(tokens_sans_ponctuation):
        tous_les_mots = [mot for phrase in tokens_sans_ponctuation for mot in phrase]
        return tous_les_mots
    
    
    list_tous_les_mots = regroupement(supprimer_p)
    
    # Supprimer les mots redondants
    # ---------------------------------------------------------------------------------------------------
    def redondants(tous_les_mots):
        mots_uniques = list(set(tous_les_mots))
        return mots_uniques
    
    mots_uniques = redondants(list_tous_les_mots)



    return doc_liste, mots_uniques, list_tous_les_mots


a,b,c = Pretraitement('Corpus_Chirac.txt')

print(a)
    

    






       
