from django.contrib import admin

from .models import Proposition
from .models import Theme
from .models import Lieu
from .models import Profile
from .models import Soutien
from .models import Proximite
from .models import Autre_utilisateur
from .models import Organisation
from .models import Evenement
from .models import Proximite
from .models import Petition

class SoutienAdmin(admin.ModelAdmin):
	list_display	= ('user', 'lien', 'propositions', 'evenement', 'organisation', 'petition')
	list_filter		= ('user', 'lien', 'propositions', 'evenement', 'organisation', 'petition')
	ordering		= ('user', 'lien', 'propositions', 'evenement', 'organisation', 'petition')
	search_fields	= ('user', 'lien', 'propositions', 'evenement', 'organisation', 'petition')

class PetitionAdmin(admin.ModelAdmin):
	list_display	= ('titre', 'date_creation', 'date_echeance', 'objectif_de_signataires')



admin.site.register(Proposition)
admin.site.register(Theme)
admin.site.register(Lieu)
admin.site.register(Profile)
admin.site.register(Soutien, SoutienAdmin)
admin.site.register(Autre_utilisateur)
admin.site.register(Proximite)
admin.site.register(Organisation)
admin.site.register(Evenement)
admin.site.register(Petition, PetitionAdmin)