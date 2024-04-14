from setuptools import setup, find_namespace_packages
import setuptools_scm

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
      name='custom_components',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Generate custom_ner_components',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Topic :: OOP Python :: Code',
      ],
      url='http://github.com/sednabcn/sPacy',
      author="Ruperto Pedro Bonet Chaple",
      author_email="ruperto.bonet@modelphysmat.com",
      license="MIT",
      packages=find_namespace_packages(),
      entry_points = {
        'console_scripts': [
            'pattern_gen=custom_components.scripts_.script_custom_patterns:pattern_gen',
            'get_ner_component=custom_components.scripts_.script_custom_ner:get_ner_component',
            'get_ner_entity=custom_components.scripts_.script_custom_entities:get_ner_entity',
            'get_normalization=custom_components.scripts_.script_normalize_datasets:get_normalization'
        ]},

      package_data={"": ["*.xlsx","*.json","*.spacy","*.cfg","*.txt","*.bin"],
         "data_spacy.ner_desc":["*"],
         "data_spacy.ner_formulas":["*"],
         "data_spacy.ner_desc.lemmatizer.lookups":["*"],
         "data_spacy.ner_formulas.parser":["*"],
         "data_spacy.ner_formulas.vocab":["*"],
         "data_spacy.ner_formulas.tagger":["*"],
         "data_spacy.ner_formulas.tok2vec":["*"]  
      },
      exclude_package_data={'custom_components':['__pycache__']},
      
      test_suite='pytest.collector',
      tests_require=['pytest'],
      scripts=[
        "custom_components/scripts_/script_custom_entities.py",
        "custom_components/scripts_/script_custom_ner.py",
        "custom_components/scripts_/script_custom_patterns.py",
        "custom_components/scripts_/script_normalize_datasets.py"
    ],
      
      include_package_data=True,
      zip_safe=False)

