
# -*- coding: utf-8 -*-
import re
import sys

from pyarrow import _plasma_store_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(_plasma_store_entry_point())
