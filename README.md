# KServe Scikit-Learn Deployment

## Quickstart

1. **Install KServe** and cluster serving runtimes for Scikit-Learn on your Kubernetes cluster.
2. **Apply manifests** to configure service accounts and deploy the inference service:
```bash
kubectl apply -f serviceaccount.yaml
kubectl apply -f inference.yaml

```


3. **Test the endpoint** with a sample prediction request:
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