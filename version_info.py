from PyInstaller.utils.win32 import versioninfo

vers = versioninfo.VSVersionInfo(
    ffi=versioninfo.FixedFileInfo(
        filevers=(0, 1, 2, 0),
        prodvers=(0, 1, 2, 0),
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
                        versioninfo.StringStruct('FileVersion', '0.1.2'),
                        versioninfo.StringStruct('InternalName', 'myapp'),
                        versioninfo.StringStruct('LegalCopyright', '(c) 2025 MyCompany'),
                        versioninfo.StringStruct('OriginalFilename', 'app.exe'),
                        versioninfo.StringStruct('ProductName', 'MyApp'),
                        versioninfo.StringStruct('ProductVersion', '0.1.2')
                    ]
                )
            ]
        ),
        versioninfo.VarFileInfo([versioninfo.VarStruct('Translation', b'\x09\x04\x00\x00')])
    ]
)

print(vers)