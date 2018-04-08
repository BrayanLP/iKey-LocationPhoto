# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="JuegodeTeclas", 
 version="1.0", 
 description="Este es un juego que detecta tus teclas", 
 author="BrayanLP", 
 author_email="brayansystemlp@gmail.com", 
 url="url del proyecto", 
 license="libre", 
 scripts=["test.py"], 
 console=["test.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)