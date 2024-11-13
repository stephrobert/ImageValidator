import logging
import yaml


def setup_logging(config_path="logging_config.yaml"):
    # Charge le fichier YAML comme un dictionnaire
    with open(config_path, "r") as file:
        logging_config = yaml.safe_load(file)

    # Vérifie si le chargement a produit un dictionnaire
    if not isinstance(logging_config, dict):
        raise ValueError(
            "Le fichier de configuration de logging doit être un dictionnaire."
        )

    # Utilisez le dictionnaire pour configurer le logging
    log_format = logging_config.get(
        "format", "%(asctime)s - %(levelname)s - %(message)s"
    )
    log_level = logging_config.get("level", "INFO")

    # Configure le logging
    logging.basicConfig(level=log_level, format=log_format)
