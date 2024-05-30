variable "resources" {
  description = "A map is created based with keys as base names and values resource types."
  type        = map(string)
}

module "naming_modules" {
  source = "../naming_module"

  for_each = var.resources

  base_name     = each.key
  resource_type = each.value
}

output "resource_names" {
  value       = { for k, v in module.naming_modules : k => v.resource_name }
}
