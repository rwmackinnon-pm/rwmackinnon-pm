# Disable Adobe Acrobat Reader DC upsell
$registryPath = "HKLM:\SOFTWARE\Policies\Adobe\Acrobat Acrobat\DC\FeatureLockDown"

# Create the registry path if it doesn't exist
if (!(Test-Path $registryPath)) {
    New-Item -Path $registryPath -Force
}

# Disable upsell
New-ItemProperty -Path $registryPath -Name "bDisableUpsell" -Value 1 -PropertyType DWORD -Force

# Optional: Disable updates
New-ItemProperty -Path $registryPath -Name "bUpdater" -Value 0 -PropertyType DWORD -Force

Write-Host "Adobe Reader upsell disabled successfully"