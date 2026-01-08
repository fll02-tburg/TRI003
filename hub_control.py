from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4")

# Based on the selection, run a program.
# 1 - hub_initialize flashes the button and plays a sound
if selected == "1":
    import hub_initialize
elif selected == "2":
    import EDG_Journey001
elif selected == "3":
    import North_West_section
elif selected == "4":
    import journey_JCB_001