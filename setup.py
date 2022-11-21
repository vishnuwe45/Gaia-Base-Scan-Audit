from setuptools import setup

setup(name='testpipeline',
      description='simple gaia python pipeline example',
      packages=['pipeline'],
      author='pipelineauthor',
      author_email='pipelineauthor@mail.com',
      install_requires=[
            'gaiasdk>=0.0.16',
            'sslyze==5.0.6',
            'securityheaders==0.0.1',
            'sqlmap==1.6.11',
            'BirDuster==1.0',
            'GitPython==3.1.27'
      ])
