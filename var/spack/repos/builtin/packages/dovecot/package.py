# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dovecot(AutotoolsPackage):
    """Dovecot mail server."""

    homepage = "https://www.dovecot.org/"
    url      = "https://dovecot.org/releases/2.3/dovecot-2.3.11.3.tar.gz"

    version('2.3.11.3', sha256='d3d9ea9010277f57eb5b9f4166a5d2ba539b172bd6d5a2b2529a6db524baafdc')
