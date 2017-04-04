# -*- mode: python -*-

block_cipher = None

added_files=[('Jalapeno_data','Jalapeno_data'),('Jalapeno','Jalapeno')]
a = Analysis(['JaloLite'],
             pathex=['/Users/Jakob/JaloLite'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='JaloLite',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='Jalo.icns')
app = BUNDLE(exe,
             name='JaloLite.app',
             icon='Jalo.icns',
             bundle_identifier=None)
