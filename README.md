# pytracing
a python trace profiler that outputs to chrome trace-viewer format (about://tracing).

# usage

    from pytracing import TraceProfiler
    tp = TraceProfiler(output=open('/tmp/trace.out', 'wb'))
    tp.install()
    ...
    tp.shutdown()


  alternatively, using the context manager:

    from pytracing import TraceProfiler
    tp = TraceProfiler(output=open('/tmp/trace.out', 'wb'))
    with tp.traced():
      ...
