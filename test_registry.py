# 
from winregistry import WinRegistry as Reg
from pprint import pprint
reg = Reg()

print("-"*10)

path = r'HKLM\SOFTWARE\Microsoft\MSBuild\ToolsVersions\4.0'
try:
  print(f"Attempting to read {path}")
  pprint(reg.read_key(path), width=100)
except:
  pass

print("-"*10)

path = r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\MSBuild\ToolsVersions\4.0'
try:
  print(f"Attempting to read {path}")
  pprint(reg.read_key(path), width=100)
except:
  pass

print("-"*10)
