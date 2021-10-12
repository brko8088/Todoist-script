import datetime
import functools
import json
import os
import uuid

import requests

DEFAULT_API_VERSION = "v8"


class SyncError(Exception):
  pass

class TodoistAPI(object):
  """
  Implements the API that makes it possible to interact with a Todoist user
  account and its data.
  """

  _serialize_fields = ("token", "api_endpoint", "sync_token", "state", "temp_ids")

  @classmethod
  def deserialize(cls, data):
    obj = cls()
    for key in cls._serialize_fields:
      if key in data:
        setattr(obj, key, data[key])
    return obj

  def __init__(
    self,
    token="",
    api_endpoint="https://api.todoist.com",
    api_version=DEFAULT_API_VERSION,
    session=None,
    cache="~/.todoist-sync/",
  ):
    self.api_endpoint = api_endpoint
    self.api_version = api_version
    self.reset_state()
    self.token = token
    self.temp_ids = {}
    self.queue = []
    self.session = session or requests.Session()

    # managers
    self.biz_invitations
    self.collaborators
    self.collaborator_states
    self.filters
    self.invitations
    self.items
    self.labels
    self.live_notifications
    self.locations
    self.notes
    self.projects
    self.project_notes
    self.reminders
    self.sections
    self.user
    self.user_settings

    self.activity
    self.backups
    self.business_users
    self.completed
    self.emials
    self.quick
    self.templates
    self.uploads