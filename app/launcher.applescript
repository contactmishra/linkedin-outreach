-- Outreach Desk.app (macOS): starts the local server if needed and opens the dashboard.
-- install.py builds it next to the app/ folder and fills in the Python path.
set appPath to POSIX path of (path to me)
set skillDir to do shell script "dirname " & quoted form of appPath
do shell script "cd " & quoted form of skillDir & " && " & quoted form of "__PYTHON__" & " app/launch.py > /dev/null 2>&1"
