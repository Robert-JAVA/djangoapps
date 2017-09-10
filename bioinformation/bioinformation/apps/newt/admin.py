# coding:utf-8
from django.contrib import admin
from bioinformation.apps.newt.models import tb_user, tb_GeneSq, tb_Gannotations, tb_Greferences, \
    tb_Gsource, tb_Gmrna, tb_G3utr, tb_G5utr, tb_Gcds, tb_Ggene, tb_Gregulutory, \
    tb_Protein, tb_Pannotations, tb_Preferences, tb_Psource, tb_aprotein, tb_region, \
    tb_cds,tb_count
    
# Register your models here.
admin.site.register(tb_user);
admin.site.register(tb_GeneSq);
admin.site.register(tb_Gannotations);
admin.site.register(tb_Greferences);
admin.site.register(tb_Gsource);
admin.site.register(tb_Gmrna);
admin.site.register(tb_G3utr);
admin.site.register(tb_G5utr);
admin.site.register(tb_Gcds);
admin.site.register(tb_Ggene);
admin.site.register(tb_Gregulutory);
admin.site.register(tb_Protein)
admin.site.register(tb_Pannotations);
admin.site.register(tb_Preferences);
admin.site.register(tb_Psource);
admin.site.register(tb_aprotein);
admin.site.register(tb_region);
admin.site.register(tb_cds);
admin.site.register(tb_count);