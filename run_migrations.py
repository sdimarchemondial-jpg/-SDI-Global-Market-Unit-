#!/usr/bin/env python
import os

def run_migrations():
    print("=== APPLICATION DES MIGRATIONS ===")

    # Changer de répertoire
    os.chdir('sdi_market')

    # Exécuter la commande migrate
    command = 'python manage.py migrate --verbosity=2'
    print(f"Exécution: {command}")

    result = os.system(command)
    print(f"Code de retour: {result}")

    if result == 0:
        print("✓ Migrations appliquées avec succès!")
    else:
        print(f"✗ Erreur lors de l'application des migrations (code: {result})")

if __name__ == '__main__':
    run_migrations()