# src/main.py
import click
import logging
from imagevalidator.config import Config
from imagevalidator.log_config import setup_logging
from imagevalidator.imagevm import ImageVM


@click.command()
@click.option(
    "--config",
    "-c",
    default="config.yaml",
    help="Path to the config file",
    show_default=True,
)
@click.option(
    "--image",
    "-i",
    required=True,
    help="Nom de l'image à charger pour la validation",
)
def main(config, image):
    # Configurer la journalisation
    setup_logging(config)
    logging.info("Démarrage de l'application ImageValidator")

    # Charger la configuration
    config = Config(config)

    # Créer une instance de ImageVM pour la validation de l'image
    try:
        vm = ImageVM(config, image)
        vm.analyze()
    except Exception as e:
        logging.error(f"Erreur lors de la validation de l'image {image} : {e}")

    logging.info("Validation terminée.")


if __name__ == "__main__":
    main()
