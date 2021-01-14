import os
import re
import deployment
from remote_hosts_list import __REMOTE_HOSTS_LIST__
from dirs_to_deploy_list import __DIRS_TO_DEPLOY_LIST__

addon_id = re.sub("deploy_", "", os.path.basename(__file__))[:-3]
deployment = deployment.Deployment()
deployment.deploy(__REMOTE_HOSTS_LIST__, [next(deploy_dir for deploy_dir in __DIRS_TO_DEPLOY_LIST__ if deploy_dir["id"] == addon_id)])