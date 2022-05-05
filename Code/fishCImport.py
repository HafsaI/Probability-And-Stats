import marshal

try:
    s = open('fishC.pyc', 'rb')
    s.seek(16)  # go past first 16 bytes
    code_obj = marshal.load(s)
    exec(code_obj)
    print("Import Succeeded")
except:
    raise Exception("Function import error. Reach out to TA")
