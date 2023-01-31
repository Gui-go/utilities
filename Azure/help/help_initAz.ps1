
# https://www.dbi-services.com/blog/how-to-create-an-azure-sql-database-using-azure-powershell/
# https://learn.microsoft.com/en-us/azure/azure-sql/database/scripts/create-and-configure-database-powershell?view=azuresql


# Connect-AzAccount
# Connect-AzAccount
# The SubscriptionId in which to create these objects
$SubscriptionId = 'acef547e-ac28-4be8-b6b4-6a240d96947c'
# Set the resource group name and location for your server
$resourceGroupName = "SpillAllOverRG"
$location = "westeurope" # "westus2"; "East US";
# Set an admin login and password for your server
$adminSqlLogin = "SqlAdmin"
$password = "SenhaSuperSecreta123"
# Set server name - the logical server name has to be unique in the system
$serverName = "server-teste1"
# The sample database name
$databaseName = "mySampleDatabase"
# The ip address range that you want to allow to access your server
$startIp = "0.0.0.0"
$endIp = "0.0.0.0"

#
# Set subscription 
Set-AzContext -SubscriptionId $subscriptionId 

# Create a resource group
$resourceGroup = New-AzResourceGroup -Name $resourceGroupName -Location $location

# Create a server with a system wide unique server name
$server = New-AzSqlServer -ResourceGroupName $resourceGroupName `
    -ServerName $serverName `
    -Location $location `
    -SqlAdministratorCredentials $(New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $adminSqlLogin, $(ConvertTo-SecureString -String $password -AsPlainText -Force))

# Create a server firewall rule that allows access from the specified IP range
$serverFirewallRule = New-AzSqlServerFirewallRule -ResourceGroupName $resourceGroupName `
    -ServerName $serverName `
    -FirewallRuleName "AllowedIPs" -StartIpAddress $startIp -EndIpAddress $endIp

# Create a blank database with an S0 performance level
$database = New-AzSqlDatabase  -ResourceGroupName $resourceGroupName `
    -ServerName $serverName `
    -DatabaseName $databaseName `
    -RequestedServiceObjectiveName "S0" `
    -SampleName "AdventureWorksLT"

# Clean up deployment 
# Remove-AzResourceGroup -ResourceGroupName $resourceGroupName


# https://learn.microsoft.com/en-us/powershell/module/az.storage/new-azstorageaccount?view=azps-9.3.0

# Container name:
# Length between 3 and 24 characters with only lowercase letters and numbers.
# Must be globally unique across Azure. Storage account names can't be duplicated in Azure.
$storageacc = "spillalloverstgacc"

# Create storage account
# get-help New-AzStorageContainer -examples
New-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageacc -Location $location -SkuName "Standard_GRS"

# get context credentials
$uploadstorage = Get-AzStorageAccount -ResourceGroupName $resourceGroupName
$storcontext = $uploadstorage.Context


$containerName = "spillalloverctn"

# Creates new container
# man New-AzStorageContainer -examples
New-AzStorageContainer -Name $containerName -Permission Off -Context $storcontext

# Send a file to blob storage
# man Set-AzStorageBlobContent -examples
# Set-AzStorageBlobContent -Container $containerName -File "C:\Users\guilherme.viegas\OneDrive - GFI\Images\mais\bmap.png" -Context $storcontext
# Get-ChildItem -File -Recurse | Set-AzStorageBlobContent -Container "C:\Users\guilherme.viegas\OneDrive - GFI\Images\mais"
Set-AzStorageBlobContent -Container $containerName -File "C:\Users\guilherme.viegas\OneDrive - GFI\Documents\02-spillAllOver\data\df_locations.csv" -Context $storcontext


Invoke-Sqlcmd -InputFile "C:\ScriptFolder\TestSqlCmd.sql" |






# 

# Get-Location
# Get-Service
# Get-Random
# Write-Output "echo echoo"


