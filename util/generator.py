# region Imports
from io import StringIO
from itertools import chain
from mako import exceptions
from mako.exceptions import RichTraceback
from mako.lookup import TemplateLookup
from mako.runtime import Context
from mako.template import Template
import json
import logging
import os
import re
# endregion
# from StringIO import StringIO

class Generator():
    logging.getLogger()

    # region Variables
    _template_lookup = None
    _project_file = None
    _directory = None
    _models = None
    _templates = None
    # endregion

    def __init__(self,
                 project_file=None,
                 output_encoding='utf-8',
                 encoding_errors='replace',
                 module_directory='/tmp/mako_modules'):
        logging.debug('Generator :: Creating Generator')
        self._module = project_file.replace('\\','').split('.')[1]
        self._project_file = os.getcwd() + '/projects/' + project_file
        if not os.path.isfile(self._project_file) :
            raise FileNotFoundError(self._project_file)

        # TODO : load the given project file and then use it's information to
        #   build TemplateLookup
        logging.debug('Generator :: Opening : ' + self._project_file)
        with open(self._project_file) as file:
            json_data = json.load(file)
            logging.debug('Generator :: json_data : ' + str(json_data))

            self._rest_api_file = os.getcwd() + '/REST/' + json_data['rest_api'] + '.rest.json'
            self._directory = os.getcwd() + '/templates/' + json_data['directory']
            self._templates = json_data['templates']

        # TODO : load the models for the project files REST API
        logging.debug('Generator :: Opening : ' + self._rest_api_file)
        with open(self._rest_api_file) as file:
            json_data = json.load(file)
            logging.debug('Generator :: json_data : ' + str(json_data))
            self._models = json_data['models']

        self._template_lookup = TemplateLookup(directories=self._directory,
                                                output_encoding=output_encoding,
                                                encoding_errors=encoding_errors,
                                                module_directory=module_directory)
        logging.debug('Generator :: Created')

    # region Methods
    # region private Methods
    def _serve_template(self, buffer=None, template_name=None, context=None):
        if not buffer:
            raise ValueError('buffer was unexpectedly None')
        if not template_name:
            raise ValueError('template_name was unexpectedly None')
        if not context:
            raise ValueError('context was unexpectedly None')

        logging.debug('Generator :: Serving Template : ' + template_name)
        template_output_name = template_name.replace('object', context['model']['name'])
        template_output_file = os.getcwd() + '/generated/' + context['module'] + '/' + template_output_name + '.js'

        self._ensure_path_exists(path=template_output_file)
        with open(template_output_file, 'w+') as file:
            try:
                template = self._template_lookup.get_template(template_name + '.tmpl.bigg')

                # Serve the Template
                self._print_mako_context(context=context)
                template.render_context(context)
                template_output = buffer.getvalue()

                # NOTE : this is mostly as a lack of understanding.
                #   MAKO seems to write blank buffer lines when it outputs
                #   these need to be removed before we write the buffer out to
                #   the approprate file.
                template_output_filtered = filter(lambda x: not re.match(r'^$', x), template_output)
                file.writelines(template_output_filtered)

                print('Generated File :: ' + template_output_file)
                logging.debug('Generator :: Served Template : ' + template_output_file)
            except:
                traceback = RichTraceback()
                for (filename, line_number, function, line) in traceback.traceback :
                    print("File %s, line : %s, in %s" % (filename, line_number, function))
                    print(line, "\n")
                print("%s: %s" % (str(traceback.error.__class__.__name__), traceback.error))

    def _ensure_path_exists(self, path):
        logging.debug('Generator :: Ensuring Path Exists : ' + path)
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
                os.makedirs(dir)

    def _print_mako_context(self, context):
        logging.debug('Generator :: Template Context :')
        for key in context.keys():
            value = context.get(key, default=None)
            logging.debug('Generator :: key : ' + str(key) + ' | value : ' + str(value))
    # endregion

    def generate(self):
        logging.debug('Generator :: Generating')
        for template in self._templates:
            template_name = template
            template = self._templates[template]
            if (('is_not_model_template' in template) and
                (template['is_not_model_template'])) :
                # Just need to generate this template once
                buffer = StringIO()
                context = Context(buffer)
                self._serve_template(buffer, template_name, context)
            else:
                # Loop over each template and genereate it for each given model
                for model in self._models:
                    buffer = StringIO()
                    context = Context(buffer, module=self._module, model=model)
                    self._serve_template(buffer, template_name, context)
    # endregion

# EOF
