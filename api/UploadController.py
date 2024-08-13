from core.Response import success, fail
from kubernetes import client, config
from azure.mgmt.containerservice import ContainerServiceClient
from azure.identity import ClientSecretCredential
from configs.config import settings

from kubernetes.client.rest import ApiException

class K8sController:
    def __init__(self):
        self.subscription_id = 'd07c204e-68de-4e1f-83f6-7cfa5f6afc0d'
        self.resource_group_name = 'btccndly'
        self.aks_cluster_name = settings.AKS_CLUSTER_NAME
        self.tenant_id = 'de1ad84e-34a8-42c3-a53c-ee4145d07303'
        self.client_id = settings.CLIENT_ID
        self.client_secret = settings.CLIENT_SECRET
        self.resource_manager_url = "https://management.chinacloudapi.cn"
        # Get azure credential
        credential = ClientSecretCredential(tenant_id=self.tenant_id, client_id=self.client_id,
                                    client_secret=self.client_secret, authority="https://login.partner.microsoftonline.cn")
        # Create aks client
        aks_client = ContainerServiceClient(
            credential=credential,
            subscription_id=self.subscription_id,
            base_url=self.resource_manager_url,credential_scopes=[self.resource_manager_url + "/.default"]
        )
        kube_config_obj = aks_client.managed_clusters.list_cluster_admin_credentials(self.resource_group_name, self.aks_cluster_name)
        kubeconfig = kube_config_obj.kubeconfigs[0].value
        # Write kubeconfig files
        with open('kubeconfig', 'wb') as kubeconfig_file:
            kubeconfig_file.write(kubeconfig)
        
    async def get_environment_variable(self,namespace:str,pod_name:str) -> dict:
        """
        """
        try:
            config.load_kube_config(config_file='kubeconfig')
            v1 = client.CoreV1Api()
            pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
            env_vars = {}
            for container in pod.spec.containers:
                for env in container.env:
                    env_vars[env.name] = env.value
        except Exception as e:
            print(e)
            return fail(code=500,data=e,msg="坏了!")
        return success(env_vars,msg="Get env var successfully!")
