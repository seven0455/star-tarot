Add-Type -AssemblyName System.Drawing

$img = [System.Drawing.Image]::FromFile("C:\.openclaw\workspace\pet\tarot_icon.png")
$resized = New-Object System.Drawing.Bitmap(144, 144)
$g = [System.Drawing.Graphics]::FromImage($resized)
$g.DrawImage($img, 0, 0, 144, 144)
$resized.Save("C:\.openclaw\workspace\pet\tarot_icon_144.png", [System.Drawing.Imaging.ImageFormat]::Png)

Write-Host "完成: 144x144.png"

$g.Dispose()
$resized.Dispose()
$img.Dispose()
