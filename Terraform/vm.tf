provider "azurerm" {
  features {}
  skip_provider_registration = true
}

variable "rg_name" {
  type = string
  default = "rg-GIS"
}

variable "svc_name" {
  type = string
  default = "gisVM"
}

resource "azurerm_virtual_network" "tfazvnet" {
  name                = "${var.svc_name}-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "westeurope"
  resource_group_name = var.rg_name
}

resource "azurerm_subnet" "tfazsubnet" {
  name                 = "${var.svc_name}-snet"
  resource_group_name  = var.rg_name
  address_prefixes     = ["10.0.1.0/24"]
  virtual_network_name = azurerm_virtual_network.tfazvnet.name
}

resource "azurerm_public_ip" "tfazpubip" {
  name                = "${var.svc_name}-pubip"
  location            = "westeurope"
  resource_group_name = var.rg_name
  allocation_method   = "Static"
}

resource "azurerm_network_interface" "tfaznic" {
  name                = "${var.svc_name}-ni"
  location            = "westeurope"
  resource_group_name = var.rg_name
  ip_configuration {
    name                          = "${var.svc_name}-intip"
    subnet_id                     = azurerm_subnet.tfazsubnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.tfazpubip.id
  }
}

resource "azurerm_linux_virtual_machine" "tfazvmachine" {
  name                   = "${var.svc_name}-vm"
  location               = "westeurope"
  resource_group_name    = var.rg_name
  network_interface_ids  = [azurerm_network_interface.tfaznic.id]
  admin_username         = "useradmin"
  admin_password         = "Passwd123" # data.azurerm_key_vault_secret.tfazkvsecret.value
  computer_name          = "azvmgis"
  disable_password_authentication = false
  size                   = "Standard_B2s"
  os_disk {
    storage_account_type = "Standard_LRS"
    disk_size_gb         = "128"
    caching              = "ReadWrite"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "20.04-LTS"
    version   = "latest"
  }
}

resource "azurerm_network_security_group" "tfaznsg" {
  name                = "${var.svc_name}-nsg"
  location            = "westeurope"
  resource_group_name = var.rg_name
  security_rule {
    name                       = "allow-ssh"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "allow-rdp"
    priority                   = 101
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "3389"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "Allow-HTTP"
    priority                   = 200
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "80"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "Allow-HTTPS"
    priority                   = 201
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "allow-geoserver-http"
    priority                   = 300
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "8080"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "allow-postgresql"
    priority                   = 400
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "5432"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "Allow-Outbound"
    priority                   = 500
    direction                  = "Outbound"
    access                     = "Allow"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "deny-inbound"
    priority                   = 600
    direction                  = "Inbound"
    access                     = "Deny"
    protocol                   = "*"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_network_interface_security_group_association" "tfazninsg" {
  network_interface_id      = azurerm_network_interface.tfaznic.id
  network_security_group_id = azurerm_network_security_group.tfaznsg.id
}

