# src/imagevalidator/imagevm.py

import logging
import guestfs


class ImageVM:
    def __init__(self, config, image_name):
        """
        Initialise l'instance de ImageVM, charge l'image et configure guestfs.
        """
        self.config = config.config
        self.image_name = image_name
        self.g = guestfs.GuestFS()

        # Charger et lancer l'image
        try:
            logging.info(f"Initialisation de l'image : {image_name}")
            self.g.add_drive(image_name, readonly=1)
            self.g.launch()
            logging.info("Image chargée et instance guestfs lancée.")
        except Exception as e:
            logging.error(f"Erreur lors du chargement de l'image {image_name} : {e}")
            raise

    def analyze(self):
        """
        Méthode principale pour analayser l'image VM.
        """
        logging.info(f"Début de la validation de l'image : {self.image_name}")

        try:
            # Obtenir la liste des partitions bootables de l'image
            devices = self.g.inspect_os()
            device = devices[0]
            operating_system = self.g.inspect_get_product_name(device)
            logging.info(f"Type de l'OS : {operating_system}")
            logging.info(f"Montage de la partition {device}")
            # Montez le système de fichiers dans le point par défaut "/"
            self.g.mount(device, "/")
            # Initialisez Augeas avec le système de fichiers monté
            self.g.aug_init("/", 0)
            for key in self.config["analyzers"]["config_keys"]:
                if "regexp" not in self.config["analyzers"]["config_keys"][key]:
                    config_value = self.get_config(
                        "/files%s" % self.config["analyzers"]["config_keys"][key]
                    )
                    logging.info(
                        f"Contenu de la ligne {key}: {config_value}"
                        if len(config_value) > 50
                        else f"Contenu de la ligne {key}: {config_value}"
                    )
                else:
                    match_value = self.match_config(
                        "/files%s" % self.config["analyzers"]["config_keys"][key]
                    )
                    logging.info(
                        f"Contenu de la ligne {key}: {match_value}"
                        if len(match_value) > 50
                        else f"Contenu de la ligne {key}: {match_value}"
                    )
            # Fermez Augeas et libérez ses ressources
            kernel_version = self.g.ls("/lib/modules/")[0]
            logging.info(f"Version du noyau trouvée : {kernel_version}")
            if kernel_version:
                drivers_net = self.g.ls(
                    f"/lib/modules/{kernel_version}/kernel/drivers/"
                )
                drivers_net_str = ", ".join(drivers_net)
                logging.info(
                    f"Pilotes trouvés pour le noyau {kernel_version} : {drivers_net_str}"
                )
            apps = self.g.inspect_list_applications(device)

            app_name_release_list = [
                f"{app['app_name']} {app['app_release']}" for app in apps
            ]
            logging.info(f"Applications trouvées : {app_name_release_list}")

            # Fermez le système de fichiers monté
            self.g.aug_close()
            # Démontez le système de fichiers après la validation
            self.g.umount_all()
            logging.info(
                f"Validation de l'image {self.image_name} terminée avec succès."
            )
        except Exception as e:
            logging.error(
                f"Erreur lors de la validation de l'image {self.image_name} : {e}"
            )
        return ""

    def get_drivers(self):
        """
        Vérifie la présence des drivers essentiels dans l'image.
        """
        logging.info("Vérification des drivers nécessaires.")
        # Exemple de vérification de driver

    def get_services(self):
        """
        Vérifie que les services nécessaires sont actifs dans l'image.
        """
        logging.info("Vérification des services essentiels.")
        services = []
        for service in services:
            logging.info(
                f"Service {service} : {self.g.inspect_get_service_status(service)}"
            )
        # Exemple de vérification de services

    def get_config(self, node):
        """
        Récupère la valeur du noeud augeas.
        """
        try:
            param = self.g.aug_get(node)
        except Exception as e:
            logging.error(
                f"An error occurred while getting the value of the node : {e}"
            )
            param = "Undef"
        return param

    def match_config(self, node):
        """
        Récupère la valeur du noeud augeas.
        """
        try:
            param = self.g.aug_match(node)
        except Exception as e:
            logging.error(
                f"An error occurred while getting the value of the node : {e}"
            )
            param = "Undef"
        return param

    def __del__(self):
        """
        Ferme et nettoie l'instance guestfs lorsque l'objet est détruit.
        """
        logging.info(f"Nettoyage de l'instance pour l'image : {self.image_name}")
        try:
            self.g.shutdown()
            self.g.close()
            logging.info("Instance guestfs fermée.")
        except Exception as e:
            logging.error(f"Erreur lors de la fermeture de l'instance guestfs : {e}")
