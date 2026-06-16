#!/usr/bin/env python
"""
🛡️ Vérification d'Intégrité — Système SOC avec IA Cybersécurité
Vérifie que tous les composants du SOC sont correctement installés et configurés
"""

import os
import sys
import json

class SOCIntegrityChecker:
    def __init__(self):
        self.workspace_root = os.path.dirname(os.path.abspath(__file__))
        self.sdi_market_root = os.path.join(self.workspace_root, 'sdi_market')
        self.results = {}
        
    def check_all(self):
        """Exécute tous les contrôles d'intégrité"""
        print("\n" + "="*60)
        print("VERIFICATION D'INTEGRITE — SOC IA CYBERSECURITE")
        print("="*60 + "\n")
        
        self.check_python_files()
        self.check_templates()
        self.check_imports()
        self.check_settings()
        
        self.print_report()
        
    def check_python_files(self):
        """Vérifie les fichiers Python essentiels"""
        print("Verification des fichiers Python...")
        
        required_files = [
            ('marketplace/ai_cybersecurity.py', 'Module IA'),
            ('marketplace/api_security.py', 'API Sécurite'),
            ('marketplace/urls.py', 'Routage URLs'),
        ]
        
        for file_path, description in required_files:
            full_path = os.path.join(self.sdi_market_root, file_path)
            exists = os.path.exists(full_path)
            status = "[OK]" if exists else "[FAIL]"
            print(f"  {status} {description:25} ({file_path})")
            self.results[f"python_{file_path}"] = exists
            
            # Vérifier la taille
            if exists:
                size = os.path.getsize(full_path)
                print(f"      Taille: {size:,} bytes")
    
    def check_templates(self):
        """Vérifie les fichiers templates"""
        print("\nVerification des templates...")
        
        required_templates = [
            ('marketplace/templates/marketplace/security_dashboard.html', 'Dashboard'),
            ('marketplace/templates/marketplace/ai_security_chat.html', 'Chat IA'),
        ]
        
        for file_path, description in required_templates:
            full_path = os.path.join(self.sdi_market_root, file_path)
            exists = os.path.exists(full_path)
            status = "[OK]" if exists else "[FAIL]"
            print(f"  {status} {description:25} ({os.path.basename(file_path)})")
            self.results[f"template_{file_path}"] = exists
    
    def check_imports(self):
        """Vérifie les imports critiques"""
        print("\nVerification des dependances...")
        
        required_modules = [
            ('psutil', 'Monitoring systeme'),
            ('django', 'Framework Django'),
            ('json', 'JSON parsing'),
            ('socket', 'Socket operations'),
            ('subprocess', 'Subprocess handling'),
        ]
        
        for module_name, description in required_modules:
            try:
                __import__(module_name)
                status = "[OK]"
                self.results[f"import_{module_name}"] = True
            except ImportError:
                status = "[FAIL]"
                self.results[f"import_{module_name}"] = False
                
            print(f"  {status} {description:25} (import {module_name})")
    
    def check_settings(self):
        """Vérifie les paramètres Django"""
        print("\nVerification des configurations...")
        
        settings_file = os.path.join(self.sdi_market_root, 'sdi_market', 'settings.py')
        
        if os.path.exists(settings_file):
            print("  [OK] Fichier settings trouve")
            
            with open(settings_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            checks = [
                ('marketplace', "App 'marketplace' installée"),
                ('INSTALLED_APPS', "INSTALLED_APPS définie"),
                ('MIDDLEWARE', "MIDDLEWARE configuré"),
            ]
            
            for check_str, description in checks:
                found = check_str in content
                status = "[OK]" if found else "[WARN]"
                print(f"  {status} {description}")
                self.results[f"settings_{check_str}"] = found
        else:
            print("  [FAIL] Fichier settings non trouve")
            self.results["settings_file"] = False
    
    def print_report(self):
        """Affiche le rapport final"""
        print("\n" + "="*60)
        print("RESUME DE LA VERIFICATION")
        print("="*60 + "\n")
        
        total_checks = len(self.results)
        passed_checks = sum(1 for v in self.results.values() if v)
        
        print(f"Total de verifications: {total_checks}")
        print(f"Reussis: {passed_checks} [OK]")
        print(f"Echoues: {total_checks - passed_checks} [FAIL]")
        print(f"Taux de reussite: {(passed_checks/total_checks*100):.1f}%\n")
        
        if passed_checks == total_checks:
            print("TOUS LES CONTROLES SONT PASSES!")
            print("Le systeme SOC IA est correctement installe et configure.\n")
            return True
        else:
            print("Certains controles ont echoue.")
            print("Veuillez verifier les elements marques [FAIL]\n")
            return False
    
    def check_ai_module(self):
        """Vérifie le module IA spécifiquement"""
        print("\nVerification du module IA...")
        
        ai_file = os.path.join(self.sdi_market_root, 'marketplace', 'ai_cybersecurity.py')
        
        if not os.path.exists(ai_file):
            print("  [FAIL] Module AI non trouve")
            return False
        
        try:
            with open(ai_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            required_classes = [
                'AICybersecurityEngine',
                'SOCPermissions',
            ]
            
            required_methods = [
                'analyze_system_security',
                'analyze_ports',
                'detect_anomalies',
                'ai_process_command',
            ]
            
            print(f"  [OK] Module trouve ({len(content)} chars)")
            
            for class_name in required_classes:
                found = f"class {class_name}" in content
                status = "[OK]" if found else "[FAIL]"
                print(f"  {status} Classe {class_name} trouvee")
                self.results[f"ai_class_{class_name}"] = found
            
            for method_name in required_methods:
                found = f"def {method_name}" in content
                status = "[OK]" if found else "[FAIL]"
                print(f"  {status} Methode {method_name} trouvee")
                self.results[f"ai_method_{method_name}"] = found
            
            return True
        except Exception as e:
            print(f"  [FAIL] Erreur lors de la lecture: {e}")
            return False
    
    def generate_health_report(self):
        """Génère un rapport JSON de santé du système"""
        report = {
            "system": "SOC IA Cybersécurité",
            "version": "2.0",
            "timestamp": __import__('datetime').datetime.now().isoformat(),
            "status": "PASS" if all(self.results.values()) else "WARN",
            "checks_total": len(self.results),
            "checks_passed": sum(1 for v in self.results.values() if v),
            "checks_failed": sum(1 for v in self.results.values() if not v),
            "details": self.results
        }
        
        return report


def main():
    """Fonction principale"""
    checker = SOCIntegrityChecker()
    
    # Exécuter les vérifications
    checker.check_all()
    checker.check_ai_module()
    
    # Générer rapport
    report = checker.generate_health_report()
    
    # Sauvegarder rapport
    report_file = os.path.join(os.path.dirname(__file__), 'soc_health_report.json')
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nRapport sauvegarde: {report_file}")
    except Exception as e:
        print(f"\nImpossible de sauvegarder le rapport: {e}")
    
    # Code de sortie
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
