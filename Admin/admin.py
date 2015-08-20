from django.contrib import admin
from Admin.models import XsltData, XsltDataSource, XsltDataSourceAttr, XsltDataSourceMap, \
    XsltMessage, XsltQueue, XsltTemplate, XsltTemplateUsage, TrackingLinks


class XsltDataAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'file_name', 'date_merged', 'merge_results', 'template_id', 'temp_key')

class XsltDataSourceAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'name', 'template', 'static_flg', 'data', 'date_refreshed', 'source_type', \
                    'source_sub_type', 'active')

class XsltDataSourceAttrAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'data_source', 'name', 'value')

class XsltDataSourceMapAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'data_source', 'template', 'ds_field_name', 'tm_field_name', 'ds_field_type', \
                    'tm_field_type')

class XsltMessageAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'name', 'template', 'data_source', 'active', 'log_batch', 'lit_id', \
                    'subject', 'from_name', 'reply_to', 'receipt', 'link_secure', 'link_tracking', 'unsub_msg', \
                    'attach_doc_id', 'twitter_msg', 'facebook_msg', 'linkedin_msg', 'verify_deliverability', 'format', \
                    'linkedin_msg')

class XsltQueueAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'xsl_source', 'xsl_source_type', 'xml_source', 'xml_source_type', 'output_path', \
                    'output_dest', 'debug_flg', 'ftp_site_url', 'ftp_site_folder', 'ftp_user', 'ftp_pass', \
                    'cm_report_id', 'cache_key', 'delete_input', 'delete_output', 'lang_cd', 'source_id', \
                    'source_type')

class XsltTemplateAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'par_row', 'file_name', 'category', 'destination', 'audience', 'lang_cd', \
                    'test_data_id', 'src_type', 'src_id', 'active')
    list_editable = ('file_name',)
    list_per_page = (20)

class XsltTemplateUsageAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'template', 'system', 'type')

class TrackingLinksAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'key', 'link', 'counter', 'last_clicked', 'bitly_link', 'description', 'type_cd')


admin.site.register(XsltData, XsltDataAdmin)
admin.site.register(XsltDataSource, XsltDataSourceAdmin)
admin.site.register(XsltDataSourceAttr, XsltDataSourceAttrAdmin)
admin.site.register(XsltDataSourceMap, XsltDataSourceMapAdmin)
admin.site.register(XsltMessage, XsltMessageAdmin)
admin.site.register(XsltQueue, XsltQueueAdmin)
admin.site.register(XsltTemplate, XsltTemplateAdmin)
admin.site.register(XsltTemplateUsage, XsltTemplateUsageAdmin)
admin.site.register(TrackingLinks, TrackingLinksAdmin)

admin.site.site_header = "PublishEmail Administration"
admin.site.index_title = ""
