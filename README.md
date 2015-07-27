# pytracing
a python trace profiler that outputs to chrome trace-viewer format (about://tracing).

# usage

    from pytracing import TraceProfiler
    tp = TraceProfiler(output=open('/tmp/trace.out', 'wb'))
    with tp.traced():
      ...execute something here...

# screenshots

![click to view detail](http://kwlzn.github.io/img/pytracing-screen-1.png "click to view detail")

![selection and aggregate view](http://kwlzn.github.io/img/pytracing-screen-2.png "selection and aggregate view")

![zoom](http://kwlzn.github.io/img/pytracing-screen-3.png "zoom")

