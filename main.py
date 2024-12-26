import argparse
import subprocess


def traceroute(ip_address, progressive=False, output_file=None):
    cmd = ['traceroute', ip_address]

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)

        results = []
        for line in process.stdout:
            print(line.strip())
            results.append(line.strip())

            if progressive:
                input("Appuyez sur Entrée pour continuer...")

        if output_file:
            with open(output_file, 'w') as f:
                f.write('\n'.join(results))
                print(f"Résultats enregistrés dans '{output_file}'")

    except Exception as e:
        print(f"Erreur : {e}")


def main():
    parser = argparse.ArgumentParser(description="Traceroute pour une adresse IP spécifiée.")
    parser.add_argument("ip_address", type=str, help="L'adresse IP à tracer.")
    parser.add_argument("-p", "--progressive", action="store_true", help="Activer l'exécution progressive.")
    parser.add_argument("-o", "--output-file", type=str, help="Fichier dans lequel enregistrer les résultats.")

    args = parser.parse_args()
    traceroute(args.ip_address, args.progressive, args.output_file)


if __name__ == "__main__":
    main()