

# https://learn.microsoft.com/en-us/training/modules/deploy-paas-solutions-with-azure-sql/3-explore-single

# Deploying Azure SQL Database Using Azure Resource Manager templates
# Another method for deploying resources is as mentioned earlier using an Azure Resource Manager template. 
# A Resource Manager template gives you the most granular control over your resources, 
# and Microsoft provides a GitHub repository called “Azure-Quickstart-Templates”, 
# which hosts Azure Resource Manager templates that you can reference in your deployments. 
# A PowerShell example of deploying a GitHub based template is shown below:

#Define Variables for parameters to pass to template
$projectName = Read-Host -Prompt "Enter a project name"
$location = Read-Host -Prompt "Enter an Azure location (i.e. centralus)"
$adminUser = Read-Host -Prompt "Enter the SQL server administrator username"
$adminPassword = Read-Host -Prompt "Enter the SQl server administrator password" -AsSecureString
$resourceGroupName = "${projectName}rg"

#Create Resource Group and Deploy Template to Resource Group
New-AzResourceGroup -Name $resourceGroupName -Location $location

New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName `
 -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-sql-logical-server/azuredeploy.json" `
 -administratorLogin $adminUser -administratorLoginPassword $adminPassword

Read-Host -Prompt "Press [ENTER] to continue ..."