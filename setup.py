try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Flask based idlerpg_site_flask for IdleRPG',
    'author': 'Rusty Bower',
    'url': 'https://github.com/rustybower/idlerpg-idlerpg_site_flask-flask',
    'download_url': 'https://github.com/rustybower/idlerpg-idlerpg_site_flask-flask/archive/master.zip',
    'author_email': 'rusty@rustybower.com',
    'version': '0.0.1',
    'install_requires': [
        # Required Dependencies
        'Flask==0.12',
        # Develpment Dependencies
        'pycodestyle==2.3.1',
        'pytest-cov==2.4.0',
        'pytest==3.0.6',
        'codeclimate-test-reporter==0.2.1',
        'mock==2.0.0'
    ],
    'packages': ['idlerpg_site_flask'],
    'scripts': [],
    'name': 'idlerpg_site_flask'
}

setup(**config)
