# z3950client

An attempt to get a Z39.50 client running in Python 3.5.1 on Windows, and querying NLM's Z3950 server.

## How to use

This queries NLM for MARC data using Z39.50.  It doesn't provide much of a
search interface - it is based on NLM Unique ID, which you can get from the
catalog.   You run it like this:


```
python querynlm.py 101589530
```


## References

- [NLM FAQ on Z39.50](https://www.nlm.nih.gov/services/lpz3950.html)
- [PyZ3950 package](https://github.com/asl2/PyZ3950)
- [Sample client code](http://zoom.z3950.org/bind/python/)
