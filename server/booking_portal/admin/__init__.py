from django.contrib import admin

from .slot import SlotAdmin
from .instrument import InstrumentAdmin
from .user import (
        StudentAdmin,
        FacultyAdmin,
        CustomUserAdmin,
)
from ..models import (
                CustomUser, Student, Faculty,
                EmailModel, LabAssistant, Instrument,
                Request, Slot, UserDetail, Announcement
)
from .email import EmailAdmin
from .request import RequestAdmin
from ..models.instrument.form_models import *


admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(EmailModel, EmailAdmin)
admin.site.register(LabAssistant, CustomUserAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserDetail)
admin.site.register(FTIR)
admin.site.register(FESEM)
admin.site.register(LCMS)
admin.site.register(TCSPC)
admin.site.register(Rheometer)
admin.site.register(AAS)
admin.site.register(TGA)
admin.site.register(BET)
admin.site.register(CDSpectrophotometer)
admin.site.register(LSCM)
admin.site.register(DSC)
admin.site.register(GC)
admin.site.register(EDXRF)
admin.site.register(HPLC)
admin.site.register(NMR)
admin.site.register(PXRD)
admin.site.register(SCXRD)
admin.site.register(XPS)
admin.site.register(UVSpectrophotometer)
admin.site.register(Announcement)
