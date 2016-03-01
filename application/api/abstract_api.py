# encoding: utf-8

from __future__ import division, unicode_literals

import sys

from importlib import import_module
from mongoengine import DoesNotExist


class AbstractApi(object):
    @classmethod
    def _get_model_name(cls):
        """
        Delete the "Api" suffix
        :return: the corresponding class name of for cls
        """
        return cls.__name__[0:len(cls.__name__) - 3]

    @classmethod
    def _get_model_module(cls):
        """
        Import corresponding model
        :return: import the model result
        """
        module = cls.__module__.split(".api", 1)[0] + ".model"
        if module in sys.modules:
            return sys.modules[module]
        else:
            return import_module(module)

    @classmethod
    def _get_model(cls):
        """
        Get model
        :return: the model for this api class
        """
        return eval(cls._get_model_name(), cls._get_model_module().__dict__)

    @classmethod
    def count_all(cls, **kwargs):
        """
        Get the count for all the objects meet the keyword arguments
        :param kwargs: condition dict
        :return: the count for all satisfied objects
        """
        return cls._get_model().objects(**kwargs).count()

    @classmethod
    def rtrv_all(cls, **kwargs):
        """
        Get the object list that meet the keyword arguments
        :param kwargs: condition dict
        :return: list of objects, based on Mongo Document
        """
        return cls._get_model().objects(**kwargs)

    @classmethod
    def rtrv_one(cls, **kwargs):
        """
        Get only one object with primary key, id for most circumstances.
        :param kwargs: condition dict, make sure the object meet the condition is unique
        :return: the object hit
        """
        try:
            obj = cls._get_model().objects.get(**kwargs)
        except DoesNotExist:
            obj = None
        return obj

    @classmethod
    def update_by_id(cls, _id, **kwargs):
        """
        update information
        :param _id: the id of the object, unique
        :param kwargs: the information in dict to be updated
        :return: the updated object
        """
        obj = cls.rtrv_one(id=_id)
        for attr, val in kwargs.iteritems():
            setattr(obj, attr, val)
        obj.save()
        return obj

    @classmethod
    def get_class_name(cls, obj):
        return obj.__class__.__name__

