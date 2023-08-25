from fastai.vision import *
from PIL import Image

def generate_creature_from_person(person_image_path, creature_image_path, output_image_path):
    # Charger l'image de la personne et de la créature
    person_img = open_image(person_image_path)
    creature_img = open_image(creature_image_path)

    # Entraîner le modèle pour effectuer le transfert de style
    learner = cnn_learner(dls=DataLoaders.from_folder('data'), arch=resnet34)
    learner.fine_tune(1)

    # Appliquer le transfert de style sur l'image de la créature en utilisant le visage de la personne
    stylized_img = learner.predict(person_img)[0]

    # Combinaison de l'image stylisée et de l'image de la créature
    final_img = creature_img.data * 0.8 + stylized_img.data * 0.2

    # Enregistrement de l'image finale résultante
    final_img = Image(final_img)
    final_img.save(output_image_path)

# Exemple d'utilisation du programme
generate_creature_from_person("C:/Users/DELL/Desktop/MyPythonExercises/sm1.jpg",
                             "C:/Users/DELL/Desktop/MyPythonExercises/lion.jpg",
                             "C:/Users/DELL/Desktop/MyPythonExercises/sm.jpg")
