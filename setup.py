from distutils.core import setup
from Cython.Distutils import build_ext
from distutils.extension import Extension


sources = ['particle.pyx', 'particle.cpp']

setup(
      ext_modules = [Extension("Particle",
                               sources= sources, language="c++")],
      cmdclass = {'build_ext': build_ext}
      
    
      )


#ipython-2.7 notebook


"""
c files

from distutils.core import setup
from Cython.Distutils import build_ext
from distutils.extension import Extension


exts = [Extension("helloCython", sources = ["mycodepy.pyx"], libraries= ["m"])]

setup(
      cmdclass = {'build_ext': build_ext},
      ext_modules = exts,
      )

#ipython-2.7 notebook


"""


