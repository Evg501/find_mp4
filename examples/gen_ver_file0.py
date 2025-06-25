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

template = """from PyInstaller.utils.win32 import versioninfo

vers = versioninfo.VSVersionInfo(
    ffi=versioninfo.FixedFileInfo(
        filevers={filevers},
        prodvers={filevers},
        mask=0x3f,
        flags=0x0,
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        versioninfo.StringFileInfo(
            [
                versioninfo.StringTable(
                    '040904B0',
                    [
                        versioninfo.StringStruct('CompanyName', 'MyCompany'),
                        versioninfo.StringStruct('FileDescription', 'My Awesome App'),
                        versioninfo.StringStruct('FileVersion', '{version}'),
                        versioninfo.StringStruct('InternalName', 'myapp'),
                        versioninfo.StringStruct('LegalCopyright', '© 2025 MyCompany'),
                        versioninfo.StringStruct('OriginalFilename', 'app.exe'),
                        versioninfo.StringStruct('ProductName', 'MyApp'),
                        versioninfo.StringStruct('ProductVersion', '{version}')
                    ]
                )
            ]
        ),
        versioninfo.VarFileInfo([versioninfo.VarStruct('Translation', b'\\x09\\x04\\x00\\x00')])
    ]
)
"""

with open("version_info.txt", "w") as f:
    f.write(template.format(filevers=filevers, version=version))