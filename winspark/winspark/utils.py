import random
import os
from backports import configparser as cfg

import random
from pyspark.sql import DataFrame

def printc(*args, num_rows: int = 20, truncate: bool = True) -> None:
    color_rng_1 = list(range(31, 47))
    color_rng_2 = list(range(91, 108))
    color_rng_1.extend(color_rng_2)
    numbs = [i for i in color_rng_1 if i not in [97, 98, 99, 35, 37, 38, 39, 100, 7, 107, 90, 30, 40]]
    numb = random.choice(numbs)
    if len(args) == 1 and isinstance(args[0], DataFrame):
        df = args[0]
        df_str = df._jdf.showString(num_rows, truncate)
        clr_df_str = f"\033[{numb}m{df_str}\033[0m"
        print(clr_df_str)
    else:
        for in_text in args:
            clr_text = f"\033[{numb}m{str(in_text)}\033[0m"
            print(clr_text, end='\n')



def setWIN_OS_Environment(config) -> None:
    hadoop_path = config.get('framework-variables', 'hadoop_path')
    if not os.path.exists(hadoop_path):
        raise ValueError(f"Invalid Hadoop path: {hadoop_path}. Please check your configuration.")
    os.environ["HADOOP_HOME"] = hadoop_path
    os.environ["hadoop.home.dir"] = hadoop_path
    hadoop_bin_path = f"{hadoop_path}\\bin"
    if hadoop_bin_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + hadoop_bin_path


def configs() -> cfg.ConfigParser:
    config = cfg.ConfigParser()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file = os.path.join(base_dir, "configs.properties")
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found at {config_file}")
    config.read(config_file)
    return config
