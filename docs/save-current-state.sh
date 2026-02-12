#!/bin/bash
# Run this on your machine to save the current helm values before morning session
# This captures the CURRENT state of your cilium helm values

echo "=== Saving current Cilium Helm values ==="
helm get values cilium -n kube-system > ~/cilium-values-base.yaml
echo "Saved to ~/cilium-values-base.yaml"

echo ""
echo "=== Current Helm revision ==="
helm history cilium -n kube-system | tail -5

echo ""
echo "=== Cluster health check ==="
cilium status

echo ""
echo "=== Gateway status ==="
kubectl get gatewayclass cilium
kubectl get gateway main-gateway
kubectl get ciliumenvoyconfigs --all-namespaces

echo ""
echo "=== Node labels ==="
kubectl get nodes -l role=gateway

echo ""
echo "Done! Files saved. Upload cilium-values-base.yaml to tomorrow's chat."
