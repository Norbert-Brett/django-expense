from django.db import models

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('utilities', 'Utilities'),
        ('rent', 'Rent'),
        ('transportation', 'Transportation'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name