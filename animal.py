MIN_ENERGIE = 15

def creer_animal(age=0, jrs_gestation=0, energie=MIN_ENERGIE, disponible=True):
   
    
    
    animal = {'age' : age, 'jrs_gestation' :  jrs_gestation, 'energie' : energie, 'disponible' : disponible} 
    print('caca')
    return animal



def obtenir_age(animal):
    # TODO: Retourner la valeur de l'âge de l'animal donné (Int)
    
    age = animal.get('age')
    return age
    pass


def obtenir_jours_gestation(animal):
    # TODO: Retourner le nombre de jours de gestation de l'animal donné (Int)
    
     # TODO: Retourner la valeur de l'âge de l'animal donné (Int)
    
    jgst = animal.get('jrs_gestation')
    return jgst
    pass


def obtenir_energie(animal):
    # TODO: Retourner la quantité d'énergie de l'animal donné (Int)
    nrg = animal.get('energie')
    return nrg
    pass


def obtenir_disponibilite(animal):
    # TODO: Retourner l'état de disponibilité de l'animal (Booléen)
    dsp = animal.get('disponible')
    return dsp
    pass


def incrementer_age(animal, puberte):
    # TODO: Incrémenter l'âge de l'animal de 1
    if animal['age'] > puberte:
        animal['jrs_gestation'] += 1
    animal['age'] += 1
    # TODO: Si l'animal est plus âgé que l'âge de la puberté, incrémenter son nombre de jours de gestation de 1
    pass


def definir_jours_gestation(animal, jrs_gest):
    # TODO: Mettre à jour le nombre de jours de gestation de l'animal avec la valeur jrs_gest donnée (Int)
    
    animal['jrs_gestation'] = jrs_gest
    
    pass


def ajouter_energie(animal, valeur):
    # TODO: Ajouter la quantité d'énergie donnée (valeur) à l'énergie actuelle de l'animal (Int)
    animal['energie'] = valeur
    pass


def definir_disponibilite(animal, permis):
    # TODO: Mettre à jour l'état de disponibilité de l'animal en utilisant le paramètre permis (Booléen)
    animal['disponible'] = permis
    pass

