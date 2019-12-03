import sys
import __main__
import dis

filename = __main__.__file__
with open(filename, "r") as f:
  content = f.read()
content = content.replace("import pycraft", "")
code = compile(content, filename, "exec")
bytecode = dis.Bytecode(code)
print(dis.dis(code))

for instr in bytecode:
  print(instr)

sys.exit()