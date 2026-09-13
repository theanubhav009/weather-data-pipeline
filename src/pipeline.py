import subprocess
from logger import logger
print("Starting Weather Data Pipeline...")
logger.info("Pipeline started")
print("\n1. Extracting weather data...")
subprocess.run(["python", "src/extract.py"], check=True)

print("\n2. Transforming weather data...")
subprocess.run(["python", "src/transform.py"], check=True)

print("\n3. Loading data into PostgreSQL...")
subprocess.run(["python", "src/load.py"], check=True)

print("\n✅ Weather Data Pipeline completed successfully!")
logger.info("Pipeline completed successfully")