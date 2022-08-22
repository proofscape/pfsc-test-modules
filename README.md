# `pfsc-test-modules`

This package is a component of the development setup for the
[`pfsc-server`](https://github.com/proofscape/pfsc-server) project.

Its purpose is to support unit tests on somewhat more realistic test cases than
typically occur in the "dummy" examples that make up most basic tests.

All Proofscape modules in this repo are derived from corresponding modules in the
[gh.toepproj.lit](https://github.com/toepproj/lit) and
[gh.toepproj.ex](https://github.com/toepproj/ex) projects.
They are licensed under MPL-2.0.


## `repos` directory

This is structured the same way as the `tests/resources/repo` directory
in `pfsc-server`. It organizes pfsc modules under `user/repo/version`
directories, and is used by the `tests/util/make_repos.py` script of
`pfsc-server` to generate actual test repos under `PFSC_ROOT/lib/test`.
