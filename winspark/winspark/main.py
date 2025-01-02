
import sys
from winspark.utils import setWIN_OS_Environment, configs
from winspark.spark_utils import getSparkSession, stop_sess

def main():
    # Simulate loading configurations
    config = configs()

    # Set up the Windows environment
    try:
        setWIN_OS_Environment(config)
        print("Environment setup successful.")
    except ValueError as e:
        print(f"Error in environment setup: {e}")
        sys.exit(1)

    # Initialize Spark session
    spark = getSparkSession()

    # Example Spark operations
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    columns = ["Name", "Age"]
    df = spark.createDataFrame(data, columns)

    print("Displaying DataFrame:")
    df.show()

    # Stop Spark session
    stop_sess(spark)

if __name__ == "__main__":
    main()
