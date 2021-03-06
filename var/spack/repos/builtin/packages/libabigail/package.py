# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Libabigail(AutotoolsPackage):
    """This is the Application Binary Interface Generic Analysis and
    Instrumentation Library.It aims at constructing, manipulating,
    serializing and de-serializing ABI-relevant artifacts."""

    homepage = "https://sourceware.org/libabigail/"
    url      = "http://mirrors.kernel.org/sourceware/libabigail/libabigail-1.7.tar.gz"

    version('1.7', sha256='27a2a8527cdcc1d7b7b88b288c43d03c543022cee539ca48ada7724303e0c82d')
    version('1.6', sha256='cf3c73bde5bfde6d23e19a7a5c97ba6f9e6c713c6ef176d1c5e62ebe213d4012')
    version('1.5', sha256='442b25ce61c15830939ece3e79f4d2d3a88604b5069982aca0daa051d7b42e6b')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('elfutils')
    depends_on('libxml2')
    depends_on('pkg-config')
    depends_on('doxygen', type='build')
    depends_on('py-sphinx')
