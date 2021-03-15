from setuptools import setup

APP = ['calculator.py']
OPTIONS = {
    # 'iconfile':'logoapp.icns',
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app = APP,
    options = {'py2app':OPTIONS},
    setup_requires=['py2app']
)