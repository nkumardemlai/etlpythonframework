@echo off
REM --- Rebuild Script for Winspark Module ---
echo Cleaning up old builds and installations...

REM Navigate to the module directory
cd C:\Users\pedam\github_checkin_code\winspark

REM Remove old build artifacts
if exist build (
    rd /s /q build
    echo Removed old build directory.
)
if exist dist (
    rd /s /q dist
    echo Removed old dist directory.
)
if exist *.egg-info (
    del /q *.egg-info
    echo Removed old egg-info files.
)

REM Uninstall the existing module
pip uninstall -y winspark
if %ERRORLEVEL% NEQ 0 (
    echo "Failed to uninstall. The package may not have been installed."
)

REM Reinstall the module in editable mode
pip install -e .
if %ERRORLEVEL% NEQ 0 (
    echo "Reinstallation failed. Exiting."
    exit /b 1
)

REM Verify the installation
pip show winspark
if %ERRORLEVEL% NEQ 0 (
    echo "Verification failed. Winspark module is not installed."
    exit /b 1
)

REM Run tests
echo Running tests...

REM Create a temporary test script
echo from winspark.spark_utils import getSparkSession > test_script.py
echo from winspark.utils import printc >> test_script.py
echo printc("Testing Winspark Module...") >> test_script.py
echo spark = getSparkSession() >> test_script.py
echo printc("Spark session created successfully!") >> test_script.py
echo spark.stop() >> test_script.py
echo printc("Spark session stopped.") >> test_script.py

REM Execute the test script
python test_script.py
if %ERRORLEVEL% NEQ 0 (
    echo "Tests failed. Please check the test script output."
    exit /b 1
)

REM Clean up temporary test script
del test_script.py
echo Test script executed and cleaned up.

echo Winspark module rebuilt and tested successfully!
exit /b 0
