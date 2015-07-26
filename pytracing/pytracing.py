import json
import os
import sys
import threading
import time


def to_microseconds(s):
  return 1000000 * float(s)


class TraceProfiler(object):
  """A python trace profiler that outputs Chrome Trace-Viewer format (about://tracing).

     Usage:

        from pytracing import TraceProfiler
        tp = TraceProfiler(output=open('/tmp/trace.out', 'wb'))
        tp.install()
        ...
        tp.shutdown()

  """
  TYPES = {'call': 'B', 'return': 'E'}
  WRITE_LOCK = threading.Lock()

  def __init__(self, output, clock=None):
    self._output = output
    self.clock = clock or time.time
    self.pid = os.getpid()

  @property
  def thread_id(self):
    return threading.current_thread().name

  def install(self):
    """Install the trace function and open the JSON output stream."""
    self._open_collection()
    sys.setprofile(self.tracer)
    threading.setprofile(self.tracer)

  def shutdown(self):
    sys.setprofile(None)
    threading.setprofile(None)
    self._close_collection()

  def _open_collection(self):
    """Write the opening of a JSON array to the output."""
    self._output.write('[\n')

  def _close_collection(self):
    """Write the closing of a JSON array to the output."""
    self._output.write(']\n')

  def fire_event(self, event_type, func_name, func_filename, func_line_no,
                 caller_filename, caller_line_no):
    """Write a trace event to the output stream."""
    timestamp = to_microseconds(self.clock())
    # https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview
    event = json.dumps(
              dict(
                name=func_name,               # Event Name.
                cat=func_filename,            # Event Category.
                tid=self.thread_id,           # Thread ID.
                ph=self.TYPES[event_type],    # Event Type.
                pid=self.pid,                 # Process ID.
                ts=timestamp,                 # Timestamp.
                args=dict(
                  function=':'.join([str(x) for x in (func_filename, func_line_no, func_name)]),
                  caller=':'.join([str(x) for x in (caller_filename, caller_line_no)]),
                )
              )
            )

    with self.WRITE_LOCK:
      self._output.write(event + ',\n')

  def tracer(self, frame, event_type, arg):
    """Bound tracer function for sys.settrace()."""
    if event_type in self.TYPES.keys() and frame.f_code.co_name != 'write':
      self.fire_event(
        event_type=event_type,
        func_name=frame.f_code.co_name,
        func_filename=frame.f_code.co_filename,
        func_line_no=frame.f_lineno,
        caller_filename=frame.f_back.f_code.co_filename,
        caller_line_no=frame.f_back.f_lineno,
      )
