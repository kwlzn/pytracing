#!/usr/bin/env python2.7

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
  with open('./trace.out', 'wb') as fh:
    tp = TraceProfiler(output=fh)
    tp.install()
    main()
    tp.shutdown()
    print('wrote trace.out')
