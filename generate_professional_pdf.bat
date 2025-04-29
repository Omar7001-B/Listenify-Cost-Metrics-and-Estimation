@echo off
echo Creating a professional PDF with properly rendered MathJax equations...
echo.

REM Check if Node.js is installed
where node >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Node.js is not installed on this system.
    echo Please install Node.js from https://nodejs.org/
    echo.
    echo Note: You can still open project_report_enhanced.html in your browser and print to PDF.
    exit /b 1
)

REM Check if puppeteer is installed
if not exist node_modules\puppeteer (
    echo Installing required Node.js dependencies...
    npm init -y >nul 2>&1
    npm install puppeteer --no-fund --no-audit --loglevel=error
    if %ERRORLEVEL% NEQ 0 (
        echo Error installing dependencies.
        exit /b 1
    )
)

REM Run the Node.js script
echo Running PDF generation script...
node generate_pdf_with_mathjax.js

if %ERRORLEVEL% NEQ 0 (
    echo Error running the PDF generation script.
    echo.
    echo Alternative: Open project_report_enhanced.html in Chrome and use print to PDF.
    exit /b 1
) else (
    echo.
    echo PDF generation complete!
    echo Your professional PDF has been saved as: listenify_project_estimation_professional.pdf
) 