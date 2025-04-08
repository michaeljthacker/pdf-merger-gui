# Building a Windows Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Run the build command:

```bash
pyinstaller --onefile --windowed src/main.py
```

Your `.exe` will be created in the `dist/` folder.

> `--windowed` = prevents terminal window from appearing
> `--onefile` = bundles everything into one `.exe` file

You can now upload `dist/main.exe` to the **Releases** tab on GitHub.