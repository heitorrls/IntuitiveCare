# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['index.py'],
    pathex=[],
    binaries=[],
    datas=[('Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', '.'), ('Anexo_II_DUT_2021_RN_465.2021_RN628L.2024.pdf', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='index',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
