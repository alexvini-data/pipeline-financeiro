import logging
import os

def configurar_logger() -> logging.Logger:
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("logs/pipeline.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("pipeline")

logger = configurar_logger()