# -*- mode: python -*-

block_cipher = None


a = Analysis(['finalcube.py'],
             pathex=['C:/Users/jasonhuang/Documents/ENGR133/Student/Cubiks Rube/'], # just the directory not the file
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('UbuntuMono-R.ttf','/Users/jasonhuang/Documents/ENGR133/Student/Cubiks Rube/UbuntuMono-R.ttf', "DATA")]
a.datas += [('Ubuntu-B.ttf','/Users/jasonhuang/Documents/ENGR133/Student/Cubiks Rube/Ubuntu-B.ttf', "DATA")]
a.datas += [('keymap.png','/Users/jasonhuang/Documents/ENGR133/Student/Cubiks Rube/keymap.png', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)

exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='finalcube',
      debug=False,
      strip=False,
      upx=True,
      console=False
)