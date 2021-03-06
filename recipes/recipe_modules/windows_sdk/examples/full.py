# Copyright 2018 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

PYTHON_VERSION_COMPATIBILITY = 'PY2+3'

DEPS = [
  'windows_sdk',
  'recipe_engine/platform',
  'recipe_engine/properties',
  'recipe_engine/step',
]


def RunSteps(api):
  with api.windows_sdk(enabled=api.platform.is_win):
    api.step('gn', ['gn', 'gen', 'out/Release'])
    api.step('ninja', ['ninja', '-C', 'out/Release'])

  # bad arch
  try:
    with api.windows_sdk(target_arch='lolnope'):
      assert False, "never here"  # pragma: no cover
  except ValueError:
    pass


def GenTests(api):
  for platform in ('linux', 'mac', 'win'):
    yield api.test(platform) + api.platform.name(platform)
