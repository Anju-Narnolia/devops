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

variable "allowed_ssh" {
default = "0.0.0.0/0"
}

variable "flask_port" {
default = 5000
}


variable "express_port" {
default = 3000
}