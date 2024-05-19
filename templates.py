naming_module_template = """variable "base_name" {
  description = "The base name for the resource."
  type        = string
}

variable "resource_type" {
  description = "The type of resource to be named."
  type        = string
  validation {
    condition     = contains(["virtual_machine", "key_vault", "storage_account"], var.resource_type)
    error_message = "The resource_type must be one of 'virtual_machine', 'key_vault', or 'storage_account'."
  }
}

locals {
  resource_name = {
    "virtual_machine" = length(var.base_name) + 5 > 15 ? substr("vm-${var.base_name}", 0, 15) : "vm-${var.base_name}-00"
    "key_vault"       = lower("kv-${var.base_name}")
    "storage_account" = replace(lower("sa${var.base_name}"), "-", "")
  }
}

resource "null_resource" "resource_name" {
  provisioner "local-exec" {
    command = "echo ${local.resource_name[var.resource_type]}"
  }
}

output "resource_name" {
  description = "The generated resource name."
  value       = local.resource_name[var.resource_type]
}
"""

parent_module_template = """variable "resources" {
  description = "A map of resources with base names as keys and resource types as values."
  type        = map(string)
}

module "naming_modules" {
  source = "../naming_module"

  for_each = var.resources

  base_name     = each.key
  resource_type = each.value
}

output "resource_names" {
  description = "A map of resource names keyed by base names."
  value       = { for k, v in module.naming_modules : k => v.resource_name }
}
"""

test_module_template = """module "parent" {
  source    = "../parent_module"
  resources = {
    "example1" = "virtual_machine"
    "example2" = "key_vault"
    "example3" = "storage_account"
  }
}

output "resource_names" {
  value = module.parent.resource_names
}
"""
