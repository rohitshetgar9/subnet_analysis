"""
python program to convert the given file to the required format
use this to run the program  python testing.py --file=file.csv --analysis=true.
Note: --analysis=true is optional
"""
import argparse
import pandas as pd

pd.set_option("display.max_rows", None)


parser = argparse.ArgumentParser(description="processing data from file")
parser.add_argument("--file", required=True)
parser.add_argument("--analysis", default=False)
args = parser.parse_args()

COUNT_SUBNET = None
COUNT_SECURITY = None
SUBNET_SECURITY = None


def main(file):
    global COUNT_SUBNET, COUNT_SECURITY, SUBNET_SECURITY
    
    # Read the first line of the file to get column names
    with open(file, "r", encoding="utf-8") as f:
        columns = f.readline().strip().split("|")

    # Read the rest of the file and create a DataFrame
    df = pd.read_csv(file, sep="|", skiprows=1, names=columns, skipinitialspace=True)
   
    COUNT_SUBNET = df["subnet"].value_counts()
    COUNT_SECURITY = df["security-group"].value_counts()
    SUBNET_SECURITY = df.groupby(["subnet", "security-group"]).size().reset_index(name="count")
    print("Dataframe format : \n")
    return df


print(main(args.file))
if args.analysis:
    print("count of usage of each subnet : \n", COUNT_SUBNET)
    print("count of usage of each security group : \n", COUNT_SECURITY)
    print(
        "count of usage of subnet + security group combinations : \n", SUBNET_SECURITY
    )
