# -*- mode: python -*-

block_cipher = None

added_files=[('Jalapeno_data','Jalapeno_data'),('Jalapeno','Jalapeno')]
a = Analysis(['JaloLite'],
             pathex=['/home/Jkob/JaloLite'],
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
#exe = EXE(pyz,
#          a.scripts,
#          exclude_binaries=True,
#          name='Jalo',
#          debug=False,
#          strip=False,
#          upx=True,
#          console=False,
#	  manifest='MANIFEST.in'
#	)
exe = BUNDLE(pyz,
          a.scripts,
          exclude_binaries=True,
          debug=False,
          strip=False,
          upx=True,
          console=False,
	  manifest='MANIFEST.in',
          icons= 'Jalo.icns'
	)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Jalo',
	       )

