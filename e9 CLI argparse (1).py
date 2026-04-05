import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("targets")
    parser.add_argument("ports")

    args = parser.parse_args()

    print("Targets:", args.targets)
    print("Ports:", parse_ports(args.ports))

if __name__ == "__main__":
    main()