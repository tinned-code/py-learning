# 一键保存：把改动全部提交并推送
# 用法：.\git-save.ps1
#       .\git-save.ps1 -msg "这次改了什么"

param(
    [string]$msg = "日常更新"
)

git add .
git commit -m $msg
git push

Write-Host "已提交并推送" -ForegroundColor Green