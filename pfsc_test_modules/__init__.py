# --------------------------------------------------------------------------- #
# Proofscape Test Modules                                                     #
# Copyright (c) 2011-2022 Proofscape contributors                             #
#                                                                             #
# This Source Code Form is subject to the terms of the Mozilla Public         #
# License, v. 2.0. If a copy of the MPL was not distributed with this         #
# file, You can obtain one at http://mozilla.org/MPL/2.0/.                    #
# --------------------------------------------------------------------------- #

from pathlib import Path

def get_repo_src_dir_path():
    p = Path(__file__)
    return str(p.parent / 'repos')
