
import os
import sos
import sos_notebook

c = get_config()
c.TemplateExporter.template_path.extend([
  os.path.join(os.path.split(os.path.abspath(sos.__file__))[0], 'templates'),
  os.path.join(os.path.split(os.path.abspath(sos_notebook.__file__))[0], 'templates')])
