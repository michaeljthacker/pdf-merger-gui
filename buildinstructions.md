# Building a Windows Executable

## Clean previous builds (optional but recommended)
```bash
Remove-Item -Recurse -Force build, dist, main.spec
```

This command will differ for non-Windows.

## Installing dependencies
Install PyInstaller and PyPDF.

```bash
pip install -r dev-requirements.txt
```
## Build it!
Run the build command:

```bash
pyinstaller --onefile --windowed src/main.py
```

Your `.exe` will be created in the `dist/` folder.

> `--windowed` = prevents terminal window from appearing
> `--onefile` = bundles everything into one `.exe` file

For owners / contributors, you can now upload `dist/main.exe` to the **Releases** tab on GitHub. Otherwise, just keep the build for yourself!