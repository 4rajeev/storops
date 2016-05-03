# coding=utf-8
# Copyright (c) 2015 EMC Corporation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from __future__ import unicode_literals

from hamcrest import assert_that, equal_to

__author__ = 'Cedric Zhuang'


def test_create_fs_success(unity_gf):
    server = unity_gf.nas_server
    name = unity_gf.add_fs_name()
    fs = unity_gf.pool.create_filesystem(
        server, name, 3 * 1024 ** 3)
    assert_that(fs.existed, equal_to(True))


def test_create_delete_snapshot(unity_gf):
    fs = unity_gf.nfs_share.filesystem
    snap = fs.create_snap()
    assert_that(snap.existed, equal_to(True))
    snap.delete()
