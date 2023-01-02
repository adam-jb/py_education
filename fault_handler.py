import faulthandler

def some_function():
    # some code here
    try:
        # code that may raise an exception
        1 / 0  # this will raise a ZeroDivisionError
    except Exception as e:
        # print the traceback of the current thread
        faulthandler.dump_traceback(e)

some_function()