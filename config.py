import os

class Config:
    output_directory = os.getenv("TAILDB_EXPORTER_OUTPUT_DIR", None)
