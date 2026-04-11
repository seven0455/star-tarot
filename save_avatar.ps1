# Get base64 from browser and save as PNG
$code = @'
const imgs = document.querySelectorAll('img');
for (const img of imgs) {
    if (img.src.startsWith('data:image/png;base64,')) {
        const base64 = img.src.split(',')[1];
        return base64;
    }
}
return null;
'@
$result = Invoke-Command -ScriptBlock { param($c) } -ArgumentList $code
