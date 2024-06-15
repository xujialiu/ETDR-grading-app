# Changelog

## 1.1.0 (2024-06-15)
- fix export the wrong table
- fix change combobox_options.json require administrator priviliage
- fix application.exe do not show the right icon
- fix save button click do not clear the comboboxes' choices
- add the following choices / line editor
  - is gradable
  - is DR
  - other diagnosis
  - is confident
- fix install.iss problem
- fix the app infinite recursion in startup caused by `if __name__ == "__main__":` in both main.py and MainWindowImpl.py

todo:
- bug: piction in combobox option do not show properly