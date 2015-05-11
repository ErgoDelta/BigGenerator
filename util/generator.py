# region Imports
from io import StringIO
from mako.exceptions import RichTraceback
from mako.lookup import TemplateLookup
from mako.runtime import Context
import fnmatch
import json
import logging
import os
import re
# endregion
# from StringIO import StringIO


class Generator():
    logging.getLogger()

    # region Variables
    _directory = None
    _models = None
    _templates = None
    _template_lookup = None
    _swagger = None
    _swagger_file = None
    # endregion

    def __init__(self,
                 swagger_file=None,
                 output_encoding='utf-8',
                 encoding_errors='replace',
                 module_directory='/tmp/mako_modules'):
        logging.debug('Generator :: Creating Generator')
        if swagger_file:
            self._swagger_file = swagger_file
            logging.debug('Generator :: Opening : ' + self._swagger_file)
            with open(self._swagger_file) as file:
                json_data = json.load(file)
                logging.debug('Generator :: json_data : ' + str(json_data))
                self._swagger = json_data
                self._models = json_data['definitions']
                self._templates = {}
                self._directory = os.getcwd()

            self._find_all_templates()

        print('Generator :: directory : ' + str(self._directory))
        logging.debug('Generator :: directory : ' + str(self._directory))
        self._template_lookup = TemplateLookup(directories=self._directory,
                                               output_encoding=output_encoding,
                                               encoding_errors=encoding_errors,
                                               module_directory=module_directory)
        logging.debug('Generator :: Created')

    # region Methods
    # region private Methods
    def _serve_template(self, buffer=None, template=None, context=None):
        if not buffer:
            raise ValueError('buffer was unexpectedly None')
        if not template:
            raise ValueError('template was unexpectedly None')
        if not context:
            raise ValueError('context was unexpectedly None')

        template_name = template['file']
        template_location = template['root'] + '/' + template_name
        template_location = template_location.replace(os.getcwd(), '')

        template_output_name = template_name.replace('object', context['model']['name'])
        template_output_name = template['root'] + '/' + template_output_name.replace('.bigg.', '.')
        template_output_file = os.getcwd() + '/generated/' + context['module'] + '/' + template_output_name

        logging.debug('Generator :: Serving Template : ' + template['file'])
        self._ensure_path_exists(path=template_output_file)
        with open(template_output_file, 'w+') as file:
            try:
                logging.debug('Generated File :: Getting Template : ' + template_location)
                template = self._template_lookup.get_template(template_location)

                # Serve the Template
                self._print_mako_context(context=context)
                template.render_context(context)
                template_output = buffer.getvalue()

                # NOTE : this is mostly as a lack of understanding.
                #   MAKO seems to write blank buffer lines when it outputs
                #   these need to be removed before we write the buffer out to
                #   the appropriate file.
                template_output_filtered = filter(lambda x: not re.match(r'^$', x), template_output)
                file.writelines(template_output_filtered)

                # NOTE : This print is supposed to be here to output ever file created to the caller.
                print('Generated File :: ' + template_output_file)
                logging.debug('Generator :: Served Template : ' + template_output_file)
            except:
                traceback = RichTraceback()
                output = "____________________________________________________________________________________________"
                logging.error(output)
                for (filename, line_number, function, line) in traceback.traceback:
                    print("File %s, line : %s, in %s" % (filename, line_number, function))
                    logging.error("File %s, line : %s, in %s" % (filename, line_number, function))

                    print(line, "\n")
                    logging.error(line)

                print("%s: %s" % (str(traceback.error.__class__.__name__), traceback.error))
                logging.error("%s: %s" % (str(traceback.error.__class__.__name__), traceback.error))

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

    def _find_all_templates(self):
        logging.debug('Generator :: Finding All Templates :')

        working_directory = os.getcwd()
        logging.debug('Generator :: working_directory :' + str(working_directory))
        for root, dirs, files in os.walk(working_directory):
            for file in files:
                if fnmatch.fnmatch(file, '*.bigg.*'):
                    logging.debug('Generator :: At location : ' + str(root))
                    logging.debug('Generator :: Found a BigG Template : ' + str(file))
                    self._templates[file] = {}
                    self._templates[file]['root'] = root.replace(working_directory, '')
                    self._templates[file]['file'] = file
    # endregion

    def generate(self):
        logging.debug('Generator :: Generating')
        for template in self._templates:
            logging.debug('Generator :: Template : ================================================================')
            logging.debug('Generator :: Template : ' + template)
            template = self._templates[template]

            for model_name in self._models:
                buffer = StringIO()
                logging.debug('Generator :: Model : -----------------------------------------------------------------')
                logging.debug('Generator :: Model : ' + model_name)
                model = self._models[model_name]
                model['name'] = model_name

                module = os.path.basename(self._swagger_file).replace('.json', '')
                context = Context(buffer, module=module,  swagger=self._swagger, model=model)

                self._serve_template(buffer=buffer, template=template, context=context)
    # endregion

# EOF
