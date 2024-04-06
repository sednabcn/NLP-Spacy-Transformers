from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
setup(name='custom_components',
      version='0.1.0',
      description='Generate custom_ner_components',
      long_description='Generation, build and save custom ner components.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Topic :: OOP Python :: Code',
      ],
      url='http://github.com/sednabcn/sPacy',
      entry_points = {
        'console_scripts': ['custom_components-sample_1=custom_components.script_custom_patterns:pattern_gen','custom_components-sample_2=custom_components.script_custom_ner:get_ner_component'],
      },
      author="Ruperto Pedro Bonet Chaple",
      author_email="ruperto.bonet@modelphysmat.com",
      License=["MIT"],
      #packages=find_packages(),
      packages=['custom_components','custom_components.custom_ner','custom_components.patterns','custom_components.tests'],
      install_requires=[
          'numpy','sPacy','pandas','nltk'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['./custom_components/script_custom_ner.py','./custom_components/script_custom_patterns.py'],
      include_package_data=True,
      zip_safe=False)

