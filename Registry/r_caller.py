import registry

r = registry.Registry()

s1 = r.get_service('so')

s1.do_thing()

s1.do_another_thing()

s2 = r.get_service('st')

s2.do_thing()

s2.do_another_thing()