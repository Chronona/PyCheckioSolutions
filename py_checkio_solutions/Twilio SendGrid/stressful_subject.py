#!/usr/local/bin/checkio --domain=py run stressful-subject

# 
# END_DESC

import re
def is_stressful(subj):
    if subj.isupper() or subj.endswith("!!!") or "a.s.a.p" in subj.lower():
        return True
    subj_no_symbol = "".join([i for i in subj.lower() if i.isalpha()])
    if re.search(r"h+e+l+p", subj_no_symbol):
        return True
    elif re.search(r"u+r+g+e+n+t", subj_no_symbol):
        return True
    else:
        return False