#!/usr/bin/env python

import os
import base64
import pprint

# printing all the env vars
pprint.pprint(dict(os.environ))
# print(len(os.environ['MYSECRET']))
# print(
#     base64.encodebytes(os.environ['MYSECRET'].encode('utf8'))
# )
