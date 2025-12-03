function Get-Input {
    $content = Get-Content -Path "input"
    return $content -split ","
}

function PartOne {
    $invalidNums = 0

    foreach ($line in (Get-Input)) {
        $minValue, $maxValue = $line -split "-"

        if (($minValue.Length % 2 -ne 0) -and ($minValue.Length -eq $maxValue.Length)) {
            continue
        } 

        $minValue = [long]$minValue
        $maxValue = [long]$maxValue

        for ($i = $minValue; $i -le $maxValue; $i++) {
            $strVal = $i.ToString()
            if ($strVal.Length % 2 -ne 0) {
                continue
            }

            # Split the string in half
            $firstHalf = $strVal.Substring(0, $strVal.Length / 2)
            $secondHalf = $strVal.Substring($strVal.Length / 2)

            if ($firstHalf -eq $secondHalf) {
                $invalidNums += $i
            }
        }
    }

    return $invalidNums
}

function PartTwo {
    [long]$invalidNums = 0
    $seen = New-Object 'System.Collections.Generic.HashSet[long]'

    foreach ($line in (Get-Input)) {
        $minValue, $maxValue = $line -split "-"
        $minValue = [long]$minValue
        $maxValue = [long]$maxValue

        $minDigits = $minValue.ToString().Length
        $maxDigits = $maxValue.ToString().Length

        for ($len = $minDigits; $len -le $maxDigits; $len++) {
            if ($len -lt 2) { continue }

            for ($split = 1; $split -le ($len / 2); $split++) {
                if ($len % $split -ne 0) { continue }

                $repeatCount = [int]($len / $split)

                [long]$base = 1
                for ($k = 0; $k -lt $split; $k++) { $base *= 10 }

                [long]$start = [long]($base / 10)
                [long]$end   = [long]($base - 1)

                for ($half = $start; $half -le $end; $half++) {
                    [long]$candidate = 0
                    for ($i = 0; $i -lt $repeatCount; $i++) {
                        $candidate = $candidate * $base + $half
                    }

                    if ($candidate -ge $minValue -and $candidate -le $maxValue) {
                        if ($seen.Add($candidate)) {
                            $invalidNums += $candidate
                        }
                    }
                }
            }
        }
    }

    return $invalidNums
}


function Main {
    $part1 = PartOne
    $part2 = PartTwo
    Write-Output "Part 1: $part1"
    Write-Output "Part 2: $part2"
}

Main
