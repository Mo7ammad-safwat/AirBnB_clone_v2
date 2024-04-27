#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# # All States
all_states = fs.all()
print(all_states)
# # print("All States: {}".format(len(all_states.keys())))
# print("======")
# # print(" all_states.keys(): {}".format((all_states.keys())))
# # print(" all_states.: {}".format((all_states)))
# print("======")

# # for state_key in all_states.keys():
# print()

# # Create a new State
new_state = State()
# print("Test_1: ")
# print(new_state)
# print("Test_: ")
new_state.name = "Abode"
fs.new(new_state)
fs.save()
# print("New State: {}".format(new_state))

# # # All States
# all_states = fs.all()
# print("All States: {}".format(len(all_states.keys())))
# for state_key in all_states.keys():
#     print(all_states[state_key])

# # Create another State
# another_state = State()
# another_state.name = "Nevada"
# fs.new(another_state)
# fs.save()
# print("Another State: {}".format(another_state))
all_states = fs.all()
# # All States
# all_states = fs.all()
# print("All States: {}".format(len(all_states.keys())))
# for state_key in all_states.keys():
#     print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# # All States
# all_states = fs.all()
# print("All States: {}".format(len(all_states.keys())))
# for state_key in all_states.keys():
#     print(all_states[state_key])