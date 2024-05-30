module "parent" {
  source    = "../parent_module"
  resources = {
    "TestingTesting1" = "virtual_machine"
    "TEST2" = "key_vault"
    "TEst--3" = "storage_account"
  }
}

output "resource_names" {
  value = module.parent.resource_names
}
