#!/usr/bin/env python
import os

models_code = '''

# ========================
# Configuration commissions dépôt MicrosDiCash
# ========================
class DepositCommissionConfig(models.Model):
    """Configuration des commissions pour les dépôts MicrosDiCash"""
    TYPE_CHOICES = (
        ('pourcentage', 'Pourcentage (%)'),
        ('fixe', 'Montant fixe'),
    )
    
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('HTG', 'HTG'), ('DOP', 'DOP'), ('EUR', 'EUR')], unique=True)
    commission_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='pourcentage')
    commission_value = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Valeur de commission (% ou montant fixe)")
    
    min_deposit = models.DecimalField(max_digits=15, decimal_places=2, default=0, help_text="Dépôt minimum")
    max_deposit = models.DecimalField(max_digits=15, decimal_places=2, default=999999, help_text="Dépôt maximum")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Configuration Commission Dépôt'
        verbose_name_plural = 'Configurations Commissions Dépôt'
        ordering = ['currency']
    
    def __str__(self):
        return f"{self.currency} - {self.commission_value} ({self.get_commission_type_display()})"
    
    def calculate_commission(self, amount):
        """Calcule la commission selon le type et la valeur"""
        from decimal import Decimal
        if not self.is_active:
            return Decimal('0')
        
        amount = Decimal(str(amount))
        
        if self.commission_type == 'pourcentage':
            return (amount * Decimal(str(self.commission_value)) / Decimal('100')).quantize(Decimal('0.01'))
        else:  # fixe
            return Decimal(str(self.commission_value))


# ========================
# Dépôts MicrosDiCash
# ========================
class Deposit(models.Model):
    """Transactions de dépôt via agents MicrosDiCash"""
    STATUS_CHOICES = (
        ('pending', 'En attente de confirmation'),
        ('confirmed', 'Confirmé'),
        ('rejected', 'Rejeté'),
        ('completed', 'Complété'),
    )
    
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deposits_made', limit_choices_to={'is_agent': True})
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deposits_received')
    
    amount = models.DecimalField(max_digits=15, decimal_places=2, help_text="Montant du dépôt")
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('HTG', 'HTG'), ('DOP', 'DOP'), ('EUR', 'EUR')])
    
    commission = models.DecimalField(max_digits=15, decimal_places=2, default=0, help_text="Commission de l'agent")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    reference = models.CharField(max_length=50, unique=True, blank=True, help_text="Référence unique du dépôt")
    
    confirmed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deposits_confirmed')
    confirmed_at = models.DateTimeField(null=True, blank=True)
    
    rejection_reason = models.TextField(blank=True, help_text="Raison du rejet si applicable")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Dépôt MicrosDiCash'
        verbose_name_plural = 'Dépôts MicrosDiCash'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Dépôt {self.amount} {self.currency} - {self.client.username} par {self.agent.username if self.agent else 'N/A'}"
    
    def save(self, *args, **kwargs):
        import uuid
        if not self.reference:
            self.reference = f"MDC{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
'''

with open('marketplace/models.py', 'a') as f:
    f.write(models_code)

print("✓ Models appended successfully")
