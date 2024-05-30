variable "base_name" {
  description = "The base name of the resource:"
  type        = string
}

variable "resource_type" {
  type        = string
  validation {
    condition     = contains(["virtual_machine", "key_vault", "storage_account"], var.resource_type)
    error_message = "The resource_type should be of : ['virtual_machine', 'key_vault', 'storage_account']"
  }
}

locals {
  resource_name = {
    description = "Rule Engine based on the resource_type "
    "virtual_machine" = length(var.base_name) + 5 > 15 ? "vm-${substr(var.base_name, 0, 9)}-00" : "vm-${var.base_name}-00"
    "key_vault"       = lower("kv-${var.base_name}")
    "storage_account" = replace(lower("sa${var.base_name}"), "-", "")
  }
}

output "resource_name" {
  description = "Generated resource name.."
  value       = local.resource_name[var.resource_type]
}
