$data = Get-Content -Path "input"

function Get-Highest {
    param(
        [string]$subString,
        [int]$Idx
    )

    $retIdx = 0
    $highest = 0
    $strLen = $subString.Length

    for ($i = 0; $i -lt ($strLen - $Idx); $i++) {
        $currChar = $subString[$i]
        $currCharInt = [int][string]$currChar
   
        if ($currCharInt -gt $highest) {
            $highest = $currCharInt
            $retIdx = $i    
        }
    }  

    return @(
        [string]$highest, $retIdx
    )
}

function Iterate {
    param(
        [int]$numsNeeded
    )
   
    $numsNeeded--
    $answer = 0
    $data | ForEach-Object {
        $subString = $_
        $curr = ""
        $idxs = ($numsNeeded..0)
 
        $idxs | ForEach-Object {
            $results = Get-Highest -subString $subString -Idx $_
            $curr += $results[0]
            $subString = $subString.Substring(($results[1] + 1))
        }
        $answer += [long]$curr
    }
    return $answer
}

$p1answer = Iterate 2
$p2answer = Iterate 12

Write-Host "PartOne: $p1answer"
Write-Host "PartTwo: $p2answer"