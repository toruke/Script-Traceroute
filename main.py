import argparse
import scapy.all as scapy

def main():
    parser = argparse.ArgumentParser(description="trace the route of the ip address specifie")
    parser.add_argument("ip_address", type=str, help="the ip address to trace")
    parser.add_argument("-p", "--progressive", action="store_true")
    parser.add_argument("-o", "--output-file", type=str, help="the output file")

    args = parser.parse_args()
    ip_address = args.ip_address
    output_file = args.output

    if args.progressive:
        pass                            #ajouter une execution progressive

    if output_file:
        try:
            with open(output_file, "w") as f:
                f.write(ip_address)
            print(f"Fichier '{output_file}' créé avec succès, contenant l'adresse IP.")
        except Exception as e:
            print(f"Error in the creation of the file : {e}")


if __name__ == '__main__':
    main()