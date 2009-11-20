##############################################################################
#
# Copyright (c) 2001, 2002, 2009 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""\
Interfaces for the unique id utility.

"""

import zope.interface


class IIntIdsQuery(zope.interface.Interface):

    def getObject(uid):
        """Return an object by its unique id"""

    def getId(ob):
        """Get a unique id of an object.
        """

    def queryObject(uid, default=None):
        """Return an object by its unique id

        Return the default if the uid isn't registered
        """

    def queryId(ob, default=None):
        """Get a unique id of an object.

        Return the default if the object isn't registered
        """

    def __iter__():
        """Return an iteration on the ids"""


class IIntIdsSet(zope.interface.Interface):

    def register(ob):
        """Register an object and returns a unique id generated for it.

        If the object is already registered, its id is returned anyway.
        """

    def unregister(ob):
        """Remove the object from the indexes.

        KeyError is raised if ob is not registered previously.
        """

class IIntIdsManage(zope.interface.Interface):
    """Some methods used by the view."""

    def __len__():
        """Return the number of objects indexed."""

    def items():
        """Return a list of (id, object) pairs."""


class IIntIds(IIntIdsSet, IIntIdsQuery, IIntIdsManage):
    """A utility that assigns unique ids to objects.

    Allows to query object by id and id by object.
    """


class IIntIdsSubclassOverride(zope.interface.Interface):
    """Methods that subclasses can usefully override."""

    def generateId(ob):
        """Return a new iid that isn't already used.

        ``ob`` is the object the id is being generated for.

        The default behavior is to generate arbitrary integers without
        reference to the objects they're generated for.

        """


class IIdEvent(zope.interface.Interface):
    """Generic base interface for IntId-related events"""

    object = zope.interface.Attribute(
        "The object related to this event")

    idmanager = zope.interface.Attribute(
        "The int id utility generating the event.")

    id = zope.interface.Attribute(
        "The id that is being assigned or unassigned.")


class IIdRemovedEvent(IIdEvent):
    """A unique id will be removed

    The event is published before the unique id is removed
    from the utility so that the indexing objects can unindex the object.

    """


class IIdAddedEvent(IIdEvent):
    """A unique id has been added

    The event gets sent when an object is registered in a
    unique id utility.

    """