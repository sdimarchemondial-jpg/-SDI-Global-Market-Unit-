from pathlib import Path

path = Path(r'c:\wamp64\www\SDI STORE 1\sdi_market\marketplace\views.py')
text = path.read_text()
start = text.index('# ==========================================\r\n# CONTRÔLE SYSTÈME - Gestion des mots de passe\r\n# ==========================================\r\n')
end = text.index('# ------------------------------\r\n# NOTIFICATIONS PERSISTANTES AVEC SONNERIE\r\n# ------------------------------', start)
path.write_text(text[:start] + text[end:])
print('Duplicate system_control_panel removed')
