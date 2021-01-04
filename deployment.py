import os
import paramiko

__DIRS_TO_DEPLOY_LIST__ = [{"name": "plugin.video.seren",          "dest": os.path.join(".kodi", "addons")},
                           {"name": "plugin.video.fullmatchtv",    "dest": os.path.join(".kodi", "addons")},
                           {"name": "service.autosubs",            "dest": os.path.join(".kodi", "addons")},
                           {"name": "service.subloader",           "dest": os.path.join(".kodi", "addons")}
                           ]

__REMOTE_HOSTS_LIST__ = ["192.168.1.108",
                         "192.168.1.107"
                         ]

for remote_host in __REMOTE_HOSTS_LIST__:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
    client.connect(remote_host, 22, 'root', 'coreelec')
    
    for dir_to_deploy in __DIRS_TO_DEPLOY_LIST__:
        destination_dir_full_path = os.path.join(dir_to_deploy["dest"], dir_to_deploy["name"])
        client.exec_command('rm -rf ' + destination_dir_full_path.replace("\\", "/"))
        copy_command = "scp -r " + dir_to_deploy["name"] + " root@" + remote_host + ":" + dir_to_deploy["dest"].replace("\\", "/")
        os.system(copy_command)

    client.exec_command('reboot')
    client.close()
