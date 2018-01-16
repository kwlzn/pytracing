#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import time

from pytracing import TraceProfiler


def function_a(x):
  print('sleeping {}'.format(x))
  time.sleep(x)
  return


def function_b(x):
  function_a(x)


def main():
  function_a(5)
  function_b(15)


if __name__ == '__main__':
  with io.open('./trace.out', mode='w', encoding='utf-8') as fh:
    tp = TraceProfiler(output=fh)
    tp.install()
    main()
    tp.shutdown()
    print('wrote trace.out')
