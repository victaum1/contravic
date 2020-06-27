# from copy import copy

class MockInOut:

    def print(self,s):
        MockInOut.outputs.append(s)

    def input(self,s):
        MockInOut.outputs.append(s)
        return self.inputs.pop(0)

    def __init__(self,inputs = None):
        if inputs is None:
            pass
        else:
            self.inputs = inputs


class FD:
    def close(self):
        MockOpen.close_called = True


class FDR(FD):
    def __init__(self,ins):
        self.input_cad = ins

    def read(self):
        MockOpen.read_called = True
        return self.input_cad


class FDW(FD):
    def write(self,cad):
        MockOpen.write_called = True
        MockOpen.out_cads.append(cad)


class MockOpen:

    def __init__(self, i_cad=None):
        if i_cad is None:
            pass
        else:
            self.input_cad = i_cad

    def open(self, fileName, readMode=None):
      MockOpen.called = True
      if (readMode == None) or (readMode == "r") or (readMode == "r+"):
          if (readMode == None):
              MockOpen.args.append((fileName,"r"))
          else:
              MockOpen.args.append((fileName,readMode))
          return FDR(self.input_cad)
      else:
          MockOpen.args.append((fileName,readMode))
          return FDW()

