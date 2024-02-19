resource "azurerm_storage_account" "tfazstgacc" {
  name                     = "${var.svc_name}stgacc"
  resource_group_name      = var.rg_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags = {
    Owner   = var.tag1_value
    Project = var.tag2_value
  }
}

resource "azurerm_storage_container" "tfazstgaccctn" {
  name                  = "${var.svc_name}stgaccctn"
  storage_account_name  = azurerm_storage_account.tfazstgacc.name
  container_access_type = "blob"
}

data "azurerm_storage_account_blob_container_sas" "tfazblobsas" {
  connection_string = azurerm_storage_account.tfazstgacc.primary_connection_string
  container_name    = azurerm_storage_container.tfazstgaccctn.name
  start             = "2022-01-01"
  expiry            = "2030-01-01"
  permissions {
    read   = true
    add    = true
    create = true
    write  = true
    delete = true
    list   = true
  }
}

resource "azurerm_storage_account_network_rules" "tfazstgaccnetwrules" {
  storage_account_id = azurerm_storage_account.tfazstgacc.id
  default_action = "Allow"
  virtual_network_subnet_ids = []
}
