import pathlib

def main():
    text_array = [
        "# -*- mode: python ; coding: utf-8 -*-",
        "",
        "a = Analysis(",
        "    ['Cubiks_Rube/finalcube.py'],",
        "    pathex=['Cubiks_Rube'],",
        "    binaries=[],",
        "    datas=[],",
        "    hiddenimports=[],",
        "    hookspath=[],",
        "    hooksconfig={},",
        "    runtime_hooks=[],",
        "    excludes=[],",
        "    noarchive=False,",
        "    optimize=0,",
        ")",
        ""]
    data_dir = pathlib.Path('Cubiks_Rube/data')
    for file in data_dir.iterdir():
        if file.is_file():
            text_array.append(f"a.datas += [('{file}', '{file}', \"DATA\")]")
    text_array += [
        "",
        "pyz = PYZ(a.pure)",
        "",
        "exe = EXE(",
        "    pyz,",
        "    a.scripts,",
        "    [],",
        "    exclude_binaries=True,",
        "    name='finalcube',",
        "    debug=False,",
        "    bootloader_ignore_signals=False,",
        "    strip=False,",
        "    upx=True,",
        "    console=False,",
        "    disable_windowed_traceback=False,",
        "    argv_emulation=False,",
        "    target_arch=None,",
        "    codesign_identity=None,",
        "    entitlements_file=None,",
        ")",
        "coll = COLLECT(",
        "    exe,",
        "    a.binaries,",
        "    a.datas,",
        "    strip=False,",
        "    upx=True,",
        "    upx_exclude=[],",
        "    name='finalcube',",
        ")"
    ]

    with open('cubiksrube.spec', 'w+') as f:
        for line in text_array:
            f.write(line + '\n')
    
    with open('times.csv', 'w+') as f:
        f.write("")
        
if __name__ == "__main__":
    main()