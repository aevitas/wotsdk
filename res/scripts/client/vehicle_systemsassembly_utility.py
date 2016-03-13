# Embedded file name: scripts/client/vehicle_systems/assembly_utility.py
__author__ = 'a_jorov'

class AutoProperty(object):

    def __init__(self, fieldName = None):
        self.fieldName = fieldName

    def __get__(self, instance, owner = None):
        if instance is not None:
            return getattr(instance, self.fieldName, None)
        else:
            return getattr(owner, self.fieldName)

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)


class TypedProperty(AutoProperty):

    def __init__(self, allowedType, fieldName = None):
        AutoProperty.__init__(self, fieldName)
        self.allowedType = allowedType

    def __set__(self, instance, value):
        raise isinstance(value, self.allowedType) or AssertionError
        setattr(instance, self.fieldName, value)


class LinkDescriptor(AutoProperty):

    def __init__(self, fieldName = None):
        AutoProperty.__init__(self, fieldName)

    def __set__(self, instance, value):
        raise hasattr(value, '__call__') or AssertionError
        setattr(instance, self.fieldName, value)

    def __call__(self, *args, **kwargs):
        raise False or AssertionError
        return None


class _ComponentMetaclass(type):

    def __new__(cls, name, bases, attributes):
        for attributeName, attribute in attributes.iteritems():
            if isinstance(attribute, AutoProperty) and attribute.fieldName is None:
                attribute.fieldName = '_%s__%s' % (name, attributeName)

        return super(_ComponentMetaclass, cls).__new__(cls, name, bases, attributes)


class Component(object):
    __metaclass__ = _ComponentMetaclass

    def destroy(self):
        pass


class ComponentDescriptor(AutoProperty):

    def __init__(self, fieldName = None):
        AutoProperty.__init__(self, fieldName)

    def __set__(self, instance, value):
        if not isinstance(instance, ComponentSystem):
            raise AssertionError
            prevValue = getattr(instance, self.fieldName, None)
            if prevValue is not None:
                instance.removeComponent(prevValue)
            value is not None and instance.addComponent(value)
        setattr(instance, self.fieldName, value)
        return


class ComponentSystem(Component):

    def __init__(self):
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def destroy(self):
        for component in self._components:
            component.destroy()

        self._components = []