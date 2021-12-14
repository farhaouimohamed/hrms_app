from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, date_rej_iga, nom, prenom, password=None,is_developper=False,is_responsable=False):
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
		user.date_rej_iga = date_rej_iga
		user.is_responsable = is_responsable
		user.is_developper = is_developper
		user.save(using=self._db)
		return user

	def create_superuser(self, email, nom,prenom, password=None):
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

class Account(AbstractBaseUser):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	email=models.EmailField(verbose_name="email", max_length=60, unique=True)
	date_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login=models.DateTimeField(verbose_name='last login', auto_now=True)
	date_rej_iga=models.DateField(null=True, blank=True)
	is_responsable = models.BooleanField(default=False)
	is_developper = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	id_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nom','prenom']

	objects = MyAccountManager()

	def __str__(self):
		return self.email
	
	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
