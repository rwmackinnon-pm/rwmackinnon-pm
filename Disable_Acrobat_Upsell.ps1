$path = "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown"
$name = "bAcroSuppressUpsell"

# Create Registry Key if it doesn't exist
If (-not(Test-Path $path)) {
    New-Item -Path $path -Force
}

# Create Registry Value
New-ItemProperty -Path $path -Name $name -Value 1 -PropertyType DWORD -Force