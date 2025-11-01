provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}

resource "kubernetes_namespace" "example" {
  metadata {
    name = "my-first-namespace"
  }
}
# Deployment
resource "kubernetes_deployment" "app" {
  metadata {
    name      = "my-app"
    namespace = kubernetes_namespace.example.metadata[0].name
    labels = {
      app = "my-app"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "my-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "my-app"
        }
      }

      spec {
        container {
          name  = "my-app"
          image = "nginx:latest"
          port {
            container_port = 80
          }
        }
      }
    }
  }
}

# Expose the Deployment with a Service
# resource "kubernetes_service" "app_service" {
#   metadata {
#     name      = "my-app-service"
#     namespace = kubernetes_namespace.example.metadata[0].name
#   }

#   spec {
#     selector = {
#       app = "my-app"
#     }

#     port {
#       port        = 80
#       target_port = 80
#     }

#     type = "NodePort"
#   }
# }
