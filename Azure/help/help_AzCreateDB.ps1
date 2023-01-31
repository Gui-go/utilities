
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



