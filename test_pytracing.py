#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import json
import time

from pytracing import TraceProfiler


def function_a(x):
  print('sleeping {}'.format(x))
  time.sleep(x)
  return


def function_b(x):
  function_a(x)


def main():
  function_a(1)
  function_b(1)


if __name__ == '__main__':
  with io.open('./trace.out', mode='w', encoding='utf-8') as fh:
    tp = TraceProfiler(output=fh)
    tp.install()
    main()
    tp.shutdown()
    print('wrote trace.out')

  with io.open('./trace.out', encoding='utf-8') as fh:
    json.load(fh)

