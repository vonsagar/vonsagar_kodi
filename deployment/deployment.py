import os
import paramiko
from remote_hosts_list import __REMOTE_HOSTS_LIST__
from dirs_to_deploy_list import __DIRS_TO_DEPLOY_LIST__


class Deployment:
    client = None

    def __init__(self):
        pass

    def ssh_connect(self, remote_host):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
        self.client.connect(remote_host["address"], 22, remote_host["username"], remote_host["password"])

    def ssh_close_and_reboot(self):
        self.client.exec_command('reboot')
        self.client.close()

    def replace_files(self, remote_host, dir_to_deploy):
        destination_dir_full_path = os.path.join(dir_to_deploy["value"]["dest"], dir_to_deploy["value"]["name"])
        self.client.exec_command('rm -rf ' + destination_dir_full_path.replace("\\", "/"))
        copy_command = "scp -r " + dir_to_deploy["value"]["name"] + " root@" + remote_host["address"] + ":" + \
                       dir_to_deploy["value"]["dest"].replace("\\", "/")
        os.system(copy_command)
        print(dir_to_deploy["value"]["name"] + " -> " + remote_host["id"])

    def deploy(self, remote_hosts_list, dirs_to_deploy_list):
        for remote_host in remote_hosts_list:
            self.ssh_connect(remote_host)

            for dir_to_deploy in dirs_to_deploy_list:
                self.replace_files(remote_host, dir_to_deploy)

            self.ssh_close_and_reboot()


if __name__ == "__main__":
    deployment = Deployment()
    deployment.deploy(__REMOTE_HOSTS_LIST__, __DIRS_TO_DEPLOY_LIST__)
