# Kubernetes Tutorial Projectflow

## Prerequisites

1. **Docker Desktop**: Ensure Docker Desktop is installed and running.
2. **Docker Hub**: Sign in to Docker Hub.
3. **Minikube**: Install Minikube (instructions provided below).

---

## Steps to Execute the Project

### **1. Build the Application**
1. Create or use an existing application.
2. Test it locally to ensure it works as expected.

---

### **2. Prepare and Build the Docker Image**

1. Create a `Dockerfile` in your project directory.
2. Build the Docker image:
   ```bash
   docker build -t kubernetes-test-app:latest .
   ```
3. Verify the image:
   ```bash
   docker images
   ```
4. Test the image locally:
   ```bash
   docker run -p 5000:5000 kubernetes-test-app:latest
   ```

---

### **3. Create the Deployment YAML File**
Define a Kubernetes deployment in a file named `deployment.yaml`.

---

### **4. Install Minikube**

1. Visit the Minikube installation page: [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download).
2. Download the `.exe` file and execute the installation via PowerShell as an administrator.
3. Restart your terminal after the installation (a system reboot may be required).

Start Minikube:
```bash
minikube start
# or
minikube start --embed-certs
```

---

### **5. Troubleshooting Minikube**

#### **Common Error**

```text
Failing to connect to https://registry.k8s.io/ from both inside the minikube container and host machine
To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
```

#### **Solutions**
1. If using a proxy, configure it for Minikube:
   ```bash
   minikube start --docker-env HTTP_PROXY=http://your-proxy:port --docker-env HTTPS_PROXY=https://your-proxy:port
   ```

2. If no proxy is being used, unset these environment variables:
   ```bash
   unset HTTP_PROXY
   unset HTTPS_PROXY
   unset NO_PROXY
   ```

3. Test connectivity to `registry.k8s.io`:
   ```bash
   nslookup registry.k8s.io
   ```
   Example output:
   ```text
   Server:  dlinkrouter.local
   Address:  192.168.0.1

   Non-authoritative answer:
   Name:    registry.k8s.io
   Addresses:  2600:1901:0:bbc4::
             34.96.108.209
   ```

4. Clean up and restart Minikube:
   ```bash
   minikube stop
   minikube delete --all
   ```

---

### **6. Verify Minikube Status**

Check the status of the Minikube cluster:
```bash
minikube status
```

Verify Kubernetes resources:
```bash
kubectl get all -A
kubectl get pods -A
kubectl get nodes -A
```

---

### **7. Adding Nodes**

To add a new node to the cluster:
```bash
minikube start --nodes=2
# or
minikube start --nodes=2 --embed-certs
```

---

### **8. Load Docker Image to Minikube**

1. Verify the Docker images:
   ```bash
   minikube image list
   docker images
   ```
2. Load the Docker image into Minikube:
   ```bash
   minikube image load kubernetes-test-app:latest
   ```

---

### **9. Apply Deployment**

Deploy the application:
```bash
kubectl apply -f deployment.yaml
```

To delete the deployment (if needed):
```bash
kubectl delete deployment kubernetes-test-app
```

---

### **10. Test the Application**

1. Check Pods and Nodes:
   ```bash
   kubectl get pods -A
   kubectl get nodes -A
   ```

2. Delete a specific Pod (optional):
   ```bash
   kubectl delete pod <pod-name/id>
   ```

3. Access the application service:
   ```bash
   minikube service kubernetes-test-app
   ```

4. Open the Minikube dashboard:
   ```bash
   minikube dashboard
   ```

---

### **11. Debugging and Logs**

- View Pod logs:
  ```bash
  kubectl logs -f <pod-id>
  ```

- Check Endpoints and Services:
  ```bash
  kubectl get endpoints
  kubectl get service
  ```

---

### **12. Load Testing with Postman**

1. Use Postman to run performance tests:
   - Go to **Collection > Runs > Performance > Run Performance Test**.
   - Example: Fixed configuration with 10 users for 1 minute.

---

### **13. Stop Minikube**

Stop the Minikube cluster:
```bash
minikube stop
```

---

### **14. Handling ImagePullBackOff Issue**

If you encounter the `ImagePullBackOff` error:

1. Tag the Docker image with your Docker Hub username:
   ```bash
   docker tag kubernetes-test-app:latest <your-dockerhub-username>/kubernetes-test-app:latest
   ```
2. Push the image to Docker Hub:
   ```bash
   docker push <your-dockerhub-username>/kubernetes-test-app:latest
   ```
