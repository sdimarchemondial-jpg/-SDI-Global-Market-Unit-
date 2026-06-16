# 🛡️ Guide d'Utilisation — SOC avec Assistant IA Cybersécurité

**Version:** 2.0  
**Date:** 2026-05-15  
**Public:** Administrateurs, Analystes SOC, Managers Sécurité  

---

## 📖 Table des Matières

1. [Accès et Interface](#accès-et-interface)
2. [Dashboard SOC](#dashboard-soc)
3. [Assistant IA Chat](#assistant-ia-chat)
4. [Commandes IA](#commandes-ia)
5. [Modules de Sécurité](#modules-de-sécurité)
6. [Permissions et Rôles](#permissions-et-rôles)
7. [Bonnes Pratiques](#bonnes-pratiques)

---

## 🔐 Accès et Interface

### Prérequis
- ✅ Compte administrateur (is_staff = True)
- ✅ Navigateur moderne (Chrome, Firefox, Edge)
- ✅ Connexion à Internet

### Accès au Dashboard
```
URL: http://localhost:8000/api/security-dashboard/
OU accès direct via le menu Admin
```

### Interface Principale
```
┌─────────────────────────────────────────────┐
│  🛡️ Centre de Surveillance Cybersécurité   │
│  Intelligence artificielle • 24/7 • Avancée │
│                                  🔄 Actual. │
└─────────────────────────────────────────────┘
│
├─ KPIs EN TEMPS RÉEL
│  ├─ 🚨 Alertes Actives
│  ├─ 🤖 Score IA Menace
│  ├─ 🌐 Connexions Actives
│  ├─ 🚫 IPs Bloquées
│  ├─ 🎯 Bots Détectés
│  └─ ⚡ Performance (CPU/RAM)
│
├─ MODULES DE SÉCURITÉ
│  ├─ 🔍 Surveillance Ports
│  ├─ 🤖 Analyse IA Temps Réel
│  ├─ 🎣 Événements Honeypot
│  ├─ 📈 Graphiques Live
│  ├─ 💻 Console Temps Réel
│  ├─ 🚨 Alertes Sécurité
│  ├─ ⚙️ État du Système
│  ├─ 🔓 Tableau des Failles
│  ├─ 💡 Recommandations IA
│  └─ ⚙️ Configuration Monitoring
│
└─ 💬 CHAT IA (Coin bas-droit)
   └─ Assistant IA 24/7
```

---

## 📊 Dashboard SOC

### Zone 1: KPIs Principaux (6 cartes)

#### 🚨 Alertes Actives
```
┌────────────────────────────┐
│ Alertes Actives            │
│                            │
│ 🚨 12                      │
│                            │
│ Critiques: 2               │
│ Résolues: 5                │
└────────────────────────────┘
```
- **Valeur**: Nombre d'alertes non résolues
- **Action**: Cliquer pour filtrer alertes critiques
- **Interprétation**: ≤5 = Bon | 5-10 = Moyen | >10 = Critique

#### 🤖 Score IA Menace
```
┌────────────────────────────┐
│ Score IA Menace            │
│                            │
│ 35.2                       │
│                            │
│ 🟢 Faible                  │
│ Confiance: 94%             │
└────────────────────────────┘
```
- **Échelle**: 0-100 (0=Sûr, 100=Critique)
- **Niveau**: Faible (0-20) → Sûre (20-40) → Moyen (40-60) → Haute (60-80) → Critique (80+)
- **Couleur**: 🟢 Vert ≤40 | 🟡 Orange 40-70 | 🔴 Rouge ≥70

#### 🌐 Connexions Actives
```
┌────────────────────────────┐
│ Connexions Actives         │
│                            │
│ 47                         │
│                            │
│ Trafic: 234.5 MB           │
└────────────────────────────┘
```
- **Nombre**: Connexions TCP établies
- **Trafic**: Données transférées

#### 🚫 IPs Bloquées
```
┌────────────────────────────┐
│ IPs Bloquées               │
│                            │
│ 23                         │
│                            │
│ Tentatives: 156            │
└────────────────────────────┘
```
- **IPs**: Adresses IP en liste noire
- **Tentatives**: Requêtes bloquées

#### 🎯 Bots Détectés
```
┌────────────────────────────┐
│ Bots Détectés              │
│                            │
│ 8                          │
│                            │
│ Honeypot: 3                │
└────────────────────────────┘
```
- **Bots**: Crawlers, scanners détectés
- **Honeypot**: Bots tombés dans les pièges

#### ⚡ Performance
```
┌────────────────────────────┐
│ Performance                │
│                            │
│ 125 ms                     │
│                            │
│ CPU: 34% | RAM: 67%        │
└────────────────────────────┘
```
- **Réponse**: Temps réponse système
- **CPU/RAM**: Usage ressources

---

### Zone 2: Surveillance des Ports (Grid)

```
┌─ Port 80 ─┐    ┌─ Port 443 ─┐   ┌─ Port 22 ──┐
│ OUVERT    │    │ OUVERT     │   │ OUVERT     │
│ Trafic: 45│    │ Trafic: 120│   │ Trafic: 5  │
│ Risque: 🟢│    │ Risque: 🟢 │   │ Risque: 🟠 │
└───────────┘    └────────────┘   └────────────┘
```

**Codes couleur:**
- 🟢 **Vert** = Port sûr
- 🟡 **Orange** = Surveillance recommandée
- 🔴 **Rouge** = Risque critique

**Ports importants:**
- 80: HTTP (Web)
- 443: HTTPS (Web sécurisé)
- 22: SSH (Accès distant)
- 3306: MySQL
- 5432: PostgreSQL

---

### Zone 3: Analyse IA Temps Réel

```
┌─────────────────────────────────┐
│ Analyse IA Temps Réel           │
│                                 │
│  Niveau de Menace               │
│  ◆ 35.2                         │
│  Dernière analyse: 10:45:23     │
│                                 │
│  Bots       │ 8                 │
│  Brute      │ 5                 │
│  SQL Inj.   │ 2                 │
│  XSS        │ 1                 │
└─────────────────────────────────┘
```

**Métriques IA:**
- **Bots détectés**: Crawlers, scanners
- **Brute force**: Tentatives connexion
- **SQL Injection**: Attaques BD
- **XSS**: Attaques cross-site

---

### Zone 4: Graphiques Temps Réel

#### Requêtes par Minute (Line Chart)
```
Requêtes
120 │     ╱╲      ╱╲
100 │    ╱  ╲    ╱  ╲
 80 │───╱────╲──╱────╲──
 60 │  ╱      ╲╱      ╲
 40 │ ╱                ╲
 20 │╱                  ╲
  0 └───────────────────
    00:00 02:00 04:00 ...
```

#### Types d'Incidents (Doughnut Chart)
```
SQL Injection (45%)  ████████
Brute Force (25%)    █████
Bots (20%)           ████
XSS (10%)            ██
```

---

### Zone 5: Console Temps Réel

```
💻 Console Temps Réel
┌─────────────────────────────────────┐
│ [INFO] Système initialisé            │
│ [DEBUG] BD connectée                 │
│ [INFO] IA chargée                   │
│ [WARNING] CPU élevé (87%)           │
│ [ERROR] Connexion SSH suspecte      │
│ [CRITICAL] Tentative brute force!   │
└─────────────────────────────────────┘
```

**Codes couleur:**
- 🔵 DEBUG = Info de débogage
- 🔵 INFO = Information
- 🟡 WARNING = Avertissement
- 🔴 ERROR = Erreur
- 🟣 CRITICAL = Critique

---

## 💬 Assistant IA Chat

### Ouvrir le Chat
1. Cliquer le bouton `💬` en bas à droite
2. Le chat s'ouvre avec animation
3. Taper votre commande

### Interface du Chat
```
┌───────────────────────────────────┐
│ 🤖 Assistant IA Cybersécurité  ✕  │
├───────────────────────────────────┤
│                                   │
│ IA: Bonjour! Je peux vous aider:  │
│ • Analyse de sécurité              │
│ • Scan des ports                   │
│ • Détection de menaces             │
│                                   │
│ Vous: Scan ports                  │
│                                   │
│ IA: 📊 PORT_SCAN                  │
│ Scan ports: 45 ports en écoute... │
│                                   │
├───────────────────────────────────┤
│ Écrivez votre demande...      [📤] │
└───────────────────────────────────┘
```

---

## 🤖 Commandes IA

### Format des Commandes

```
COMMANDE              │ SYNTAXE ACCEPTÉE
──────────────────────┼──────────────────────────
Analyse sécurité      │ "Analyse", "Check", "Scanning"
Scan ports            │ "Scan ports", "Ports ouverts"
Vérifier firewall     │ "Firewall", "Pare-feu"
Trafic réseau         │ "Trafic", "Réseau", "Network"
État serveur          │ "Serveur", "Status", "Health"
Détecter menaces      │ "Menace", "Threat", "Anomalies"
Vulnérabilités        │ "Vuln", "Failles", "Vulnérabilités"
Analyser logs         │ "Logs", "Journal", "Events"
Recommandations       │ "Conseil", "Suggestions"
État système          │ "Système", "CPU", "RAM"
```

### Exemples de Commandes

#### 1️⃣ Analyse Sécurité Complète
```
Vous: "Analyse sécurité"

IA: 📊 ANALYSIS
Analyse complète: Score menace 35.2, Niveau: Faible
- Système sain
- 45 connexions actives
- 1 anomalie détectée
Confiance: 94%
```

#### 2️⃣ Scan des Ports
```
Vous: "Scan ports"

IA: 🔍 PORT_SCAN
Scan ports: 45 ports en écoute, Risque: Moyen
- Port 80: Ouvert (HTTP)
- Port 443: Ouvert (HTTPS)
- Port 22: Ouvert (SSH - Surveillance recommandée)
- Port 3306: Ouvert (MySQL - Risque!)
Confiance: 89%
```

#### 3️⃣ Détection de Menaces
```
Vous: "Détecte menaces"

IA: 🎯 THREAT_DETECTION
Menaces détectées: 3 anomalies, Score: 35.2
- CPU usage: 87% (ANOMALIE)
- Tentative brute force: 12 (ANOMALIE)
- Port 3389 ouvert: RDP (ANOMALIE)
Confiance: 92%
```

#### 4️⃣ Recommandations
```
Vous: "Recommandations"

IA: 💡 RECOMMENDATIONS
5 recommandations disponibles:
1. [CRITIQUE] Fermer port MySQL 3306
2. [HAUTE] Activer SSH key-only auth
3. [MOYEN] Mettre à jour OpenSSL
4. [BAS] Configurer WAF
5. [BAS] Activer logging détaillé
```

#### 5️⃣ État du Système
```
Vous: "État serveur"

IA: ⚙️ SERVER_STATUS
Serveur: CPU 34.5%, Mémoire 67.2%
- Uptime: 12 j 5 h 30 m
- Charge: 1.2 (4 cores)
- Disque: 45% utilisé
- Connexions TCP: 47 établies
```

---

## 🛡️ Modules de Sécurité

### 1. 🔍 Surveillance Ports Réseau

**Fonctionnalités:**
- Scan temps réel des ports
- Classification par risque
- Trafic par port
- Recommandations automatiques

**Zones de risque:**
```
🟢 VERT (Sûr):        80, 443, 8000-8999
🟡 ORANGE (Attent.):  22 (SSH), 3389 (RDP)
🔴 ROUGE (Critique):  3306 (MySQL), 5432 (PostgreSQL), 27017 (MongoDB)
```

**Actions:**
- Cliquer un port pour détails
- Recevoir recommandations IA
- Créer alerte si anormal

### 2. 🤖 Analyse IA Temps Réel

**Détecte:**
- Comportements anormaux
- Pics d'activité
- Patterns suspects
- Anomalies système

**Score:** 0-100
- 0-20: Sûr ✅
- 20-40: Faible ⚠️
- 40-60: Moyen ⚠️⚠️
- 60-80: Élevé 🔴
- 80+: Critique 🔴🔴

### 3. 🎣 Honeypot (Pièges Virtuels)

**Fonctionnement:**
- Faux services attractifs
- Enregistrement des tentatives
- Classification des attaquants
- Blocage automatique

**Événements détectés:**
- Scans port
- Brute force attempts
- Exploits connus
- Reconnaissance

### 4. 💻 Console Temps Réel

**Types d'événements:**
```
[DEBUG]   Infos de débogage (bleu)
[INFO]    Informations (bleu clair)
[WARNING] Avertissements (jaune)
[ERROR]   Erreurs (rouge)
[CRITICAL] Critique (rouge foncé)
```

**Filtrage:**
- Tous les logs
- Par niveau de sévérité
- Par service
- Dernières N entrées

### 5. 🚨 Tableau des Failles

**Colonnes:**
| Faille | Type | Niveau | Emplacement | Confiance | État | Action |
|--------|------|--------|-------------|-----------|------|--------|
| XSS    | App  | ÉLEVÉ  | /admin      | 92%       | ⚠️   | Fixer  |

**Sévérité:**
- 🔴 CRITIQUE = Fixer IMMÉDIATEMENT
- 🔴 ÉLEVÉ = Fixer sous 24h
- 🟡 MOYEN = Fixer sous 7 jours
- 🟢 BAS = À considérer

### 6. 💡 Recommandations IA

**Format:**
```
┌─ CRITIQUE ─────────────────────┐
│ Fermer port MySQL 3306         │
│ Risk: SQL injection            │
│ Confiance: 95%                 │
└────────────────────────────────┘
```

**Agir sur recommandation:**
1. Lire la description
2. Consulter la confiance IA
3. Cliquer "Implémenter"
4. Confirmer l'action

---

## 🔐 Permissions et Rôles

### Rôles SOC

#### 🔴 Super Admin (Niveau 100)
```
Permissions:
✅ Voir tous les dashboards
✅ Gérer tous les modules
✅ Éditer configuration IA
✅ Générer rapports
✅ Activer/Désactiver sécurité
✅ Attribuer rôles
```

#### 🟠 Security Admin (Niveau 80)
```
Permissions:
✅ Voir tous les dashboards
✅ Gérer sécurité
✅ Éditer alertes
✅ Générer rapports
❌ Éditer IA
❌ Activer/Désactiver
```

#### 🟡 SOC Analyst (Niveau 60)
```
Permissions:
✅ Voir dashboards
✅ Gérer alertes
✅ Voir rapports
❌ Générer rapports
❌ Éditer configuration
```

#### 🟢 Read Only (Niveau 20)
```
Permissions:
✅ Voir dashboard
❌ Modifier alertes
❌ Générer rapports
❌ Accéder APIs
```

### Attribution de Rôles

```
Admin Panel > Security > Assign SOC Role
┌───────────────────────────────┐
│ Utilisateur: [John Admin]     │
│ Rôle: [Security Admin ▼]      │
│ Permissions accordées:        │
│ ✓ view_all                    │
│ ✓ manage_security             │
│ ✓ edit_alerts                 │
│ ✓ generate_reports            │
│                               │
│     [Annuler]  [Sauvegarder] │
└───────────────────────────────┘
```

---

## 📋 Bonnes Pratiques

### ✅ À Faire

```
1. Consulter le dashboard quotidiennement
   └─ Vérifier les alertes critiques

2. Utiliser le chat IA pour analyses
   └─ Plus rapide que navigation manuelle

3. Suivre les recommandations IA
   └─ Scores de confiance élevés

4. Configurer surveillance continue
   └─ Scans automatiques actifs

5. Exporter rapports régulièrement
   └─ Archivage et audit

6. Mettre à jour firewall/ACLs
   └─ Basé sur détections

7. Former l'équipe
   └─ Connaissance du système
```

### ❌ À Éviter

```
1. Ignorer alertes critiques
   └─ Risque de sécurité

2. Désactiver monitoring
   └─ Visibilité réduite

3. Utiliser rôles admin par défaut
   └─ Danger de sécurité

4. Ignorer recommandations IA
   └─ Opportunités manquées

5. Ne pas mettre à jour
   └─ Vulnérabilités croissantes

6. Partager accès facilement
   └─ Risque d'accès non autorisé

7. Négliger les logs
   └─ Traces perdues
```

---

## 🔧 Dépannage

### Le chat IA ne répond pas

**Solution:**
```
1. Vérifier vous êtes connecté (is_staff)
2. Vérifier internet
3. Actualiser la page (F5)
4. Vérifier console (F12 > Console)
5. Relancer le serveur Django
```

### Le dashboard se charge lentement

**Solution:**
```
1. Réduire la fréquence de refresh (Settings)
2. Fermer autres onglets
3. Vider cache du navigateur
4. Vérifier CPU/RAM du serveur
5. Optimiser requêtes BD
```

### Les alertes ne s'affichent pas

**Solution:**
```
1. Vérifier config monitoring active
2. Vérifier les permissions
3. Vérifier les filtres
4. Relancer le scan manuel
5. Consulter les logs serveur
```

---

## 📞 Support et Ressources

### Ressources Internes
- Documentation technique: `CYBERSECURITY_UPDATE_2.0.md`
- Guide sécurité: `SECURITY_GUIDE.md`
- API Documentation: `/api/docs/`

### Commandes Utiles

```bash
# Vérifier statut sécurité
curl http://localhost:8000/api/security-dashboard/

# Test chat IA
curl -X POST http://localhost:8000/api/ai/chat/ \
  -d '{"message":"Analyse sécurité"}' \
  -H "Content-Type: application/json"

# Port scan
curl http://localhost:8000/api/ai/port-scan/

# Threat detection
curl http://localhost:8000/api/ai/threat-detection/
```

---

**Guide mis à jour le:** 2026-05-15  
**Version:** 2.0  
**Auteur:** Équipe Sécurité  

✅ **Vous êtes maintenant prêt à utiliser le SOC avec IA!**
