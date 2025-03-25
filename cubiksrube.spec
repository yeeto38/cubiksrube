# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['Cubiks_Rube/finalcube.py'],
    pathex=['Cubiks_Rube'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

a.datas += [('Cubiks_Rube/data/keymap.png', 'Cubiks_Rube/data/keymap.png', "DATA")]
a.datas += [('Cubiks_Rube/data/Ubuntu-B.ttf', 'Cubiks_Rube/data/Ubuntu-B.ttf', "DATA")]
a.datas += [('Cubiks_Rube/data/UbuntuMono-R.ttf', 'Cubiks_Rube/data/UbuntuMono-R.ttf', "DATA")]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='finalcube',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='finalcube',
)
