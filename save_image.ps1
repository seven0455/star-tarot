$img = document.querySelectorAll('img')[0]
if ($img.src.startswith('data:')) {
    $base64 = $img.src.substring($img.src.indexof(',') + 1)
    [IO.File]::WriteAllBytes("C:\.openclaw\workspace\xiaoqi_avatar.png", [Convert]::FromBase64String($base64))
    "saved"
} else {
    "not base64"
}
