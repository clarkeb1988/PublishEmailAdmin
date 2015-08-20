from django.db import models


class XsltData(models.Model):
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='DATE_CREATED')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='LAST_UPDATED')  # Field name made lowercase.
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.
    date_merged = models.DateTimeField(db_column='DATE_MERGED', blank=True, null=True)  # Field name made lowercase.
    merge_results = models.CharField(db_column='MERGE_RESULTS', max_length=150, blank=True)  # Field name made lowercase.
    template_id = models.IntegerField(db_column='TEMPLATE_ID', blank=True, null=True)  # Field name made lowercase.
    temp_key = models.CharField(db_column='TEMP_KEY', max_length=15, blank=True)  # Field name made lowercase.
    file = models.TextField(db_column='FILE', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.file_name

    class Meta:
        managed = False
        db_table = 'XSLT_DATA'


class XsltDataSource(models.Model):
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='DATE_CREATED')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='LAST_UPDATED')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80)  # Field name made lowercase.
    template = models.ForeignKey('XsltTemplate', db_column='TEMPLATE_ID', blank=True, null=True)  # Field name made lowercase.
    static_flg = models.CharField(db_column='STATIC_FLG', max_length=1)  # Field name made lowercase.
    data = models.ForeignKey(XsltData, db_column='DATA_ID', blank=True, null=True)  # Field name made lowercase.
    date_refreshed = models.DateTimeField(db_column='DATE_REFRESHED', blank=True, null=True)  # Field name made lowercase.
    source_type = models.CharField(db_column='SOURCE_TYPE', max_length=15)  # Field name made lowercase.
    source_sub_type = models.CharField(db_column='SOURCE_SUB_TYPE', max_length=240, blank=True)  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'XSLT_DATA_SOURCE'


