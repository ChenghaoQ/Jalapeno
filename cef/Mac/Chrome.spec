# -*- mode: python -*-

block_cipher = None

data_files=[('Chromium Embedded Framework.framework','Chromium Embedded Framework.framework'),('subprocess','.')]
a = Analysis(['Chrome.py'],
             pathex=['/Users/Jakob/ENV/test2'],
             binaries=[],
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.binaries =[each for each in a.binaries
         if 'Chromium Embedded Framework' not in each]
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Chrome',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Chrome')
