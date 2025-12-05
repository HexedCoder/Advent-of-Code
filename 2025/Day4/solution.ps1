function Get-Input {
    $lines = Get-Content -Path "input"
    $array2D = @()

    foreach ($line in $lines) {
        $chars = $line.ToCharArray()
        $array2D += , $chars   # Keep row as char array
    }

    return $array2D
}

function Get-NeighborCount {
    param(
        [object[]]$grid,
        [int]$row,
        [int]$col
    )

    $count = 0
    $rows = $grid.Count

    $directions = @(
        @{ dr = -1; dc = 0 }
        @{ dr = -1; dc = 1 }
        @{ dr = 0; dc = 1 }
        @{ dr = 1; dc = 1 }
        @{ dr = 1; dc = 0 }
        @{ dr = 1; dc = -1 }
        @{ dr = 0; dc = -1 }
        @{ dr = -1; dc = -1 }
    )

    foreach ($dir in $directions) {
        $nr = $row + $dir.dr
        $nc = $col + $dir.dc

        if (
            $nr -ge 0 -and
            $nr -lt $rows -and
            $nc -ge 0 -and
            $nc -lt $grid[$nr].Length
        ) {
            if ($grid[$nr][$nc] -eq '@') {
                $count++
            }
        }
    }

    return $count
}

function Get-Accessible {
    param(
        [object[]]$data,
        [int]$rows,
        [switch]$Move
    )

    $currAccessible = 0

    for ($r = 0; $r -lt $rows; $r++) {
        for ($c = 0; $c -lt $data[$r].Length; $c++) {
            if ($data[$r][$c] -eq '@') {
                $neighbors = Get-NeighborCount -grid $data -row $r -col $c

                if ($neighbors -lt 4) {
                    $currAccessible++

                    if ($Move) {
                        $data[$r][$c] = 'x'
                    }
                }
            }
        }
    }

    return $currAccessible
}

function Get-Storage {
    param(
        [object[]]$data,
        [bool]$continue
    )

    $rows = $data.Count
    $totalAccessible = 0
    
    if (-not $continue) {
        $totalAccessible = Get-Accessible -data $data -rows $rows
    }
    else {
        while ($true) {
            $currAccessible = Get-Accessible -data $data -rows $rows -Move

            if ($currAccessible -eq 0) {
                break
            }

            $totalAccessible += $currAccessible
        }
    }

    return $totalAccessible
}

$data = Get-Input
$p1answer = Get-Storage ($data.Clone()) $false
$p2answer = Get-Storage $data $true

Write-Host "PartOne: $p1answer"
Write-Host "PartTwo: $p2answer"
