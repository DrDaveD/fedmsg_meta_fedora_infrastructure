# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#           Pierre-Yves Chibon <pingou@pingoured.fr>
#
""" Tests for anitya messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from common import add_doc


class TestNewDistro(Base):
    """ These messages are published when a new Linux distribution is added
    to the database of `anitya <http://release-monitoring.org>`_.
    """
    expected_title = "anitya.distro.add"
    expected_subti = 'ralph added the distro named "Fedora" to anitya'
    expected_link = "http://release-monitoring.org/distros"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['distros/Fedora'])
    msg = {
        u'i': 1,
        u'msg': {
            u'distro': {
                u'name': u'Fedora',
            },
            u'message': {
                u'agent': u'rbean@redhat.com',
                u'distro': u'Debian',
            },
            u'project': None,
        },
        "i": 2,
        "timestamp": 1386821177,
        "msg_id": "2013-d814724a-8ca3-4e8d-936a-e4195e93336c",
        "topic": "org.fedoraproject.prod.anitya.distro.add",
    }


class TestEditDistro(Base):
    """ These messages are published when a Linux distribution's entry is
    edited in the `anitya <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.distro.edit"
    expected_subti = 'ralph changed a distro name from "Fedora" to "FancyHat"'
    expected_link = "http://release-monitoring.org/distros"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['distros/Fedora', 'distros/FancyHat'])
    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1386821512,
        "msg_id": "2013-f18cfb35-894d-41e6-9fda-6f7b99e7e003",
        "topic": "org.fedoraproject.prod.anitya.distro.edit",
        "msg": {
            "project": None,
            "message": {
                "new": "FancyHat",
                "old": "Fedora",
                "agent": "rbean@redhat.com"
            },
            "distro": {
                "name": "Fedora"
            }
        }
    }


class TestAddProject(Base):
    """ These messages are published when someone adds a new project to
    `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.add"
    expected_subti = 'ralph added the project "ansi2html" to anitya'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/ansi2html'])
    msg = {
        "username": "apache",
        "i": 4,
        "timestamp": 1386821688,
        "msg_id": "2013-154429ec-842e-4d7f-acae-8d7434b4cbff",
        "topic": "org.fedoraproject.prod.anitya.project.add",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386839688.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386839688.0,
                "packages": [],
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "agent": "rbean@redhat.com"
            },
            "distro": None,
        }
    }


class TestAddProjectTried(Base):
    """ These messages are published when someone *tries* to add a new project
    to `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.add.tried"
    expected_subti = 'ralph tried to add the project "ansi2html" to anitya'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/ansi2html'])
    msg = {
        "username": "apache",
        "i": 4,
        "timestamp": 1386821688,
        "msg_id": "2013-154429ec-842e-4d7f-acae-8d7434b4cbff",
        "topic": "org.fedoraproject.prod.anitya.project.add.tried",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386839688.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386839688.0,
                "packages": [],
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "agent": "rbean@redhat.com"
            },
            "distro": None,
        }
    }


class TestEditProject(Base):
    """ These messages are published when someone edits the details of a
    project in `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.edit"
    expected_subti = 'ralph edited the following fields of the "ansi2html"' + \
        ' project: homepage, regex'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/ansi2html'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1386822064,
        "msg_id": "2013-35ba0f89-762e-4ed2-a686-484a6862beb6",
        "topic": "org.fedoraproject.prod.anitya.project.edit",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386839688.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386840021.0,
                "packages": [],
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "fields": [
                    "homepage",
                    "regex"
                ],
                "agent": "rbean@redhat.com"
            },
            "distro": None
        }
    }


class TestRemoveProject(Base):
    """ These messages are published when someone *removes* a project from
    `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.remove"
    expected_subti = 'ralph deleted the "ansi2html" project'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/ansi2html'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1386822329,
        "msg_id": "2013-738f0d92-221e-4894-a3bc-5bf865199529",
        "topic": "org.fedoraproject.prod.anitya.project.remove",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386839688.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386840064.0,
                "packages": [],
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "agent": "rbean@redhat.com"
            },
            "distro": None
        }
    }


class TestNewMappingProject(Base):
    """ These messages are published when someone maps an upstream project to a
    package name in a particular distribution (in the `anitya
    <http://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.new"
    expected_subti = 'ralph mapped the name of "ansi2html" in Fedora to' + \
        ' "python-ansi2html"'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set(['python-ansi2html'])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'projects/ansi2html',
        'mappings/Fedora/python-ansi2html',
        'distros/Fedora',
    ])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1386823075,
        "msg_id": "2013-7e860d4e-d9eb-41c6-b693-f0786b45db19",
        "topic": "org.fedoraproject.prod.anitya.project.map.new",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386838297.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386838297.0,
                "homepage": "ansi2html.com",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "new": "python-ansi2html",
                "agent": "rbean@redhat.com",
                "distro": "Fedora"
            },
            "distro": {
                "name": "Fedora",
            },
        }
    }


class TestUpdatedMappingProject(Base):
    """ These messages are published when someone updates the mapping between
    an upstream project and a package name in a particular distribution
    (in the `anitya <http://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.update"
    expected_subti = 'ralph updated the name of "ansi2html" in "Fedora" ' + \
        'from "python-ansi2html" to "python3-ansi2html"'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([
        'python-ansi2html',
        'python3-ansi2html',
    ])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'projects/ansi2html',
        'mappings/Fedora/python-ansi2html',
        'mappings/Fedora/python3-ansi2html',
        'distros/Fedora',
    ])
    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1386824705,
        "msg_id": "2013-319d6a62-827c-458b-971c-6528f6e71dc3",
        "topic": "org.fedoraproject.prod.anitya.project.map.update",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386842519.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386842519.0,
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "edited": [
                    "package_name"
                ],
                "agent": "ralph@fedoraproject.org",
                "project": "guake",
                "new": "guake2",
                "prev": "guake",
                "distro": "Fedora"
            },
            "distro": {
                "name": "Fedora"
            }
        }
    }


class TestNewUpstreamVersion(Base):
    """ The purpose of anitya is to monitor upstream projects and to
    try and detect when they release new tarballs.  *These* messages are the
    ones that get published when a tarball is found that is newer than the
    one last seen in the `anitya <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.version.update"
    expected_subti = 'A new version of "aspell" has been detected:  ' + \
        '"0.60.6.1" in advance of "0.60.6"'
    expected_link = "http://release-monitoring.org/project/5/"
    expected_icon = "https://todo.com/image.png"
    #expected_secondary_icon = None
    expected_packages = set([
        'aspell',
    ])
    expected_usernames = set([])
    expected_objects = set([
        'projects/aspell',
    ])
    msg = {
        "username": "fedmsg",
        "i": 1,
        "timestamp": 1412234961,
        "msg_id": "2014-f4dfc3e4-8909-45d7-b929-1862efb373cf",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.anitya.project.version.update",
        "msg": {
            "project": {
                "id": 5,
                "regex": None,
                "name": "aspell",
                "created_on": 1412174948.0,
                "version": "0.60.6.1",
                "version_url": None,
                "updated_on": 1412232860.0,
                "homepage": "http://www.gnu.org/software/aspell/",
                "backend": "GNU project"
            },
            "packages": [
                {
                    "package_name": "aspell",
                    "distro": "Fedora"
                }
            ],
            "old_version": "0.60.6",
            "upstream_version": "0.60.6.1",
            "versions": [
                "0.60.6.1"
            ]
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
