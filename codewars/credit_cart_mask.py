"""
link for trian : https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!'
"""

# *****************************************************************
def maskify(cc):
    if len(cc) < 2 :
        return cc
    elif len(cc) < 1 :
        return ""
    lst_hid = ['#' * len(cc[:-4])]
    lst_nw = cc[-4::]
    lst_hid.append(lst_nw)
    att_lst = ''.join(lst_hid)
    return att_lst
# *******************************************************************

"""
second way : 
def maskify(cc):
    return cc[-4:].rjust(len(cc), "#")
"""