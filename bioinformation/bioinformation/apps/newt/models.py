# coding:utf-8
from django.db import models

# Create your models here.
class tb_user(models.Model):
    name=models.CharField(max_length=50,blank=True);
    email=models.CharField(max_length=50,blank=True);
    password=models.CharField(max_length=50,blank=True);
    def _unicode_(self):
        return self.name;
class tb_GeneSq(models.Model):
    sequence_id=models.CharField(max_length=100,blank=True);
    name=models.CharField(max_length=200,blank=True);
    description=models.TextField(blank=True);
    time=models.CharField(max_length=200,blank=True);
    origin=models.TextField(blank=True);
    user_id=models.IntegerField(max_length=11,blank=True);
    gi=models.CharField(max_length=100,blank=True);
    format=models.CharField(max_length=100,blank=True,default="gene");
    def _unicode_(self):
        return self.name;
class tb_Gannotations(models.Model):
    sequence_version=models.CharField(max_length=200,blank=True);
    source=models.CharField(max_length=200,blank=True);
    taxonomy=models.CharField(max_length=200,blank=True);
    keywords=models.CharField(max_length=200,blank=True);
    accessions=models.CharField(max_length=200,blank=True);
    data_file_division=models.CharField(max_length=200,blank=True);
    organism=models.CharField(max_length=200,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
        return self.source;
class tb_Greferences(models.Model):
    authors=models.CharField(max_length=200,blank=True);
    title=models.CharField(max_length=200,blank=True);
    journal=models.CharField(max_length=200,blank=True);
    pubmed=models.CharField(max_length=200,blank=True);
    annotations_id=models.ForeignKey(tb_Gannotations);
    def _unicode_(self):
        return self.title;
class tb_Gsource(models.Model):
    organism=models.CharField(max_length=200,blank=True);
    mod_type=models.CharField(max_length=200,blank=True);
    db_xref=models.CharField(max_length=200,blank=True);
    sex=models.CharField(max_length=200,blank=True);
    tissue_type=models.CharField(max_length=200,blank=True);
    dev_stage=models.CharField(max_length=200,blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.organism;
class tb_Ggene(models.Model):
    gene=models.CharField(max_length=200,blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.gene;
class tb_Gmrna(models.Model):
    gene=models.CharField(max_length=200,blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    product=models.CharField(max_length=200,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.gene;
class tb_G5utr(models.Model):
    gene=models.CharField(max_length=200,blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.gene;
class tb_Gcds(models.Model):
    gene=models.CharField(max_length=200,blank=True);
    product=models.CharField(max_length=200,blank=True);
    protein_id=models.CharField(max_length=200,blank=True);
    codon_start=models.CharField(max_length=200,blank=True);
    translation=models.TextField(blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.gene;
class tb_G3utr(models.Model):
    gene=models.CharField(max_length=200,blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.gene;
class tb_Gregulutory(models.Model):
    gene=models.CharField(max_length=200,blank=True);
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    regulutory_class=models.CharField(max_length=200,blank=True);
    sequence_id=sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.gene;
class tb_Protein(models.Model):
    sequence_id=models.CharField(max_length=100,blank=True);
    name=models.CharField(max_length=200,blank=True);
    description=models.TextField(blank=True);
    time=models.CharField(max_length=200,blank=True);
    origin=models.TextField(blank=True);
    gi=models.CharField(max_length=100,blank=True);
    user_id=models.IntegerField(max_length=11,blank=True);
    format=models.CharField(max_length=100,blank=True,default="protein");
    def _unicode_(self):
        return self.name;
class tb_Pannotations(models.Model):
    sequence_version=models.CharField(max_length=200,blank=True);
    source=models.CharField(max_length=200,blank=True);
    taxonomy=models.CharField(max_length=200,blank=True);
    keywords=models.CharField(max_length=200,blank=True);
    accessions=models.CharField(max_length=200,blank=True);
    data_file_division=models.CharField(max_length=200,blank=True);
    organism=models.CharField(max_length=200,blank=True);
    db_source=models.CharField(max_length=200,blank=True);
    comment=models.TextField(blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
        return self.source;
class tb_Preferences(models.Model):
    authors=models.CharField(max_length=200,blank=True);
    title=models.CharField(max_length=200,blank=True);
    journal=models.CharField(max_length=200,blank=True);
    pubmed=models.CharField(max_length=200,blank=True);
    annotations_id=models.ForeignKey(tb_Pannotations);
    def _unicode_(self):
        return self.title;
class tb_Psource(models.Model):
    start=models.IntegerField(max_length=11,blank=True);
    end= models.IntegerField(max_length=11,blank=True);
    note=models.CharField(max_length=200,blank=True);
    collection_date=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    isolation_source=models.CharField(max_length=200,blank=True)
    db_xref=models.CharField(max_length=200,blank=True)
    host=models.CharField(max_length=200,blank=True)
    organism=models.CharField(max_length=200,blank=True)
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
        return self.note;
class tb_aprotein(models.Model):
    start=models.IntegerField(max_length=11,blank=True);
    end= models.IntegerField(max_length=11,blank=True);
    product=models.CharField(max_length=200,blank=True)
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
            return self.product;
class tb_region(models.Model):
    note=models.CharField(max_length=200,blank=True)
    start=models.IntegerField(max_length=11,blank=True);
    end= models.IntegerField(max_length=11,blank=True);
    db_xref=models.CharField(max_length=200,blank=True)
    region_name=models.CharField(max_length=200,blank=True)
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
        return self.region_name;
class tb_cds(models.Model):
    gene=models.CharField(max_length=200,blank=True)
    coded_by=models.CharField(max_length=200,blank=True)
    start=models.IntegerField(max_length=11,blank=True);
    end=models.IntegerField(max_length=11,blank=True);
    sequence_id=models.CharField(max_length=100,blank=True);
    def _unicode_(self):
        return self.gene;
class tb_count(models.Model):
    ip=models.CharField(max_length=50,blank=True)
    time=models.DateField(blank=True)
    def _unicode_(self):
        return self.ip;