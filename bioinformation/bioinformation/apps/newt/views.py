# coding:utf-8
import hashlib
import os
import sys
import time
from Bio import SeqIO
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render_to_response
from bioinformation.apps.newt.models import tb_Protein, tb_GeneSq, tb_user, tb_Gannotations, \
    tb_Greferences, tb_Gsource, tb_Ggene, tb_Gmrna, tb_G5utr, tb_Gcds, tb_G3utr, \
    tb_Gregulutory, tb_Pannotations, tb_Preferences, tb_Psource, tb_aprotein, \
    tb_region, tb_cds, tb_count
from django.http import HttpResponse
from bioinformation.util import DateUtils
from bioinformation import settings
# from test.test_multiprocessing import _file_like
# from test.test_codecs import RecodingTest
# Create your views here.
def index(req):
    return render_to_response("newt/main.html", {});
def top(req):
    addr = req.META['REMOTE_ADDR'];
    req.session["IP"] = addr;
    try:
        count = tb_count.objects.get(ip=addr);
    except:
        count = None;
    if count is None:
        ipcount = tb_count();
        ipcount.ip = addr;
        ipcount.time = DateUtils.getDate();
        ipcount.save();
    cp = list(tb_count.objects.all());
    req.session["count"] = len(cp);
    return render_to_response("newt/index.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def bottom(req):
    hour = time.localtime().tm_hour
    if hour % 2 == 0:
        music = "I Am You.mp3"
    if hour % 2 != 0 :
        music = "Stan.mp3"
    return render_to_response("newt/music.html", {"music":music});
def login_view(req):
    return render_to_response("newt/services.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def register_view(req):
     return render_to_response("newt/contact.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def about(req):
     return render_to_response("newt/about.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def download_view(req):
    m = list(tb_Protein.objects.all());
    k = list(tb_GeneSq.objects.all());
    num = 1;
    k.extend(m);
    if len(k) == 0:
        return render_to_response("newt/noResult.html", {"all":"all", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
    if req.REQUEST.get("page") is  not  None:
        num = req.REQUEST.get("page");
    database = req.REQUEST.get("database");
    if database is None:
        database = "all";
    wh = req.REQUEST.get("where");
    keywords = req.REQUEST.get("keywords");
    if keywords is None:
        keywords = "";
    if database == "all":
        m = list(tb_Protein.objects.filter(Q(description__icontains=keywords)));
        k = list(tb_GeneSq.objects.filter(Q(description__icontains=keywords)));
        k.extend(m);
        if len(k) == 0:
             return render_to_response("newt/noResult.html", {"all":"all", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        for k1 in k:
            k1.user_id = len(k1.origin);
        p = Paginator(k, 10);
        if wh is not None and wh == "up":
            if int(num) > 1:
                m = int(num);
                num = m - 1;
            else:
                num = 1;
        if wh is not None and wh == "down":
            if int(num) < p.num_pages:
                num = int(num) + 1;
            else:
                num = p.num_pages;
        pg = p.page(num);
        return render_to_response("newt/download.html", {"list_gene": pg.object_list, "currentPage":pg.number, "pageCount":p.num_pages, "count":p.count, "perPage":p.per_page, "list_num":p.page_range, "current_num":num, "all":"all", "database":"all", "ind":pg.start_index(), "keywords":keywords, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
    if database == "gene":
        k = list(tb_GeneSq.objects.filter(Q(description__icontains=keywords)));
        if len(k) == 0:
             return render_to_response("newt/noResult.html", {"gene":"gene", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        for k1 in k:
            k1.user_id = len(k1.origin);
        p = Paginator(k, 10);
        if wh is not None and wh == "up":
            if int(num) > 1:
                m = int(num);
                num = m - 1;
            else:
                num = 1;
        if wh is not None and wh == "down":
            if int(num) < p.num_pages:
                num = int(num) + 1;
            else:
                num = p.num_pages;
        pg = p.page(num);
        m = pg.object_list;
        return render_to_response("newt/download.html", {"list_gene": pg.object_list, "currentPage":pg.number, "pageCount":p.num_pages, "count":p.count, "perPage":p.per_page, "list_num":p.page_range, "current_num":num, "gene":"gene", "database":"gene", "ind":pg.start_index(), "keywords":keywords, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
    if database == "protein":
        k = list(tb_Protein.objects.filter(Q(description__icontains=keywords)));
        if len(k) == 0:
             return render_to_response("newt/noResult.html", {"protein":"protein", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        for k1 in k:
            k1.user_id = len(k1.origin);
        p = Paginator(k, 10);
        if wh is not None and wh == "up":
            if int(num) > 1:
                m = int(num);
                num = m - 1;
            else:
                num = 1;
        if wh is not None and wh == "down":
            if int(num) < p.num_pages:
                num = int(num) + 1;
            else:
                num = p.num_pages;
        pg = p.page(num);
        return render_to_response("newt/download.html", {"list_gene": pg.object_list, "currentPage":pg.number, "pageCount":p.num_pages, "count":p.count, "perPage":p.per_page, "list_num":p.page_range, "current_num":num, "protein":"protein", "database":"protein", "ind":pg.start_index(), "keywords":keywords, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def upload_view(req):
    m = req.session.get("username");
    if m == None:
        return render_to_response("newt/index.html", {"ERROR":"YES", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
    else:
            return render_to_response("newt/uploadview.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def register(req):
    reload(sys)
    sys.defaultencoding = 'utf-8'
    if req.method == "POST":
        user = tb_user();
        user.name = req.REQUEST['name'].rstrip();
        user.email = req.REQUEST['email'].rstrip();
        user.password = hashlib.sha1(req.REQUEST['password'].rstrip()).hexdigest();
        if user.name == "" or user.email == "" or req.REQUEST['password'] == "" or req.REQUEST['password1'] == "":
            return render_to_response("contact.html", {"REGISTERERROR":"YES", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        user.save();
    return render_to_response("newt/index.html", {"REGISTERSUCCESS":"YES", "ContextPath":(req.META['HTTP_HOST'] + "/newt/"), "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def login(req):
    reload(sys)
    sys.defaultencoding = 'utf-8'
    if req.method == "POST":
        username = req.REQUEST['name'].rstrip();
        passwd = hashlib.sha1(req.REQUEST['password'].rstrip()).hexdigest();
        try:
            usr = tb_user.objects.get(name=username, password=passwd);
        except:
            return render_to_response("newt/services.html", {"LOGINERROR":"YES", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        if usr.name != None:
            req.session['userid'] = usr.id;
            req.session['username'] = username;
            return render_to_response("newt/index.html", {"LOGINSUCCESS":"YES", "ContextPath":(req.META['HTTP_HOST'] + "/newt/"), "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        else:
                return render_to_response("newt/index.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def exit(req):
    try:
        del req.session['username'];
        del req.session["userid"]
    except:
            return render_to_response("newt/index.html", {"EXIT":"NO", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
    return render_to_response("newt/index.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def upload(req):
    if req.method == "POST":
        resourcetype = req.REQUEST['resourcetype'];
        filetype = req.REQUEST['filetype'];
        upload_file = req.FILES.get("filename");
        if resourcetype == "" or filetype == "" or upload_file is None:
            return render_to_response("newt/uploadview.html", {"UPLOADERROR":"YES", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        elif resourcetype == "dna":
                try:
                    record = SeqIO.read(upload_file, "genbank");
                except:
                    return render_to_response("newt/uploadview.html", {'FORMATERROR':'YES', "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
                m = record.annotations.get('gi');
                try:
                    result = tb_GeneSq.objects.get(gi=m);
                except:
                    result = None;
                if result is not None:
                    return  render_to_response("newt/uploadview.html", {'MESSAGEERROR':'YES', "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
                path = os.path.dirname(__file__)
                ms = file(path + settings.MEDIA_ROOT + "datafile/" + record.annotations.get('gi') + ".gb", "wb");
                for chunk in upload_file.chunks():
                    ms.write(chunk)
                ms.close();
                gen = tb_GeneSq();
                gen.sequence_id = record.id;
                gen.name = record.name;
                gen.description = record.description;
                gen.origin = record.seq;
                gen.gi = record.annotations.get('gi')
                gen.time = record.annotations.get("date");
                gen.user_id = req.session['userid']
                gen.save();
                gannotations = tb_Gannotations();
                gannotations.sequence_version = record.annotations.get('sequence_version');
                gannotations.source = record.annotations.get('source')
                for  a in  record.annotations.get('taxonomy'):
                    gannotations.taxonomy += a;
                for b in  record.annotations.get('keywords'):
                    gannotations.keywords += b;
                gannotations.accessions = record.annotations.get('accessions')[0];
                gannotations.data_file_division = record.annotations.get('data_file_division')
                gannotations.organism = record.annotations.get('organism')
                gannotations.sequence_id = record.id;
                gannotations.save();
                for m in record.annotations.get("references"):
                    references = tb_Greferences();
                    references.authors = m.authors
                    references.title = m.title;
                    references.journal = m.journal;
                    references.pubmed = m.pubmed_id
                    references.annotations_id = gannotations
                    references.save();
                if len(record.features) >= 1:
                        source = tb_Gsource();
                        source.organism = record.features[0].qualifiers.get('organism')
                        source.mod_type = record.features[0].qualifiers.get('mol_type')
                        source.db_xref = record.features[0].qualifiers.get('db_xref')
                        source.sex = record.features[0].qualifiers.get('sex')
                        source.tissue_type = record.features[0].qualifiers.get('tissue_type')
                        source.dev_stage = record.features[0].qualifiers.get('dev_stage')
                        source.start = record.features[0].location.start.position
                        source.end = record.features[0].location.end.position
                        source.sequence_id = record.id
                        source.save();
                if len(record.features) >= 2:
                    Ggene = tb_Ggene();
                    Ggene.gene = record.features[1].qualifiers.get('gene')
                    Ggene.start = record.features[1].location.start.position
                    Ggene.end = record.features[1].location.end.position
                    Ggene.sequence_id = record.id
                    Ggene.save();
                if len(record.features) >= 3:
                    mrna = tb_Gmrna();
                    mrna.gene = record.features[2].qualifiers.get('gene')
                    mrna.start = record.features[2].location.start.position
                    mrna.end = record.features[2].location.end.position
                    mrna.product = record.features[2].qualifiers.get('product')
                    mrna.sequence_id = record.id
                    mrna.save();
                if len(record.features) >= 4:
                    utr5 = tb_G5utr();
                    utr5.gene = record.features[3].qualifiers.get('gene')
                    utr5.start = record.features[3].location.start.position
                    utr5.end = record.features[3].location.end.position
                    utr5.sequence_id = record.id;
                    utr5.save();
                if len(record.features) >= 5:
                    cds = tb_Gcds();
                    cds.gene = record.features[4].qualifiers.get('gene')
                    cds.product = record.features[4].qualifiers.get('product')
                    cds.protein_id = record.features[4].qualifiers.get('protein_id')
                    cds.codon_start = record.features[4].qualifiers.get('codon_start')
                    cds.translation = record.features[4].qualifiers.get('translation')
                    cds.start = record.features[4].location.start.position
                    cds.end = record.features[4].location.end.position
                    cds.sequence_id = record.id
                    cds.save();
                if len(record.features) >= 6:
                    utr3 = tb_G3utr();
                    utr3.gene = record.features[5].qualifiers.get('gene')
                    utr3.start = record.features[5].location.start.position
                    utr3.end = record.features[5].location.end.position
                    utr3.sequence_id = record.id
                    utr3.save();
                if len(record.features) >= 7:
                    regulutory = tb_Gregulutory();
                    regulutory.gene = record.features[6].qualifiers.get('gene')
                    regulutory.start = record.features[6].location.start.position
                    regulutory.end = record.features[6].location.end.position
                    regulutory.regulutory_class = record.features[6].qualifiers.get('regulatory_class')
                    regulutory.sequence_id = record.id;
                    regulutory.save();
                return render_to_response("newt/uploadview.html", {"UPLOADSUCCESS":"YES", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        elif resourcetype == "protein":
               try:
                record = SeqIO.read(upload_file, "genbank");
               except:
                 return render_to_response("newt/uploadview.html", {'FORMATERROR':'YES', "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
               m = record.annotations.get('gi');
               try:
                    result = tb_Protein.objects.get(gi=m);
               except:
                    result = None;
               if result is not None:
                 return render_to_response("newt/uploadview.html", {'MESSAGEERROR':'YES', "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
               path = os.path.dirname(__file__);
               ms = file(path + settings.MEDIA_ROOT + "datafile/" + record.annotations.get('gi') + ".gp", "wb");
               for chunk in upload_file.chunks():
                    ms.write(chunk)
               ms.close();
               protein = tb_Protein();
               protein.sequence_id = record.id;
               protein.name = record.name;
               protein.description = record.description;
               protein.origin = record.seq;
               protein.gi = record.annotations.get('gi')
               protein.time = record.annotations.get("date");
               protein.user_id = req.session['userid'];
               protein.save();
               pannotations = tb_Pannotations();
               pannotations.sequence_version = record.annotations.get('sequence_version')
               pannotations.source = record.annotations.get('source')
               for  a in  record.annotations.get('taxonomy'):
                   pannotations.taxonomy += a;
               for b in  record.annotations.get('keywords'):
                    pannotations.keywords += b;
               pannotations.accessions = record.annotations.get('accessions')[0];
               pannotations.data_file_division = record.annotations.get('data_file_division')
               pannotations.organism = record.annotations.get('organism')
               pannotations.sequence_id = record.id;
               pannotations.db_source = record.annotations.get('db_source')
               pannotations.comment = record.annotations.get('comment')
               pannotations.save();

               for m in record.annotations.get("references"):
                   preferences = tb_Preferences();
                   preferences.authors = m.authors
                   preferences.title = m.title;
                   preferences.journal = m.journal;
                   preferences.pubmed = m.pubmed_id
                   preferences.annotations_id = pannotations
                   preferences.save();
               if len(record.features) >= 1:
                   psource = tb_Psource();
                   psource.start = record.features[0].location.start.position
                   psource.end = record.features[0].location.end.position
                   psource.note = record.features[0].qualifiers.get('note')
                   psource.collection_date = record.features[0].qualifiers.get('collection_date')
                   psource.country = record.features[0].qualifiers.get('country')
                   psource.isolation_source = record.features[0].qualifiers.get('isolation_source')
                   psource.db_xref = record.features[0].qualifiers.get('db_xref')
                   psource.host = record.features[0].qualifiers.get('host')
                   psource.organism = record.features[0].qualifiers.get('organism')
                   psource.sequence_id = record.id;
                   psource.save();
               if len(record.features) >= 2:
                   aprotein = tb_aprotein();
                   aprotein.start = record.features[1].location.start.position
                   aprotein.end = record.features[1].location.end.position
                   aprotein.product = record.features[1].qualifiers.get('product')
                   aprotein. sequence_id = record.id
                   aprotein.save();
               if len(record.features) >= 3:
                   region = tb_region();
                   region.note = record.features[2].qualifiers.get('note')
                   region.start = record.features[2].location.start.position
                   region.end = record.features[2].location.end.position
                   region.db_xref = record.features[2].qualifiers('db_xref')
                   region.region_name = record.features[2].qualifiers.get('region_name')
                   region.sequence_id = record.id
                   region.save();
               if len(record.features) >= 4:
                   cds = tb_cds();
                   cds.gene = record.features[3].qualifiers.get('gene')
                   cds.coded_by = record.features[3].qualifiers.get('coded_by')
                   cds.start = record.features[3].location.start.position
                   cds.end = record.features[3].location.start.position
                   cds.sequence_id = record.id
                   cds.save();
               return render_to_response("newt/uploadview.html", {"UPLOADSUCCESS":"YES", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def search(req):
    if req.method == "POST":
        database = req.REQUEST['database'];
        value = req.REQUEST['value'];
        if database == "all":
            gen = list(tb_GeneSq.objects.filter(Q(description__icontains=value)));
            protein = list(tb_Protein.objects.filter(Q(description__icontains=value)));
            gen.extend(protein);
            if len(gen) == 0:
                return render_to_response("newt/noResult.html", {"all":"all", "keywords":value, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
            for k1 in gen:
                k1.user_id = len(k1.origin);
            p = Paginator(gen, 10);
            pg = p.page(1);
            return render_to_response("newt/download.html", {"list_gene": pg.object_list, "currentPage":pg.number, "pageCount":p.num_pages, "count":p.count, "perPage":p.per_page, "list_num":p.page_range, "current_num":1, "all":"all", "database":"all", "ind":pg.start_index(), "keywords":value, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        elif database == "gene":
            gen = list(tb_GeneSq.objects.filter(Q(description__icontains=value)));
            if len(gen) == 0:
                return render_to_response("newt/noResult.html", {"gene":"gene", "keywords":value, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
            for k1 in gen:
                k1.user_id = len(k1.origin);
            p = Paginator(gen, 10);
            pg = p.page(1);
            return render_to_response("newt/download.html", {"list_gene": pg.object_list, "currentPage":pg.number, "pageCount":p.num_pages, "count":p.count, "perPage":p.per_page, "list_num":p.page_range, "current_num":1, "gene":"gene", "database":"gene", "ind":pg.start_index(), "keywords":value, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        elif database == "protein":
             protein = list(tb_Protein.objects.filter(Q(description__icontains=value)));
             if len(protein) == 0:
                 return render_to_response("newt/noResult.html", {"protein":"protein", "keywords":value, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
             for k1 in protein:
                k1.user_id = len(k1.origin);
             p = Paginator(protein, 10);
             pg = p.page(1);
             return render_to_response("newt/download.html", {"list_gene": pg.object_list, "currentPage":pg.number, "pageCount":p.num_pages, "count":p.count, "perPage":p.per_page, "list_num":p.page_range, "current_num":1, "protein":"protein", "database":"protein", "ind":pg.start_index(), "keywords":value, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def download_GenBank(req):
    if req.method == "GET":
        name = req.REQUEST['name'];
        format = req.REQUEST['format'];
        try:
            if format == "gene":
                fl = open(settings.MEDIA_ROOT + "datafile/" + name + ".gb");
            if format == "protein":
                fl = open(settings.MEDIA_ROOT + "datafile/" + name + ".gp");
        except:
            if format == "gene":
                return render_to_response("newt/error.html", {"gene":"gene", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")})
            if format == "protein":
                return render_to_response("newt/error.html", {"protein":"protein", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")})
        data = fl.read();
        if format == "gene":
            filename = "sequence.gb";
        if format == "protein":
            filename = "sequence.gp";
        fl.close();
        response = HttpResponse(data, content_type='application/octet-stream') ;
        response['Content-Disposition'] = 'attachment; filename=%s' % filename;
        return response;
def download_FASTA(req):
    if req.method == "GET":
        name = req.REQUEST['name'];
        format = req.REQUEST['format'];
        if format == "gene":
            try:
                SeqIO.convert(settings.MEDIA_ROOT + "datafile/" + name + ".gb", "genbank", settings.MEDIA_ROOT + "fasta/sequence.fna", "fasta")
            except:
                return render_to_response("newt/error.html", {"gene":"gene", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        if format == "protein":
            try:
                SeqIO.convert(settings.MEDIA_ROOT + "datafile/" + name + ".gp", "genbank", settings.MEDIA_ROOT + "fasta/sequence.fna", "fasta")
            except:
                return render_to_response("newt/error.html", {"protein":"protein", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        try:
            fl = open(settings.MEDIA_ROOT + "fasta/sequence.fna");
        except:
            return render_to_response("newt/error.html", {"username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        data = fl.read();
        filename = "sequence.fna";
        fl.close();
        response = HttpResponse(data, content_type='application/octet-stream') ;
        response['Content-Disposition'] = 'attachment; filename=%s' % filename;
        return response;
def fasta_view(req):
    if req.method == "GET":
        name = req.REQUEST['name'];
        format = req.REQUEST['format'];
        if format == "gene":
            gene = tb_GeneSq.objects.get(gi=name);
            leg = len(gene.origin)
            return render_to_response("newt/fasta.html", {"sequence":gene, "gene":"gene", "length":leg, "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        if format == "protein":
            protein = tb_Protein.objects.get(gi=name);
            leg = len(protein.origin)
            return render_to_response("newt/fasta.html", {"sequence":protein, "length":leg, "protein":"protein", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
def genbank_view(req):
    if req.method == "GET":
        name = req.REQUEST['name'];
        fmat = req.REQUEST['format'];
        protein_id = "";
        protein_gi = "";
        if fmat == "gene":
            gen = tb_GeneSq.objects.get(gi=name);
            try:
                sequence = SeqIO.read(settings.MEDIA_ROOT + "datafile/" + name + ".gb", "genbank");
                an = sequence.annotations;
                features = sequence.features;
            except:
                return render_to_response("newt/noResult.html", {"gene":"gene", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")})
            if len(sequence.features) > 4:
                if  sequence.features[4].qualifiers.has_key("protein_id"):
                    if len(sequence.features[4].qualifiers.get('protein_id')) >= 1:
                        protein_id = sequence.features[4].qualifiers.get('protein_id')[0];
                        protein_gi = tb_Protein.objects.get(sequence_id=protein_id).gi;
                        return render_to_response("newt/genbank.html", {"sequence":gen, "sequence_annotations":an, "sequence_features":features, "format":fmat, "protein_id":protein_gi, "gene":"gene", "length":len(sequence.seq), "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
            return render_to_response("newt/genbank.html", {"sequence":gen, "sequence_annotations":an, "sequence_features":features, "format":fmat, "gene":"gene", "length":len(sequence.seq), "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
        if fmat == "protein":
            protein = tb_Protein.objects.get(gi=name)
            try:
                sequence = SeqIO.read(settings.MEDIA_ROOT + "datafile/" + name + ".gp", "genbank");
                an = sequence.annotations;
                features = sequence.features;
            except:
                return render_to_response("newt/noResult.html", {"protein":"protein", "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")})
            return render_to_response("newt/Pgenbank.html", {"sequence":protein, "sequence_annotations":an, "sequence_features":features, "format":fmat, "protein":"protein", "length":len(sequence.seq), "username":req.session.get("username"), "addr":req.session.get("IP"), "ipcount":req.session.get("count")});
