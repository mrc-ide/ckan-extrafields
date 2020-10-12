# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk

class MRC_IDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def _modify_package_schema(self, schema):
        schema.update({
            'data_type': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'disease_pathogen': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'age_range': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'geography': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'data_start_date': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'data_end_date': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'date_data_received': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'public_url_id': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'original_owner': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'custodian': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'custodian_email': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'changes_made': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'sharable_int': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'sharable_pub': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'data_size': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'extra_lic_info': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')],
            'other_notes': [tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        schema = super(MRC_IDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(MRC_IDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(MRC_IDatasetFormPlugin, self).show_package_schema()
        schema.update({
            'data_type': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'disease_pathogen': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'age_range': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'geography': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'data_start_date': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'data_end_date': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'date_data_received': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'public_url_id': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'original_owner': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'custodian': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'custodian_email': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'changes_made': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'sharable_int': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'sharable_pub': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'data_size': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'extra_lic_info': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')],
            'other_notes': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
