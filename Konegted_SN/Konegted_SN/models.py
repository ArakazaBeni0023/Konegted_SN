from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)

     def __str__(self):
        return f"{self.nom} - {self.prenom}"

class Formateur(models.Model):
    id = models.BigAutoField(primary_key=True)
    # nom = models.CharField(max_length=64)
    # prenom = models.CharField(max_length=64)
    
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="Formateur")
    
    telephone = models.CharField(max_length=20)
    lieu = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    qualification = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = "Formateur"

class Parent(models.Model):
    id = models.BigAutoField(primary_key=True)
    # nom = models.CharField(max_length=64)
    # prenom = models.CharField(max_length=64)

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="Parent")
    
    telephone = models.CharField(max_length=20)
    lieu = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Parent"

class Matier(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom =models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = "Matier"
        
class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="Formateur")
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="Parent")
    matier = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = "Reservation"
    