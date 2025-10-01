
![basic!](./docs/lab-simple.png)
# Trailblzaers K8s space 
 objective here is to gain a level of comfort in the cloud native application space. 
### Basic Could Native Application for Lab

## The Rancher Node

### install k3s
K3s is a light weight k8s installtion we will use to house Rancher.
~~~
K3s_VERSION="v1.33.5+k3s1"

curl -sfL https://get.k3s.io | \
        INSTALL_K3S_VERSION=${K3s_VERSION} \
        INSTALL_K3S_EXEC='server --cluster-init --write-kubeconfig-mode=644' \
        sh -s -
~~~
### install helm
we use helm to install rancher and cilium
~~~
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
~~~
### set k8s configs
~~~
mkdir .kube
cp /etc/rancher/k3s/k3s.yaml .kube/config
~~~
### Cert Manager check for version compat

Check the current version for compatibility.
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/<VERSION>/cert-manager.crds.yaml

~~~


helm repo add jetstack https://charts.jetstack.io

helm repo update

kubectl create namespace cert-manager

helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.18.2 \
  --set crds.enabled=true

~~~
### check the cert manager is running
~~~
kubectl get po -n cert-manager
~~~
### Rancher Install

~~~


helm repo add rancher-latest https://releases.rancher.com/server-charts/latest

helm repo update

kubectl create namespace cattle-system

helm install rancher rancher-latest/rancher \
  --namespace cattle-system \
  --set hostname=<instanceip>.sslip.io \
  --set replicas=1 \
  --set bootstrapPassword=Rancher
~~~
*remeber hostname is the public ip and must be permanant*
### check the rancher is running
~~~
watch -n 2 kubectl get po -n cattle-system
~~~

## 2) Node setup Ubuntu (performed on each node in the cluster)

*Disable UFW*
~~~
sudo ufw status
sudo ufw disable
sudo reboot
~~~

#### Define a K8s Cluster
*Use Rancher UI to define and deploy a K8s cluster*