class XsltDataSourceAttr(models.Model):
    data_source = models.ForeignKey(XsltDataSource, db_column='DATA_SOURCE_ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80)  # Field name made lowercase.
    value = models.TextField(db_column='VALUE')  # Field name made lowercase.
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.

    def __str__(self):
        return self.row_id

    class Meta:
        managed = False
        db_table = 'XSLT_DATA_SOURCE_ATTR'


class XsltDataSourceMap(models.Model):
    data_source = models.ForeignKey(XsltDataSource, db_column='DATA_SOURCE_ID')  # Field name made lowercase.
    template = models.ForeignKey('XsltTemplate', db_column='TEMPLATE_ID')  # Field name made lowercase.
    ds_field_name = models.CharField(db_column='DS_FIELD_NAME', max_length=80)  # Field name made lowercase.
    tm_field_name = models.CharField(db_column='TM_FIELD_NAME', max_length=80)  # Field name made lowercase.
    ds_field_type = models.CharField(db_column='DS_FIELD_TYPE', max_length=10)  # Field name made lowercase.
    tm_field_type = models.CharField(db_column='TM_FIELD_TYPE', max_length=10)  # Field name made lowercase.
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.

    def __str__(self):
        return self.row_id

    class Meta:
        managed = False
        db_table = 'XSLT_DATA_SOURCE_MAP'


class XsltMessage(models.Model):
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80)  # Field name made lowercase.
    desc_text = models.CharField(db_column='DESC_TEXT', max_length=240, blank=True)  # Field name made lowercase.
    template = models.ForeignKey('XsltTemplate', db_column='TEMPLATE_ID', blank=True, null=True)  # Field name made lowercase.
    data_source = models.ForeignKey(XsltDataSource, db_column='DATA_SOURCE_ID')  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1)  # Field name made lowercase.
    log_batch = models.CharField(db_column='LOG_BATCH', max_length=1)  # Field name made lowercase.
    log_emails = models.CharField(db_column='LOG_EMAILS', max_length=1)  # Field name made lowercase.
    lit_id = models.CharField(db_column='LIT_ID', max_length=15, blank=True)  # Field name made lowercase.
    subject = models.CharField(db_column='SUBJECT', max_length=240)  # Field name made lowercase.
    from_name = models.CharField(db_column='FROM_NAME', max_length=80)  # Field name made lowercase.
    reply_to = models.CharField(db_column='REPLY_TO', max_length=80)  # Field name made lowercase.
    receipt = models.CharField(db_column='RECEIPT', max_length=1)  # Field name made lowercase.
    link_secure = models.CharField(db_column='LINK_SECURE', max_length=1)  # Field name made lowercase.
    link_tracking = models.CharField(db_column='LINK_TRACKING', max_length=1)  # Field name made lowercase.
    unsub_msg = models.CharField(db_column='UNSUB_MSG', max_length=1)  # Field name made lowercase.
    attach_doc_id = models.IntegerField(db_column='ATTACH_DOC_ID', blank=True, null=True)  # Field name made lowercase.
    twitter_msg = models.CharField(db_column='TWITTER_MSG', max_length=1)  # Field name made lowercase.
    facebook_msg = models.CharField(db_column='FACEBOOK_MSG', max_length=1)  # Field name made lowercase.
    linkedin_msg = models.CharField(db_column='LINKEDIN_MSG', max_length=1)  # Field name made lowercase.
    verify_deliverability = models.CharField(db_column='VERIFY_DELIVERABILITY', max_length=1)  # Field name made lowercase.
    format = models.CharField(db_column='FORMAT', max_length=4)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    recurring_rules = models.CharField(db_column='RECURRING_RULES', max_length=240, blank=True)  # Field name made lowercase.
    execute_next = models.DateTimeField(db_column='EXECUTE_NEXT', blank=True, null=True)  # Field name made lowercase.
    last_executed = models.DateTimeField(db_column='LAST_EXECUTED', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'XSLT_MESSAGE'


class XsltQueue(models.Model):
    xsl_source = models.CharField(db_column='XSL_SOURCE', max_length=250, blank=True)  # Field name made lowercase.
    xsl_source_type = models.CharField(db_column='XSL_SOURCE_TYPE', max_length=15, blank=True)  # Field name made lowercase.
    xml_source = models.TextField(db_column='XML_SOURCE', blank=True)  # Field name made lowercase.
    xml_source_type = models.CharField(db_column='XML_SOURCE_TYPE', max_length=15, blank=True)  # Field name made lowercase.
    output_path = models.CharField(db_column='OUTPUT_PATH', max_length=50, blank=True)  # Field name made lowercase.
    output_dest = models.CharField(db_column='OUTPUT_DEST', max_length=15, blank=True)  # Field name made lowercase.
    debug_flg = models.CharField(db_column='DEBUG_FLG', max_length=1, blank=True)  # Field name made lowercase.
    ftp_site_url = models.CharField(db_column='FTP_SITE_URL', max_length=50, blank=True)  # Field name made lowercase.
    ftp_site_folder = models.CharField(db_column='FTP_SITE_FOLDER', max_length=50, blank=True)  # Field name made lowercase.
    ftp_user = models.CharField(db_column='FTP_USER', max_length=50, blank=True)  # Field name made lowercase.
    ftp_pass = models.CharField(db_column='FTP_PASS', max_length=50, blank=True)  # Field name made lowercase.
    cm_report_id = models.CharField(db_column='CM_REPORT_ID', max_length=15, blank=True)  # Field name made lowercase.
    cache_key = models.CharField(db_column='CACHE_KEY', max_length=15, blank=True)  # Field name made lowercase.
    delete_input = models.CharField(db_column='DELETE_INPUT', max_length=1, blank=True)  # Field name made lowercase.
    delete_output = models.CharField(db_column='DELETE_OUTPUT', max_length=1, blank=True)  # Field name made lowercase.
    lang_cd = models.CharField(db_column='LANG_CD', max_length=5, blank=True)  # Field name made lowercase.
    source_id = models.CharField(db_column='SOURCE_ID', max_length=15, blank=True)  # Field name made lowercase.
    source_type = models.CharField(db_column='SOURCE_TYPE', max_length=15, blank=True)  # Field name made lowercase.
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.

    def __str__(self):
        return self.row_id

    class Meta:
        managed = False
        db_table = 'XSLT_QUEUE'


class XsltTemplate(models.Model):
    file_name = models.CharField(db_column='FILE_NAME', max_length=250, blank=True)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=50, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='DATE_CREATED')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='LAST_UPDATED')  # Field name made lowercase.
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.
    destination = models.CharField(db_column='DESTINATION', max_length=15, blank=True)  # Field name made lowercase.
    audience = models.CharField(db_column='AUDIENCE', max_length=15, blank=True)  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1, blank=True)  # Field name made lowercase.
    test_data_id = models.IntegerField(db_column='TEST_DATA_ID', blank=True, null=True)  # Field name made lowercase.
    file = models.TextField(db_column='FILE', blank=True)  # Field name made lowercase.
    lang_cd = models.CharField(db_column='LANG_CD', max_length=3, blank=True)  # Field name made lowercase.
    par_row = models.ForeignKey('self', db_column='PAR_ROW_ID', blank=True, null=True)  # Field name made lowercase.
    src_type = models.CharField(db_column='SRC_TYPE', max_length=15, blank=True)  # Field name made lowercase.
    src_id = models.CharField(db_column='SRC_ID', max_length=15, blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.file_name

    class Meta:
        managed = False
        db_table = 'XSLT_TEMPLATE'


class XsltTemplateUsage(models.Model):
    row_id = models.AutoField(primary_key=True, db_column='ROW_ID')  # Field name made lowercase.
    template = models.ForeignKey(XsltTemplate, db_column='TEMPLATE_ID')  # Field name made lowercase.
    system = models.CharField(db_column='SYSTEM', max_length=100, blank=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=100, blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.row_id

    class Meta:
        managed = False
        db_table = 'XSLT_TEMPLATE_USAGE'

class TrackingLinks(models.Model):
    row_id = models.CharField(db_column='ROW_ID', max_length=15)  # Field name made lowercase.
    key = models.AutoField(primary_key=True, db_column='KEY')  # Field name made lowercase.
    link = models.CharField(db_column='LINK', max_length=240)  # Field name made lowercase.
    counter = models.IntegerField(db_column='COUNTER')  # Field name made lowercase.
    last_clicked = models.DateTimeField(db_column='LAST_CLICKED', blank=True, null=True)  # Field name made lowercase.
    bitly_link = models.CharField(db_column='BITLY_LINK', max_length=40, blank=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=80, blank=True)  # Field name made lowercase.
    type_cd = models.CharField(db_column='TYPE_CD', max_length=20, blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.link

    class Meta:
        managed = False
        db_table = 'TRACKING_LINKS'