# **IPv6 Dynamic DNS Updater Script (EN/FR)**

## **English**

### Overview

This Python script automatically updates DNS records when your server's IPv6 address changes. It works with IONOS to update AAAA records for self-hosted domains, ensuring they always point to the correct IP, even with dynamic addresses and CGNAT.

### Features

- **Automatic IPv6 DNS updates** via IONOS API
- **Logs updates**
- **No third-party service needed**

### Requirements

- Python 3
- `requests` library (`pip install requests`)

### Setup

1. **API Key**: Store your IONOS API key in `IONOS_API_KEY.txt`.
2. **Domains**: Add your domains to the `URLs` list in the script.
3. **IPv6 Address File**: Ensure `ipv6.txt` exists for the script to compare IPs.
4. **Cron Job (optional)**: Run the script periodically to check for changes.

### Usage

1. Clone or download the script.
2. Configure your API key and domains.
3. Run the script manually or set it up in a cron job.

---

## **Français**

### Présentation

Ce script Python met à jour automatiquement les enregistrements DNS lorsque l'adresse IPv6 de votre serveur change. Il fonctionne avec IONOS pour mettre à jour les enregistrements AAAA, garantissant que vos domaines pointent toujours vers la bonne IP, même avec des adresses dynamiques et CGNAT.

### Fonctionnalités

- **Mise à jour automatique des DNS IPv6** via l'API IONOS
- **Journalisation des mises à jour**
- **Aucun service tiers nécessaire**

### Prérequis

- Python 3
- Bibliothèque `requests` (`pip install requests`)

### Configuration

1. **Clé API** : Placez votre clé API IONOS dans `IONOS_API_KEY.txt`.
2. **Domaines** : Ajoutez vos domaines à la liste `URLs` dans le script.
3. **Fichier IPv6** : Assurez-vous que `ipv6.txt` existe pour comparer les IP.
4. **Cron Job (optionnel)** : Exécutez le script périodiquement pour détecter les changements.

### Utilisation

1. Clonez ou téléchargez le script.
2. Configurez votre clé API et vos domaines.
3. Exécutez le script manuellement ou avec un cron job.
