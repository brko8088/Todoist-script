from pprint import pformat

class Model(object):
  def __init__(self, data, api):
    self.temp_id = "";
    self.data = data
    self.api = api

  def __setitem__(self, key, value):
    self.data[key] = value

  def __getitem__(self, key):
    return self.data[key]

  def __repr(self):
    formatted_dict = pformat(dict(self.data))
    classname = self.__class__.__name__
    return "%s(%s)" % (classname, formatted_dict)

  def __contains__(self, value):
    return value in self.data

class Collaborator(Model):
  """
  Implements a collaborator.
  """

  def delete(self, project_id):
    """
    Deletes a collaborator from a shared project.
    """
    self.api.collaborators.delete(project_id, self["email"])

class CollaboratorState(Model):
    """
    Implements a collaborator state.
    """

    pass

class Filter(Model):
  """
  Implements a filter.
  """

  def update(self, **kwargs):
    """
    Updates filter
    """
    self.api.filters.update(self["id"], **kwargs)
    self.data.update(kwargs)

  def delete(self):
    """
    Deletes filter.
    """
    self.api.filters.delete(self["id"])
    self.data["is_deleted"] = 1