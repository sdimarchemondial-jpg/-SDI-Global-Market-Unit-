# 🎯 GUIDE D'UTILISATION - SYSTÈME DE RETRAIT

## 📌 Accès à l'Application

### Adresse
```
http://localhost:8000
```

### Comptes de Test

#### 👤 Utilisateur (Vendeur)
- **Username**: `vendeur`
- **Mot de passe**: `password123`
- **Rôle**: buyer_seller
- **Solde initial**: 85 USD (après tests)

#### 🛡️ Admin Principal
- **Username**: `admin`
- **Mot de passe**: `password123`
- **Rôle**: super_admin
- **Fonction**: Approuver/rejeter tous les retraits

#### 🛡️ Admin Secondaire
- **Username**: `sdi.admin`
- **Rôle**: admin_secondary
- **Fonction**: Approuver/rejeter les retraits (avec permission)

---

## 💰 Processus de Retrait

### ÉTAPE 1: Créer un Retrait (Utilisateur)

1. Se connecter avec `vendeur` / `password123`
2. Aller au profil utilisateur
3. Cliquer sur "Retirer des Fonds"
4. Remplir le formulaire:
   - **Montant**: Ex: 10.00
   - **Devise**: USD, HTG, DOP, EUR
   - **Compte**: principal ou multidevice
   - **Code PIN**: `46236880` (pour vendeur)
   - **Code Sécurisé**: `2053` (pour vendeur)
5. Cliquer "Confirmer le Retrait"

**Résultat**:
- ✅ Montant débité IMMÉDIATEMENT du compte
- 📧 Message: "En attente de confirmation de l'administration"

### ÉTAPE 2: Approuver le Retrait (Admin)

1. Se connecter avec `admin` / `password123`
2. Aller au profil
3. Section "Retraits en attente" affiche les retraits à traiter
4. Clique sur "Approuver" pour le retrait
5. Optionnel: Ajouter des notes

**Résultat**:
- ✅ Retrait marqué comme "Approuvé"
- 📧 Email d'approbation envoyé à l'utilisateur avec lien de reçu
- 📄 Reçu généré et accessible

### ÉTAPE 3: Rejeter le Retrait (Optionnel)

1. Au lieu d'approuver, cliquer sur "Rejeter"
2. Sélectionner la raison:
   - Données bancaires invalides
   - Compte suspendu
   - Montant dépassant la limite
   - Autre

**Résultat**:
- ✅ Montant remboursé au compte de l'utilisateur
- 📧 Email de rejet envoyé avec la raison
- 🔄 L'utilisateur peut réessayer

---

## 📋 Affichage dans le Profil

### Pour l'Utilisateur
```
📊 Mes Retraits

Retraits Approuvés:
- 10.00 USD - Approuvé le 08/05/2026 04:37
  [Voir Reçu] [Télécharger PDF]

Historique des Retraits:
- 15.00 USD - Rejeté le 08/05/2026 04:38 (Données bancaires invalides)
- 5.00 USD - Approuvé le 08/05/2026 04:44
```

### Pour l'Admin
```
👥 Retraits en Attente de Confirmation

| Utilisateur | Montant | Devise | Date | Actions |
|-------------|---------|--------|------|---------|
| vendeur | 25.00 | USD | 08/05 04:45 | [Approuver] [Rejeter] |
| fabien | 50.00 | HTG | 08/05 04:46 | [Approuver] [Rejeter] |
```

---

## 📧 Emails Reçus

### Email 1: Approbation
```
Sujet: Confirmation de retrait #1
Corps:
  Votre retrait de 10.00 USD a été approuvé.
  ID de retrait: 1
  Date de confirmation: 08/05/2026 04:37
  
  Voir et télécharger le reçu: [Lien]
```

### Email 2: Rejet
```
Sujet: Retrait rejeté #2
Corps:
  Votre retrait de 15.00 USD a été rejeté.
  ID de retrait: 2
  Raison: Données bancaires invalides
  Montant remboursé: 15.00 USD
  
  Vous pouvez réessayer avec des données valides.
```

---

## 🔐 Gestion des Permissions Admin Secondaire

### Attribuer des Permissions (Super Admin)

1. Aller à: `http://localhost:8000/admin/`
2. Connexion avec admin
3. Aller à "AdminWithdrawalPermission"
4. Ajouter une nouvelle permission:
   - **Admin**: sdi.admin
   - **Peut confirmer les retraits**: ✓
   - **Accordé par**: admin

### Résultat
- Admin secondaire peut maintenant approuver/rejeter les retraits
- Les actions sont auditées (qui, quand)

---

## 📊 Voir les Reçus

### Format Web
```
http://localhost:8000/withdrawal-receipt/1/
```

Affiche:
- Numéro du retrait
- Montant et devise
- Compte utilisé
- Date de confirmation
- Admin qui a confirmé
- Bouton d'impression

### Télécharger en PDF
- Cliquer sur "Télécharger le reçu"
- PDF généré automatiquement
- Contient tous les détails

---

## 🧪 Tester le Système

### Scripts de Test Disponibles

```bash
# Test 1: Création de retrait
python sdi_market/test_withdrawal_direct.py

# Test 2: Approbation et email
python sdi_market/test_withdrawal_approval.py

# Test 3: Rejet et remboursement
python sdi_market/test_withdrawal_rejection.py

# Test 4: Permissions admin
python sdi_market/test_admin_permissions.py

# Test 5: Affichage des retraits
python sdi_market/test_withdrawal_profile_view.py

# Test 6: Workflow complet
python sdi_market/test_complete_workflow.py
```

### Résultats Attendus
✅ Tous les tests doivent passer
✅ Soldes cohérents
✅ Emails envoyés
✅ Permissions respectées

---

## 🐛 Troubleshooting

### Problème: "Invalid HTTP_HOST header"
**Solution**: Le serveur de test ajoute 'testserver' à ALLOWED_HOSTS automatiquement

### Problème: "Codes PIN/Secure incorrects"
**Solution**: Pour vendeur, utiliser:
- PIN: `46236880`
- Secure Code: `2053`

### Problème: Emails non reçus
**En développement**: Les emails s'affichent dans la console (console backend)
**En production**: Configurer les variables d'environnement EMAIL_HOST_USER et EMAIL_HOST_PASSWORD

### Problème: Retraits n'apparaissent pas dans le profil
**Solution**: S'assurer que l'utilisateur est connecté. Actualiser la page (F5).

---

## 📞 Support

Pour plus d'informations:
- Consulter `IMPLEMENTATION_COMPLETE.md` pour les détails techniques
- Consulter `TEST_RESULTS_SUMMARY.md` pour les résultats des tests

---

## ✅ Checklist de Validation

- [ ] Je peux créer un retrait
- [ ] Le montant est débité immédiatement
- [ ] Admin voit le retrait en attente
- [ ] Admin peut approuver
- [ ] Email d'approbation reçu
- [ ] Reçu accessible
- [ ] Admin peut rejeter
- [ ] Montant remboursé après rejet
- [ ] Email de rejet reçu
- [ ] Permissions admin secondaire fonctionnent

**Tous les points validés?** ✅ Le système est opérationnel!