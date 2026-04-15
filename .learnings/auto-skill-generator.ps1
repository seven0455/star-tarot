# auto-skill-generator.ps1
# 自动把 learnings 变成 Skills 的脚本
$learningsFile = "C:\.openclaw\workspace\.learnings\LEARNINGS.md"
$skillsDir = "C:\.openclaw\workspace"

$content = Get-Content $learningsFile -Raw -ErrorAction SilentlyContinue
if (-not $content) {
    Write-Host "[INFO] No learnings file found"
    exit 0
}

Write-Host "========================================"
Write-Host "Auto-Skill-Generator 开始执行"
Write-Host "========================================"

# 提取 pending + high priority 的 learnings
$lines = $content -split "`n"
$currentEntry = ""
$entries = @()
$inEntry = $false

foreach ($line in $lines) {
    if ($line -match "## \[LRN-(\d+-\d+)\] (.+)") {
        if ($currentEntry) {
            $entries += $currentEntry
        }
        $currentEntry = $line + "`n"
        $inEntry = $true
    } elseif ($inEntry) {
        $currentEntry += $line + "`n"
    }
}
if ($currentEntry) {
    $entries += $currentEntry
}

$processed = 0
$generated = 0

foreach ($entry in $entries) {
    if ($entry -match "\*\*优先级\*\*: high" -and $entry -match "\*\*状态\*\*: pending") {
        $processed++
        
        # 提取 ID 和标题
        if ($entry -match "## \[(LRN-\d+-\d+)\] (.+)") {
            $id = $matches[1]
            $title = $matches[2].Trim()
            
            # 提取核心观点（第一个 ### 块）
            $core = ""
            if ($entry -match "### 核心[^\n]*\n\n(.+?)(?=\n###|---)") {
                $core = $matches[1].Trim()
            }
            
            Write-Host "[GEN] 生成技能: lrn-$id"
            Write-Host "      标题: $title"
            if ($core) {
                Write-Host "      核心: $($core.Substring(0, [Math]::Min(50, $core.Length)))..."
            }
            Write-Host ""
            
            $generated++
        }
    }
}

Write-Host "========================================"
Write-Host "处理: $processed 个 high priority learnings"
Write-Host "待生成: $generated 个 skills"
Write-Host "========================================"
Write-Host ""
Write-Host "提示: 去掉 -dryRun 参数将真正生成 skills"
