provider " digitalocean " {
token = var . digitalocean_token
}
resource " digitalocean_droplet " " web " {
image = " ubuntu -20 -04 - x64 "
name = " example - droplet "
region = " nyc1 "
size = "s -1 vcpu -1 gb "
}
variable " digitalocean_token " {
description = " The DigitalOcean API token ."
type = string
sensitive = true
default = " API_TOKEN "
}