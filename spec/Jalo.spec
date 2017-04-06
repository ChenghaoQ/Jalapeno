# -*- mode: python -*-

block_cipher = None


a = Analysis(['Jalo'],
             pathex=['/Users/Jakob/Ja'],
             binaries=[],
             datas=[('Jalapeno_data','Jalapeno_data'),('Jalapeno','Jalapeno')],
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
          exclude_binaries=True,
          name='Jalo',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='Jalo.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Jalo')
app = BUNDLE(coll,
             name='Jalo.app',
             icon='Jalo.icns',
             bundle_identifier=None,
             info_plist=dict(LSUIElement=True,
                              NSHighResolutionCapable=True))
