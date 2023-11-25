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

df = pd.DataFrame(columns=["machineid", "ip_addr", "security", "sub_net"])
COUNT_SUBNET = None
COUNT_SECURITY = None
SUBNET_SECURITY = None


def main(file):
    global df,  COUNT_SUBNET, COUNT_SECURITY, SUBNET_SECURITY
    with open(file, "r", encoding="utf-8") as f:
        r = f.readlines()

    for i in r:
        i = i.split("|")
        if "machineid" in i:
            continue
        machineid = i[0]
        ip_addr = i[1]
        security_group = i[2].split(",")
        if "\n" not in i[3]:
            subnet = i[3]
        else:
            subnet = i[3][:-1]

        for security in security_group:
            for sub_net in subnet.split(","):
                dict1 = {
                    "machineid": machineid,
                    "ip_addr": ip_addr,
                    "security": security,
                    "sub_net": sub_net,
                }
                df1 = pd.DataFrame([dict1])
                df = pd.concat([df, df1], ignore_index=True)

    COUNT_SUBNET = df["sub_net"].value_counts()
    COUNT_SECURITY = df["security"].value_counts()
    SUBNET_SECURITY = df.groupby(["sub_net", "security"]).value_counts()
    print("Dataframe format : \n")
    return df


print(main(args.file))
if args.analysis:
    print("count of usage of each subnet : \n", COUNT_SUBNET)
    print("count of usage of each security group : \n", COUNT_SECURITY)
    print(
        "count of usage of subnet + security group combinations : \n", SUBNET_SECURITY
    )
