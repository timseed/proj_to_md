from setuptools import setup

setup(
    name='proj_to_md',
    version='',
    packages=['tim',  'tim.utils', 'tim.utils.proj2md'],
    entry_points={'console_scripts': ['proj2md=tim.utils.proj2md.__main__:main']},
    license='',
    author='tim seed',
    author_email='tim@sy-edm.com',
    description='Quickly dump a python project into a Markdown output format.'
)
