# -*- mode: python -*-

block_cipher = None

import shutil


DISTPATH = "dist"
shutil.copyfile("pydownloader.cfg", '{0}/{1}'.format(DISTPATH, "pydownloader.cfg"))
shutil.copyfile("pydownloader.csv", '{0}/{1}'.format(DISTPATH, "pydownloader.csv"))


a = Analysis(['main.py'],
             pathex=['E:\\dev\\python\\tools\\pydownloader\\src'],
             binaries=[],
             datas=[],
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
          #Tree('resource', prefix='resource'),
          #Tree('captured/config/', prefix='config'),
          a.zipfiles,
          a.datas,
          name='pydownloader',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True,
          icon='resource/icon.ico',

          )
