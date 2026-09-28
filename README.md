# KServe Scikit-Learn Deployment

## Quickstart

1. **Run locally (outside Kubernetes/KServe):**
    ```bash
    docker build -t vimalpillai/modelpredictor .
    docker run -d -p 8000:8000 vimalpillai/modelpredictor
    ```


2. **Install KServe** and cluster serving runtimes for Scikit-Learn on your Kubernetes cluster.
3. **Apply manifests** to configure service accounts and deploy the inference service:
    ```bash
    kubectl apply -f serviceaccount.yaml
    kubectl apply -f inference.yaml
    ```


4. **Test the endpoint** with a sample prediction request:
    ```bash
    curl -s -X POST http://localhost:5000/v1/models/model-predictor:predict \
    -H "Content-Type: application/json" \
    -d '{"instances":[[21, 22, 234, 456, 12]]}'
    ```



---

## Files Overview

* **`serviceaccount.yaml`**: Sets up permissions for pulling model artifacts.
    > **Note:** Do not base64 encode the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` inside this file.


* **`inference.yaml`**: Defines the KServe `InferenceService` custom resource for the Scikit-Learn model.

---


# Argo CD Deployment and Configuration Guide

1. Install Argo CD in the cluster.
2. Create a new application and configure the **General**, **Source**, and **Destination** sections:
   * Enter the application name and project name, and set the sync policy to **Automatic**.
   * Enter the repository details in the **Source** section.
   * Enter the target cluster and namespace details in the **Destination** section.
3. Click **Create**.
4. Edit the secret resource `sa-s3-secret` in the `nano` editor and enter `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in base64-encoded format using the following command:
   ```bash
   echo -n "AKIA..." | base64
    ```
5. Delete the **InferenceService** resource from the Argo CD UI and synchronize that resource again.