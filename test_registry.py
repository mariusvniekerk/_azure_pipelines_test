# 
from winregistry import WinRegistry as Reg
reg = Reg()

print("-"*10)

path = r'HKLM\SOFTWARE\Microsoft\MSBuild\ToolsVersions\4.0'
try:
  print(f"Attempting to read {path}")
  print(reg.read_key(path))
except:
  pass

print("-"*10)

path = r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\MSBuild\ToolsVersions\4.0'
try:
  print(f"Attempting to read {path}")
  print(reg.read_key(path))
except:
  pass

print("-"*10)
