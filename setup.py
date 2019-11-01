import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.AirtableUtility',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description=u'Airtable utility that programmatically creates questions from airtable fields. \r\n\r\nAdd new fields to airtable and it creates the questions for you, then saves the answers back to airtable. \r\n\r\nDoes not with with select fields due to the limitations of the airtable API\r\n\r\n## Needs Fixing: \r\nThere is some weirdness with the interview mixing up the variable names\r\n\r\nNeed to fix the attachment feature so it sends them to the API properly',
      long_description_content_type='text/markdown',
      author='System Administrator',
      author_email='admin@admin.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['airtable', 'airtable-python-wrapper'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/AirtableUtility/', package='docassemble.AirtableUtility'),
     )

