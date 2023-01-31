
function checkForNumberTables {

    param(
        [string]$instance = "localhost",
        [string]$db = "master"
    )

    $query = 'USE ' + $db + ' SELECT COUNT(*) AS col1 FROM INFORMATION_SCHEMA.TABLES'

    $Ntables = (Invoke-Sqlcmd -Query $query -ServerInstance $instance).col1
    
    $res = 'The ' + $db + ' db has ' + $Ntables + ' tables'

    Write-Output $res
}


# checkForNumberTables -instance "GFIPT1366\SQLEXPRESS" -db "ODS"

# checkForNumberTables "GFIPT1366\SQLEXPRESS" "ODS" 
