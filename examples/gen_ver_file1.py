# generate_version_file.py
import re

# Получаем версию из __init__.py
#with open("my_app/__init__.py") as f:
with open("__init__.py") as f:    
    version = re.search(r'__version__\s*=\s*"(.*)"', f.read()).group(1)

parts = list(map(int, version.split('.')))
while len(parts) < 4:
    parts.append(0)
filevers = tuple(parts)

template = """
# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers={filevers},
    prodvers={filevers},
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '000004b0',
        [StringStruct('CompanyName', 'Find mp4'),
        StringStruct('FileDescription', 'Find mp4'),
        StringStruct('FileVersion', '{version}'),
        StringStruct('InternalName', 'Find mp4'),
        StringStruct('LegalCopyright', '123'),
        StringStruct('OriginalFilename', 'app.exe'),
        StringStruct('ProductName', 'Find mp4'),
        StringStruct('ProductVersion', '{version}')])
      ]), 
    VarFileInfo([VarStruct('Translation', [0, 1200])])
  ]
)
"""

with open("version_info.res", "w") as f:
    f.write(template.format(filevers=filevers, version=version))