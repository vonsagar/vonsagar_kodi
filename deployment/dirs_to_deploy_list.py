import os

__DIRS_TO_DEPLOY_LIST__ = [{"id": "seren",       "value": {"name": "plugin.video.seren",         "dest": os.path.join(".kodi", "addons")}},
                           {"id": "fullmatchtv", "value": {"name": "plugin.video.fullmatchtv",   "dest": os.path.join(".kodi", "addons")}},
                           {"id": "autosubs",    "value": {"name": "service.autosubs",           "dest": os.path.join(".kodi", "addons")}},
                           {"id": "subloader",   "value": {"name": "service.subloader",          "dest": os.path.join(".kodi", "addons")}},
                           {"id": "openplayers", "value": {"name": "Players",                    "dest": os.path.join(".kodi", "userdata", "addon_data", "plugin.video.openmeta", "Players")}}
                           ]
