# Octoprint plugin called darkmodeui

plugin_identifier = "darkmodeui"

plugin_package = "octoprint_darkmodeui"

plugin_name = "DarkMode UI"

plugin_version = "0.0.1"

plugin_description = "Dark Mode UI"

plugin_author = "QuinnC"

plugin_author_email = "QuinnC@Alloew.com"

plugin_url = "https://github.com/Alloew/Octoprint-Dark-Mode"

plugin_license = "AGPLv3"

plugin_requires = []

plugin_additional_data = []

plugin_addtional_packages = ["flask"]

plugin_ignored_packages = []

additional_setup_parameters = {}

from setuptools import setup

try:
    import octoprint_setuptools
except:
    print("Could not import OctoPrint's setuptools")
    import sys
    sys.exit(-1)
    
setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	package=plugin_package,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires,
	additional_packages=plugin_addtional_packages,
	ignored_packages=plugin_ignored_packages,
	additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
	from octoprint.util import dict_merge
	setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)