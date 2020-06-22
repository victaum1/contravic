# from copy import copy

class MockInOut:
    outputs = []

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
        self.input_cads = ins

    def read(self):
        MockOpen.read_called = True
        return self.input_cads.pop(0)


class FDW(FD):
    def write(self,cad):
        MockOpen.write_called = True
        MockOpen.out_cads.append(cad)


class MockOpen:
    args = []
    called = False
    read_called = False
    write_called = False
    close_called = False
    out_cads = []

    def __init__(self, i_cads=None):
        if i_cads is None:
            pass
        else:
            self.input_cads = i_cads

    def open(self, fileName, readMode=None):
      MockOpen.called = True
      if readMode == None:
          MockOpen.args.append((fileName,"r"))
          return FDR(self.input_cads)
      else:
          MockOpen.args.append((fileName,readMode))
          return FDW()

