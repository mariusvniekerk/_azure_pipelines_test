# 

from winregistry import WinRegistry as Reg
reg = Reg()

path = r'HKLM\SOFTWARE\Microsoft\MSBuild\ToolsVersions\4.0'
print(reg.read_value(path, 'VCTargetsPath'))

path = r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\MSBuild\ToolsVersions\4.0'
print(reg.read_value(path, 'VCTargetsPath'))

