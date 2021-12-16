from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE

class MyCollaboratorManager(BaseUserManager):
	def create_user(self, email, nom, prenom,matricule,date_fin_fonction,service,fonction, date_debut_fonction,is_developper,is_responsable,password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not nom:
			raise ValueError('Users must have a first name')
		if not prenom:
			raise ValueError('Users must have a last name')

		user = self.model(
			email=self.normalize_email(email),
			nom=nom,
            prenom=prenom,
			password=password,
		) 
		user.matricule = matricule
		user.service = service
		user.fonction = fonction
		user.date_debut_fonction = date_debut_fonction
		user.date_fin_fonction = date_fin_fonction
		user.is_responsable = is_responsable
		user.is_developper = is_developper
		user.save(using=self._db)
		return user

	def create_superuser(self, email, nom,prenom,password=None):
		user = self.model(
			email=self.normalize_email(email),
            nom=nom,
			prenom=prenom,
			password=password,
        )
		user.id_admin =True
		user.is_staff =True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Collaborateur(AbstractBaseUser):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	email=models.EmailField(verbose_name="email", max_length=60, unique=True)
	matricule=models.TextField(null=True,blank=True)
	service=models.TextField(null=True,blank=True)
	fonction=models.TextField(null=True,blank=True)
	responsable=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	date_debut_fonction=models.DateField(null=True,blank=True)
	date_fin_fonction=models.DateField(null=True,blank=True)
	date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login=models.DateTimeField(verbose_name='last login', auto_now=True)
	is_responsable = models.BooleanField(default=False)
	is_developper = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nom','prenom']

	objects = MyCollaboratorManager()

	def __str__(self):
		return self.email
	
	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True



class Absence(models.Model):
	date_debut=models.DateTimeField(null=False, blank=False)
	date_fin=models.DateTimeField(null=False, blank=False)
	codification=models.CharField(max_length=255, null=False, blank=False)
	nature= models.CharField(max_length=20,null=False,blank=False)
	est_valide=models.BooleanField(default=False)
	nbr_jours=models.IntegerField(null=False,blank=False)
	cause=models.TextField(null=True,blank=True)
	developpeur=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)

class Mail(models.Model):
    objet=models.CharField(max_length=255,null=False,blank=False)
    body=models.TextField(null=False,blank=False)
	absence=models.ForeignKey(Mail,on_delete=CASCADE,null=False,blank=False)
    collaborateur=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)