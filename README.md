Voici une version mise à jour du fichier `README.md` avec la section de débogage
ajoutée et des corrections sur d'autres parties :

---

# ImageValidator

**ImageValidator** est un outil Python conçu pour vérifier la conformité des
images de machines virtuelles (VM) avant leur déploiement en environnement
cloud. Il permet de valider des éléments critiques comme les drivers, la
configuration réseau, les services de démarrage et bien plus encore, afin
d'assurer que chaque image est prête pour les principales plateformes cloud
(AWS, Azure, GCP, OpenStack, etc.).

## Fonctionnalités

- **Validation de conformité des disques** : Vérifie la structure et le format
  des partitions.
- **Vérification des drivers essentiels** : S'assure de la présence de drivers
  requis comme `virtio`.
- **Contrôle des utilisateurs** : Vérifie l'existence d'un utilisateur configuré
  pour l'administration.
- **Services au démarrage** : S'assure que `cloud-init`, `SSH` et autres
  services requis sont bien activés.
- **Paramètres GRUB** : Analyse et valide la ligne de commande du bootloader.
- **Rapports de conformité** : Génère un rapport de validation pour chaque image
  vérifiée.

## Prérequis

- **Python** 3.10 ou plus
- **libguestfs** installé pour manipuler les images de VM
- **pyyaml** pour la gestion des fichiers de configuration en YAML

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre_nom/ImageValidator.git
   cd ImageValidator
   ```

2. Installez KVM comme documenté [ici](https://blog.stephane-robert.info/docs/virtualiser/type1/kvm/).
3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Assurez-vous que **libguestfs** est installé avec toutes ses dépendances
   systèmes et correctement configuré pour interagir avec les images de disques
   virtuels.

5. Installez le projet en mode développement :

   ```bash
   pip install -e .
   ```

Une fois installé, vous pouvez utiliser la commande `image-validator` pour
lancer l'application.

## Débogage

Pour déboguer le programme dans VSCode :

1. Assurez-vous que le fichier de configuration `.vscode/launch.json` est
   correctement configuré :

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Debug image-validator",
               "type": "debugpy",
               "request": "launch",
               "program": "${workspaceFolder}/launch_image_validator.py",
               "console": "integratedTerminal",
               "justMyCode": true
           }
       ]
   }
   ```

2. Pour déboguer directement dans le terminal sans VSCode, lancez le script
   suivant à la racine du projet :

   ```bash
   python launch_image_validator.py --config config.yaml
   ```

## Contribution

Nous accueillons toutes les contributions pour enrichir le projet
ImageValidator. Que vous soyez développeur, testeur ou utilisateur, chaque
participation est la bienvenue !

### Règles de Contribution

1. **Forkez le dépôt** et clonez-le en local.
2. **Créez une branche** pour vos modifications :

   ```bash
   git checkout -b feature/ma-fonctionnalité
   ```

3. **Commitez vos changements** en suivant le format suivant :
   - Message clair et concis pour décrire le changement, par exemple : `feat:
     ajout de la vérification des utilisateurs`.
   - Évitez les modifications volumineuses dans un même commit.
4. **Poussez votre branche** vers GitHub :

   ```bash
   git push origin feature/ma-fonctionnalité
   ```

5. **Ouvrez une Pull Request** :
   - Ajoutez une description détaillée de votre modification.
   - Liez les issues associées (le cas échéant).

### Bonnes Pratiques

- **Respectez la structure du code** : Placez vos fichiers dans les dossiers
  appropriés (`src/`, `tests/`, etc.).
- **Écrivez des tests** : Toute nouvelle fonctionnalité doit être accompagnée de
  tests unitaires pour en garantir la robustesse.
- **Documentez vos modifications** : Si vous ajoutez une fonctionnalité, pensez
  à mettre à jour le README ou les fichiers de documentation concernés.

## Roadmap

- **Version 0.1** : Fonctionnalités de validation de base (disques, drivers,
  services, GRUB).
- **Version 0.2** : Ajout des fonctionnalités correctives (modification des
  paramètres GRUB, installation de packages).
- **Version 0.3** : Ajout de la compatibilité multi-cloud avec des
  configurations spécifiques à chaque fournisseur (AWS, Azure, GCP).

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de
détails.

## Contact et Support

Si vous avez des questions ou des suggestions, n’hésitez pas à **ouvrir une
issue** ou à rejoindre la section **Discussions** du projet. Nous sommes là pour
vous aider !

