
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
Set-AzStorageBlobContent -Container $containerName -File "C:\Users\guilherme.viegas\OneDrive - GFI\Images\mais\bmap.png" -Context $storcontext
# Get-ChildItem -File -Recurse | Set-AzStorageBlobContent -Container "C:\Users\guilherme.viegas\OneDrive - GFI\Images\mais"

