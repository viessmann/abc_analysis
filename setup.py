from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='abc_analysis',
      version='0.1.2',
      description='ABC analysis with automated limit detection',
      long_description=readme(),
      download_url='https://github.com/viessmann/abc_analysis/archive/v0.1.2.tar.gz',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
      ],
      keywords='abc-analysis abc_analysis',
      url='https://github.com/viessmann/abc_analysis',
      author='Tino Gehlert',
      author_email='ghlt@viessmann.com',
      license='GNU General Public License v3 (GPLv3)',
      packages=find_packages(),
      install_requires=[
         'pandas>=0.22',
		  'numpy>=1.14',
         'scipy>=1.1.0',
		  'matplotlib>=2.2.2'
      ],
      include_package_data=True,
      zip_safe=False)