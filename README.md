# 🌍 SDI Marché Mondial - E-Commerce & Chat Global

**Plateforme e-commerce complète combinant un marketplace, un système de wallet multi-devises, un chat global, et un système de livraison automatisé.**

## 🎓 Formation en ligne
Ce projet est également conçu comme support de formation pour apprendre Django et le développement e-commerce.
Consultez `FORMATION.md` et `docs/formation/` pour un parcours pas à pas, des modules et des exercices pratiques.

## 🚀 Démarrage rapide

### Installation

1. **Cloner le projet et accéder au dossier principal :**
   ```bash
   cd sdi_market
   ```

2. **Créer un environnement virtuel (facultatif mais recommandé) :**
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations Django :**
   ```bash
   python manage.py migrate
   ```

5. **Créer un superuser (pour accès admin) :**
   ```bash
   python manage.py createsuperuser
   ```

6. **Démarrer le serveur développement :**
   ```bash
   python manage.py runserver
   ```

Le site sera accessible à : **http://127.0.0.1:8000**

---

## 📚 Modules supplémentaires pour la formation

- **Administration & Déploiement** : [docs/admin_deploy.md](docs/admin_deploy.md)
- **Données de démonstration** : `scripts/create_demo_seed.py` — script pour créer comptes et produits de démo
- **Exercices "Petit projet"** : [docs/petit_projet.md](docs/petit_projet.md)

Pour charger rapidement des données de démonstration :

```bash
python scripts/create_demo_seed.py
```


## 📋 Fonctionnalités principales

### 🛒 Marketplace
- Catalogue complet de produits
- Système d'acheteurs et vendeurs
- Panier d'achat et commandes
- Recherche et filtrage avancés
- Système d'évaluation et d'avis

### 💬 Chat Ensemble
- **Chat global** "Marché Mondial SDI" accessible à tous les utilisateurs inscrits
- Partage de produits directement dans la conversation
- Envoi de texte et d'images
- Publicité intelligente automatique
- Notifications en temps réel

### 💰 Wallet Multi-Devises
- Support : USD, HTG, PESO
- Transactions sécurisées
- Commissions et paiements

### 🚚 Système de Livraison
- Assignation automatique des livreurs
- GPS en temps réel
- Suivi de commande
- Zone de livraison

### 📊 Recommandations
- Produits personnalisés par utilisateur
- Produits tendances
- Suggestions similaires

---

## 🏗️ Architecture

```
sdi_market/
├── marketplace/           # Application Django principale
│   ├── models.py         # Modèles (User, Product, Order, Chat, etc.)
│   ├── views.py          # Vues et logique métier
│   ├── urls.py           # Routage
│   ├── templates/        # Templates HTML
│   ├── migrations/       # Migrations base de données
│   └── admin.py          # Interface admin Django
├── sdi_market/           # Configuration Django
│   ├── settings.py       # Paramètres
│   ├── urls.py           # URLs principales
│   └── wsgi.py          # WSGI
├── manage.py            # Utilitaire Django
└── requirements.txt     # Dépendances Python
```

---

## 🔑 Variables d'environnement importantes

À configurer dans `sdi_market/settings.py` :

- `SECRET_KEY` - Clé secrète Django (à changer en production)
- `DEBUG` - Mode debug (actuellement True)
- `ALLOWED_HOSTS` - Hôtes autorisés
- `UNSPLASH_ACCESS_KEY` - API pour générer les images produits

---

## 📚 Documentation supplémentaire

- [Configuration des images produits](sdi_market/IMAGE_GENERATION_README.md)
- [Fonctionnalités détaillées](FONCTIONNALITES.md)
- [Système de livraison](IMPLEMENTATION_SUMMARY.md)
- [Importance du système de livraison](DELIVERY_SYSTEM_IMPORTANCE.md)

---

## 🛠️ Stack technique

- **Backend** : Django 6.0.3
- **API REST** : Django REST Framework 3.15.1
- **Auth** : JWT (djangorestframework-simplejwt)
- **Base de données** : SQLite (configurable pour MySQL/PostgreSQL)
- **Images** : Pillow 10.2.0
- **ML** : scikit-learn, pandas, numpy
- **APIs** : Unsplash (images), Haversine (distance GPS)

---

## 🔄 Commandes utiles

```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un compte admin
python manage.py createsuperuser

# Charger les données de test
python manage.py management commands create_test_data

# Lancer le serveur
python manage.py runserver

# Accès admin
http://127.0.0.1:8000/admin/
```

---

## 📞 Support et debug

### Erreur : "table introuvable : marketplace_chatgroup"
- Solution : `python manage.py migrate`

### Erreur : Page non trouvée
- Vérifier que le serveur est en cours d'exécution
- Vérifier l'URL exacte

### Base de données manquante
- Supprimer `db.sqlite3` et relancer les migrations

---

## 🌐 Accès au site

- **Accueil** : http://127.0.0.1:8000/
- **Chat Ensemble** : http://127.0.0.1:8000/chat/
- **Dashboard** : http://127.0.0.1:8000/dashboard/
- **Admin** : http://127.0.0.1:8000/admin/

---

## ✨ À venir et améliorations

- [ ] Chat privé entre utilisateurs
- [ ] Canaux de chat par catégorie/zone
- [ ] Animations UI riche pour les publicités
- [ ] Système de promotion payante pour vendeurs
- [ ] Mobile app (Flutter/React Native)
- [ ] Déploiement production (Heroku/AWS)

---

## 📄 Licence

Propriétaire - SDI Marché Mondial 2026

---

**Dernière mise à jour** : 9 Avril 2026
