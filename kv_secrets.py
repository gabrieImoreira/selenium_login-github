import os
import traceback
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def retrieve_credentials():
    try:
        keyVaultName = "github-credenciais"
        KVUri = f"https://github-credenciais.vault.azure.net"

        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)

        secretUsername = client.get_secret("username")
        secretPassword = client.get_secret("password")

        return (True, secretUsername.value, secretPassword.value)
    except:
        return (False, traceback.exc())
        
    
