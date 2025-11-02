variable "aws_region" {
  default = "ap-south-1"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "key_name" {
  default = "flask-key"
  description = "my flask-express instance"
  type        = string
}

variable "allowed_cidr" {
  default = "0.0.0.0/0"
}
