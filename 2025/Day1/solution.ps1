function Get-Input {
    Get-Content -Path "input"
}

function PartOne {
    $currPosition = 50
    $zeroHits = 0

    foreach ($line in (Get-Input)) {
        $direction = $line[0]
        $steps     = [int]$line.Substring(1).Trim()

        if ($direction -eq "L") {
            $currPosition -= $steps
        }
        else {
            $currPosition += $steps
        }

        $currPosition %= 100

        if ($currPosition -eq 0) {
            $zeroHits++
        }
    }

    return $zeroHits
}

function PartTwo {
    $currPosition = 50
    $zeroHits = 0

    foreach ($line in (Get-Input)) {
        $direction = $line[0]
        $steps     = [int]$line.Substring(1).Trim()
        $prev = $currPosition

        if ($direction -eq "L") {
            $steps *= -1
        }

        # Calculate how many 100-boundaries were crossed, PowerShell's trash modulo
        $totalCrossings = [math]::Floor($($prev + $steps) / 100)
        $zeroCrossings = $totalCrossings -ge 0 ? $totalCrossings : -$totalCrossings

        # Don't count when we started on zero
        if (($prev % 100 -eq 0) -and ($totalCrossings -lt 0)) {
            $zeroCrossings--
        }

        # Normalize position
        $currPosition = ($prev + $steps) - ($totalCrossings * 100)

        # Count landing on zero
        if (($currPosition -eq 0) -and ($steps -lt 0)) {
            $zeroCrossings++
        }

        # Accumulate total zero hits
        $zeroHits += $zeroCrossings
    }

    return $zeroHits
}

function Main {
    $part1 = PartOne
    $part2 = PartTwo
    Write-Output "Part 1: $part1"
    Write-Output "Part 2: $part2"
}

Main
